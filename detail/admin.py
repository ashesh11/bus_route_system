from django.contrib import admin
from . import models

@admin.register(models.Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ['id', 'bus_name', 'bus_number']

@admin.register(models.Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['id', 'route_name', 'route_number']

@admin.register(models.BusRoute)
class BusRouteAdmin(admin.ModelAdmin):
    list_display = ['id', 'bus', 'route', 'from_time', 'to_time']
