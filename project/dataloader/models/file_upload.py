from django.db import models
from uuid import uuid1


class FileTypeChoices(models.TextChoices):
    CSV = "CSV", "CSV"
    UNKNOWN = "UNKNOWN", "Unknown"


class FileUpload(models.Model):
    id = models.BigAutoField(primary_key=True, default=uuid1().int)
    clef = models.CharField(
        unique=True, default=uuid1().hex.upper(), max_length=33
    )  # For public use
    name = models.CharField(blank=False, max_length=150)
    type = models.CharField(
        max_length=10, choices=FileTypeChoices.choices, default=FileTypeChoices.UNKNOWN
    )
    structure = models.JSONField()
    data = models.JSONField()
