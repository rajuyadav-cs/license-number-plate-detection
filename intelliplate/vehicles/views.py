from datetime import datetime, time, timedelta

from django.utils import timezone
from django.views.generic import ListView, DetailView

from .models import VehicleLog


class VehicleHistoryView(ListView):
    model = VehicleLog
    template_name = "vehicles/history.html"
    context_object_name = "vehicle_logs"
    paginate_by = 10

    def get_queryset(self):
        queryset = VehicleLog.objects.all().order_by("-detected_at")

        search = self.request.GET.get("search", "").strip()
        selected_date = self.request.GET.get("date", "").strip()

        if search:
            queryset = queryset.filter(plate_number__icontains=search)

        if selected_date:
            date_obj = datetime.strptime(selected_date, "%Y-%m-%d").date()

            start_datetime = timezone.make_aware(
                datetime.combine(date_obj, time.min)
            )

            end_datetime = timezone.make_aware(
                datetime.combine(date_obj + timedelta(days=1), time.min)
            )

            queryset = queryset.filter(
                detected_at__gte=start_datetime,
                detected_at__lt=end_datetime
            )

        return queryset


class VehicleDetailView(DetailView):
    model = VehicleLog
    template_name = "vehicles/detail.html"
    context_object_name = "vehicle"