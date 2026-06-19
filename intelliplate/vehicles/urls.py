from django.urls import path
from .views import VehicleHistoryView, VehicleDetailView

urlpatterns = [
    path("history/", VehicleHistoryView.as_view(), name="vehicle_history"),
    path("history/<int:pk>/", VehicleDetailView.as_view(), name="vehicle_detail"),
]