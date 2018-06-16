from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Owner, Vehicle
from .forms import VehicleForm, EditProfile
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    vehicle = Vehicle.objects.filter(owner = request.user.owner)
    return render(request, 'owner/homepage.html', {"vehicle": vehicle})


def profile(request):
    profile = Owner.objects.get(user=request.user)
    return render(request, 'owner/profile.html', {"profile": profile})


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


def editVehicle(request, owner_id):
    '''
    View function to edit an instance of a supervisor already created
    '''
    vehicle = Vehicle.objects.get(pk=owner_id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Success! Your edit has been successful!')
            return redirect('owner:home')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'owner/editVehicle.html', {"form": form, "vehicle": vehicle})


def deleteVehicle(request, owner_id):
    '''
    View function that enables one delete a given supervisor in a sacco
    '''

    Vehicle.objects.filter(pk=owner_id).delete()
    messages.error(
        request, f'Vehicle deleted!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def editProfile(request, owner_id):
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES,
                           instance=Owner.objects.get(pk=owner_id))
        if form.is_valid():
            form.save()
            return redirect('owner:profile')
    else:
        form = EditProfile(instance=Owner.objects.get(pk=owner_id))
    return render(request, 'owner/editProfile.html', {"form": form})
