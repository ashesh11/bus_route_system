from django.shortcuts import render
from .models import Bus, Route, BusRoute
from django_tables2 import RequestConfig
from .tables import BusTable, RouteTable, RouteForBusTable, BusForRouteTable

def home(request):
    return render(request, 'detail/home.html')

def bus_list(request):
    buses = Bus.objects.all()
    table = BusTable(buses)
    RequestConfig(request, paginate=False).configure(table)
    return render(request, 'detail/bus_list.html', {'table': table})

def route_list_for_bus(request, pk):
    bus = Bus.objects.get(pk=pk)
    routes = BusRoute.objects.filter(bus=bus)
    table = RouteForBusTable(routes)
    RequestConfig(request, paginate=False).configure(table)
    return render(request, 'detail/route_list_for_bus.html', {'table': table, 'bus': bus})

def route_list(request):
    routes = Route.objects.all()
    table = RouteTable(routes)
    RequestConfig(request, paginate=False).configure(table)
    return render(request, 'detail/route_list.html', {'table': table})

def bus_list_for_route(request, pk):
    route = Route.objects.get(pk=pk)
    buses = BusRoute.objects.filter(route=route)
    table = BusForRouteTable(buses)
    RequestConfig(request, paginate=False).configure(table)
    return render(request, 'detail/bus_list_for_route.html', {'table': table, 'route': route})
