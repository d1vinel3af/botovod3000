from django.shortcuts import render
from bots.models import BotModel

def control_panel(request):
    list_bots = BotModel.objects.all()

    return render(request, "control_panel/index.html",
                  context={
                      "bots": list_bots
                  })