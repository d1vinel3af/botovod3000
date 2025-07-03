from django.urls import path

from .views import ControlPanel

urlpatterns = [
    path("", ControlPanel.as_view(), name='control_panel'),
]