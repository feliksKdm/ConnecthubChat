from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    context = {}
    return render(request, 'hub/home.html')