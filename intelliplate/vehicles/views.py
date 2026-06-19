from django.views.generic import ListView, DetailView
from .models import VehicleLog


class VehicleHistoryView(ListView):
    model = VehicleLog
    template_name = "vehicles/history.html"
    context_object_name = "vehicle_logs"
    paginate_by = 10

    def get_queryset(self):
        queryset = VehicleLog.objects.all().order_by("-detected_at")

        search = self.request.GET.get("search")
        date = self.request.GET.get("date")

        if search:
            queryset = queryset.filter(plate_number__icontains=search)

        if date:
            queryset = queryset.filter(detected_at__date=date)

        return queryset


class VehicleDetailView(DetailView):
    model = VehicleLog
    template_name = "vehicles/detail.html"
    context_object_name = "vehicle"