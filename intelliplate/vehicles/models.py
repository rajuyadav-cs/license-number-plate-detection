from django.db import models


class VehicleLog(models.Model):
    plate_number = models.CharField(max_length=20, blank=True, null=True)
    confidence = models.FloatField(default=0.0)

    uploaded_image = models.ImageField(upload_to="uploads/")
    result_image = models.ImageField(upload_to="results/", blank=True, null=True)
    plate_crop = models.ImageField(upload_to="plate_crops/", blank=True, null=True)

    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.plate_number or 'Unknown Plate'} - {self.confidence}"