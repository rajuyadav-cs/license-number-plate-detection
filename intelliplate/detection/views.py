from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from .forms import ImageUploadForm
from .services.plate_detector import detect_license_plate
from vehicles.models import VehicleLog


class DetectImageView(FormView):
    template_name = "detection/detect.html"
    form_class = ImageUploadForm
    success_url = reverse_lazy("detect")

    def form_valid(self, form):
        image = form.cleaned_data["image"]

        fs = FileSystemStorage(location=settings.MEDIA_ROOT / "uploads")
        filename = fs.save(image.name, image)

        uploaded_image_path = settings.MEDIA_ROOT / "uploads" / filename
        uploaded_image_url = f"{settings.MEDIA_URL}uploads/{filename}"

        detection_result = detect_license_plate(uploaded_image_path)

        vehicle_log = VehicleLog.objects.create(
            plate_number=detection_result["plate_number"],
            confidence=detection_result["confidence"],
            uploaded_image=f"uploads/{filename}",
            result_image=detection_result["result_image_path"],
            plate_crop=detection_result["plate_crop_path"],
        )

        return self.render_to_response(
            self.get_context_data(
                form=form,
                vehicle_log=vehicle_log,
                plate_number=detection_result["plate_number"],
                uploaded_image_url=uploaded_image_url,
                result_image_url=detection_result["result_image_url"],
                plate_crop_url=detection_result["plate_crop_url"],
                detections_count=detection_result["detections_count"],
                confidence=detection_result["confidence"],
            )
        )