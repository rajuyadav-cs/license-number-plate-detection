from django.contrib import admin
from .models import VehicleLog


@admin.register(VehicleLog)
class VehicleLogAdmin(admin.ModelAdmin):
    list_display = ("id", "plate_number", "confidence", "detected_at")
    search_fields = ("plate_number",)
    list_filter = ("detected_at",)