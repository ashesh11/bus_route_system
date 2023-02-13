
import django_tables2 as tables
from django_tables2 import A
from .models import Bus, Route, BusRoute

class BusTable(tables.Table):
    routes_count = tables.RelatedLinkColumn(
        'route-for-bus',
        args=[A('pk')]
    )
    class Meta:
        model = Bus
        template_name = "django_tables2/bootstrap.html"
        fields = ("bus_name", "bus_number", "routes_count")


class RouteForBusTable(tables.Table):
    from_time = tables.DateTimeColumn(format="M. d, Y, g:i a")
    to_time = tables.DateTimeColumn(format="M. d, Y, g:i a")

    class Meta:
        model = BusRoute
        template_name = "django_tables2/bootstrap.html"
        fields = ("route__route_name", "route__route_number", "from_time", "to_time")


class RouteTable(tables.Table):
    buses_count = tables.RelatedLinkColumn(
        'bus-for-route',
        args=[A('pk')]
    )
    class Meta:
        model = Route
        template_name = "django_tables2/bootstrap.html"
        fields = ("route_name", "route_number", "buses_count")


class BusForRouteTable(tables.Table):
    from_time = tables.DateTimeColumn(format="M. d, Y, g:i a")
    to_time = tables.DateTimeColumn(format="M. d, Y, g:i a")

    class Meta:
        model = BusRoute
        template_name = "django_tables2/bootstrap.html"
        fields = ("bus__bus_name", "bus__bus_number", "from_time", "to_time")