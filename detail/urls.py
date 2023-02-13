from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('buses/', views.bus_list, name="bus-list"),
    path('buses/<int:pk>/routes/', views.route_list_for_bus, name="route-for-bus"),
    path('routes/', views.route_list, name="route-list"),
    path('routes/<int:pk>/buses/', views.bus_list_for_route, name="bus-for-route")
]