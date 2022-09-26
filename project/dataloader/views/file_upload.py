from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from ..models import FileUpload


"""
Views to create and read FileUpload records
"""


@method_decorator(csrf_exempt, name="dispatch")
class FileUploadCRView(View):
    def post(self, request):
        filepath = request.POST.get("filepath", None)
        if not filepath:
            return JsonResponse({"error": "Unvalid filepath"}, status=400)
        record = FileUpload.save_csv_file(filepath)
        return JsonResponse(
            {
                "filename": record.name,
                "columns": str(record.structure),
                "rows": list(record.data.values()),
            },
            status=201,
        )

    def get(self, request):
        return JsonResponse({"message": "Not yet implemented"}, status=201)


"""
Views to update and delete FileUpload record
"""


@method_decorator(csrf_exempt, name="dispatch")
class FileUploadUDView(View):
    def patch(self, request, item_id):
        return JsonResponse({"message": "Not yet implemented"}, status=201)

    def delete(self, request, item_id):
        return JsonResponse({"message": "Not yet implemented"}, status=201)
