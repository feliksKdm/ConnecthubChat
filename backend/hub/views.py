# Create your views here.
from django.shortcuts import render
from django.conf import settings

DEBUG = False

def home_screen_view(request):
	context = {}
	return render(request, "hub/home.html", context)