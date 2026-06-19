from django.views.generic import TemplateView
from django.utils import timezone
from vehicles.models import VehicleLog


class Home(TemplateView):
    template_name = "home.html"


class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_detections = VehicleLog.objects.count()

        today = timezone.now().date()

        today_detections = VehicleLog.objects.filter(
            detected_at__date=today
        ).count()

        avg_confidence = (
            VehicleLog.objects.all()
            .values_list("confidence", flat=True)
        )

        if avg_confidence:
            avg_confidence = round(
                sum(avg_confidence) / len(avg_confidence), 2
            )
        else:
            avg_confidence = 0

        recent_detections = VehicleLog.objects.order_by(
            "-detected_at"
        )[:5]

        context.update({
            "total_detections": total_detections,
            "today_detections": today_detections,
            "avg_confidence": avg_confidence,
            "recent_detections": recent_detections,
        })

        return context