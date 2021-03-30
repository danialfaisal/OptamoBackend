from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import requests

class Weather(models.Model):
    station_id = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    precipitation = models.CharField(max_length=200)
    temp_min = models.CharField(max_length=200)
    temp_max = models.CharField(max_length=200)
    snowfall = models.CharField(max_length=200)


    def __str__(self):
        return str(self.station_id)



