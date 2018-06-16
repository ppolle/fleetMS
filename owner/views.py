from django.shortcuts import render, redirect, get_object_or_404
from django.http  import Http404, HttpResponse
from .models import Owner, Vehicle
from .forms import VehicleForm
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    vehicle = Vehicle.objects.filter(owner = request.user.owner)
    return render(request, 'owner/homepage.html', {"vehicle": vehicle})


def profile(request):
    return render(request, 'owner/profile.html')
def search(request):
    pass


def vehicle(request):
    '''
    View function to add a new vehicle
    '''
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.owner = request.user.owner
            # user.vehicle = Vehicle.objects.all().filter(owner.user=request.user)
            vehicle.save()
            messages.success(
                request, f'Congratulations! You have succesfully Added a new Vehicle!')
            return redirect('owner:home')
    else:
        form = VehicleForm()
    return render(request, 'owner/vehicle.html', {"form": form})
