from django.urls import path
from . import views

urlpatterns = [
  path('', views.vehicle_view, name='vehicle_view'),
]