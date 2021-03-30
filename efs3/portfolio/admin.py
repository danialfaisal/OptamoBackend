from django.contrib import admin
from .models import Weather

class WeatherList(admin.ModelAdmin):
    list_display = ('station_id', 'state', 'precipitation', 'temp_min', 'temp_max', 'snowfall')
    list_filter = ('station_id', 'state', 'precipitation')
    search_fields = ('station_id', 'state')
    ordering = ['station_id']


admin.site.register(Weather, WeatherList)

