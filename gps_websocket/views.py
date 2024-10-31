from django.shortcuts import render

# Create your views here.
# gps_app/views.py
from django.shortcuts import render

def gps_tracker(request):
    return render(request, 'gps_tracker.html')
