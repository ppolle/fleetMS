from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from supervisor.models import Driver, Conductor, AssignCrew, Supervisor
from .models import Owner, Vehicle
from supervisor.models import Issue
from .forms import VehicleForm, EditProfile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/loginViews/')
def home(request):
    vehicle = Vehicle.objects.filter(owner=request.user.owner)
    return render(request, 'owner/homepage.html', {"vehicle": vehicle})


def profile(request):
    profile = Owner.objects.get(user=request.user)
    return render(request, 'owner/profile.html', {"profile": profile})


@login_required(login_url='/loginViews/')
def vehicle(request):
    '''
    View function to add a new vehicle
    '''
    if request.method == 'POST':
        if Vehicle.objects.filter(owner=request.user.owner.id).count() >= 4:
            messages.error(request, f'Error! You have registered the maxmimum number of vehicles')
            return redirect("owner:home")
        else:

            form = VehicleForm(request.POST)
            if form.is_valid():
                vehicle = form.save(commit=False)
                vehicle.owner = request.user.owner

                vehicle.sacco = request.user.owner.sacco
                vehicle.save()

                messages.success(
                    request, f'Congratulations! You have succesfully Added a new Vehicle!')
                return redirect('owner:home')
    else:
        form = VehicleForm()
    return render(request, 'owner/vehicle.html', {"form": form})


@login_required(login_url='/loginViews/')
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


@login_required(login_url='/loginViews/')
def deleteVehicle(request, owner_id):
    '''
    View function that enables one delete a given supervisor in a sacco
    '''

    Vehicle.objects.filter(pk=owner_id).delete()
    messages.error(
        request, f'Vehicle deleted!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/loginViews/')
def editProfile(request, owner_id):
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES,
                           instance=Owner.objects.get(pk=owner_id))
        if form.is_valid():
            form.save()
            messages.success(
        request, f'Succesfull Edited your profile!')
            return redirect('owner:profile')
    else:
        form = EditProfile(instance=Owner.objects.get(pk=owner_id))
    return render(request, 'owner/editProfile.html', {"form": form})


@login_required(login_url='/loginViews/')
def crewDetails(request, vehicleId):
    '''
    View function that enables one delete a given supervisor in a sacco

    '''
    if AssignCrew.objects.filter(vehicle_id = vehicleId).exists():
        crews = AssignCrew.objects.filter(vehicle_id = vehicleId)
        return render(request, 'owner/crewDetails.html', {"crews":crews})
    else:
        crews = AssignCrew.objects.filter(vehicle_id = vehicleId)
        owner = Vehicle.objects.get(id = vehicleId)
        return render(request,'owner/crewDetails.html',{"crews":crews,"owner":owner})

    

