from django.urls import path
from .views import DetectImageView

urlpatterns = [
    path('', DetectImageView.as_view(), name='detect'),
]