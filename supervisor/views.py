from django.shortcuts import render

# Create your views here.


def supervisor(request):
    return render(request, 'supervisor/supervisor.html')
