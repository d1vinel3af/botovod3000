from django.shortcuts import render


def control_panel(request):
    return render(request, "control_panel/index.html")