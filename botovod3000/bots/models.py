from django.db import models

# Create your models here.
class BotModel(models.Model):
    title = models.CharField(max_length=10)
    pair = models.CharField(max_length=10)
    status = models.CharField(max_length=5)
    profit = models.FloatField()

    def __str__(self):
        return f"{self.title} | {self.pair} | {self.status}"