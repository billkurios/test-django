from django.db import models
from uuid import uuid1
import csv
import os


class FileTypeChoices(models.TextChoices):
    CSV = "CSV", "CSV"
    UNKNOWN = "UNKNOWN", "Unknown"


class FileUpload(models.Model):
    clef = models.CharField(
        primary_key=True, default=uuid1().hex.upper(), max_length=33
    )  # For public use
    name = models.CharField(blank=False, max_length=150)
    type = models.CharField(
        max_length=10, choices=FileTypeChoices.choices, default=FileTypeChoices.UNKNOWN
    )
    structure = models.JSONField()
    data = models.JSONField()

    @staticmethod
    def save_csv_file(filepath, quotechar=" ", newline="", delimiter="|"):
        with open(filepath, "r", newline=newline) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
            structure = None
            data = {}
            current_index = 0
            for row in csv_reader:
                if structure is None:
                    structure = row  # the first line contains columns names
                    continue
                data[current_index] = row
                current_index += 1
            filename = os.path.basename(filepath).split(".")[0]
            # create a new record
            return FileUpload.objects.create(
                name=filename, type=FileTypeChoices.CSV, structure=structure, data=data
            )
