from rest_framework import serializers
from .models import Weather


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
            model = Weather
            fields = ('station_id','state', 'precipitation', 'temp_min', 'temp_max', 'snowfall')


