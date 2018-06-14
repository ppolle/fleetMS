from django.shortcuts import render
from django.http  import Http404
from .models import Owner
# Create your views here.

def home(request):
    return render(request, 'homepage.html',{})


def profile(request):
    return render(request, 'profile.html')
def search(request):
    pass
