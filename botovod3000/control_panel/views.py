from django.shortcuts import render
from django.views.generic import TemplateView



class ControlPanel(TemplateView):
    template_name = "control_panel/index.html"