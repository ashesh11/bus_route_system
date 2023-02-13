from django.db import models
from django.urls import reverse
from datetime import datetime

class Bus(models.Model):
    bus_name = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=100)
    routes = models.ManyToManyField('Route', through='BusRoute')

    def __str__(self) -> str:
        return self.bus_name


    @property
    def routes_count(self):
        return self.routes.count()


class Route(models.Model):
    route_name = models.CharField(max_length=100)
    route_number = models.CharField(max_length=100)
    buses = models.ManyToManyField('Bus', through='BusRoute')

    def __str__(self) -> str:
        return self.route_name

    @property
    def buses_count(self):
        return self.buses.count()

class BusRoute(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.bus.bus_name} ({self.bus.bus_number}), {self.route}'

    class Meta:
        unique_together = ['bus', 'from_time', 'to_time']