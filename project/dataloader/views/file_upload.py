from django.views import View
from django.http import JsonResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from ..models import FileUpload


"""
Views to create and read FileUpload records
"""


@method_decorator(csrf_exempt, name="dispatch")
class FileUploadCRView(View):
    def post(self, request):
        # data = request.body.decode("utf-8")
        data = {"message": "New item added"}
        return JsonResponse(data, status=201)

    def get(self, request):
        pass


"""
Views to update and delete FileUpload record
"""


@method_decorator(csrf_exempt, name="dispatch")
class FileUploadUDView(View):
    def patch(self, request, item_id):
        pass

    def delete(self, request, item_id):
        pass
