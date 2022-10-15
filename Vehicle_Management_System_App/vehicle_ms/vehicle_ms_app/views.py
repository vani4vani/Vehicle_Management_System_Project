#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vehicle_view(request):
    return HttpResponse("<h1>Vehicle Management Stystem</h1>")