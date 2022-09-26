from django.test import TestCase

from ..models import FileUpload


"""
Ces differents cas de tests ne concernent uniquement
l'upload de fichier de type .csv
"""


class FileUploadCSVTestCase(TestCase):
    def test_unknown_file(self):
        """
        Dans ce cas de test, le nom fichier
        renseigne est invalide. Donc la reponse
        doit etre un message d'erreur
        """
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            response = self.client.post(
                "/upload-file/",
                {"filepath": "upload/unknow_file.csv"},
            )
        self.assertEqual(response.status_code, 404)  # Not found

    def test_bad_extension(self):
        """
        Dans ce cas de test, l'extension du fichier
        n'est pas .csv
        La reponse attendu est une erreur
        """
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            response = self.client.post(
                "/upload-file/",
                {"filepath": "upload/other_file.txt"},
            )
        self.assertEqual(response.status_code, 400)  # Bad request

    def test_good_file_but_no_header(self):
        """
        Dans ce cas de test, il s'agit bien d'un fichier .csv
        mais la structure du fichier n'as pas d'entete
        L'api doit neanmoins traite ce fichier et confirme
        par un message de succes
        """
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            response = self.client.post(
                "/upload-file/",
                {"filepath": "upload/no_header_file.csv"},
            )
        self.assertEqual(response.status_code, 201)  # Record created

    def test_empty_file(self):
        """
        Dans ce cas de test, le fichier est vide
        Nous devons renvoyer un message d'erreur
        """
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            response = self.client.post(
                "/upload-file/",
                {"filepath": "upload/empty_file.csv"},
            )
        self.assertEqual(response.status_code, 400)  # Bad request

    def test_good_file(self):
        """
        fichier modele attendu
        """
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            response = self.client.post(
                "/upload-file/",
                {"filepath": "upload/model_file.csv"},
            )
        self.assertEqual(response.status_code, 201)  # Record created
