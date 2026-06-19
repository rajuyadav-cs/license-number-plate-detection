from django.urls import path
from .views import Home, DashboardView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]