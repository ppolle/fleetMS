from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def supervisor(request):
    return render(request, 'supervisor/supervisor.html')


def new_supervisor(request):
    return render(request, 'supervisor/new_supervisor.html')
