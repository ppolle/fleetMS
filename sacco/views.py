from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Sacco, Super_list
from .forms import SaccoForm, Super_listForm, EditProfile, EditSupervisor
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from owner.models import Owner, Vehicle
from django.views import View

# Create your views here.

@login_required(login_url='/loginViews/')
def dashboard(request):
    '''
    View function to display all that a user will be interacting with fromm the onset of the app.
    '''
    supervisor = Super_list.objects.filter(sacco = Sacco.objects.get(pk=request.user.sacco.id))
    owner = Owner.objects.filter(sacco = Sacco.objects.get(pk=request.user.sacco.id))
    return render(request, 'sacco/all/dashboard.html', {"supervisor": supervisor, "owner": owner})

# Supervisor section

@login_required(login_url='/loginViews/')
def superlist(request):
    '''
    View function to add a new supervisor
    '''
    if request.method == 'POST':
        form = Super_listForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.sacco = Sacco.objects.get(user = request.user)
            '''
            above line of code displays a supervisor registered in a specific sacco
            '''
            user.save()
            messages.success(request, f'Congratulations! You have succesfully Added a new Supervisor!')
            return redirect('sacco:sacco_home')
    else:
        form = Super_listForm()
    return render(request, 'sacco/all/supervisor.html', {"form": form})

@login_required(login_url='/loginViews/')
def edit_superlist(request, supervisor_id):
    '''
    View function to edit an instance of a supervisor already created
    '''
    supervisor = Super_list.objects.get(pk=supervisor_id)
    if request.method == 'POST':
        form = EditSupervisor(request.POST, instance=supervisor)
        if form.is_valid():
            form.save()
            messages.success(request, f'Success! Your edit has been successful!')
            return redirect('sacco:sacco_home')
    else:
        form = EditSupervisor(instance=supervisor)
    return render(request, 'sacco/all/editsupervisor.html', {"form": form, "supervisor":supervisor})

@login_required(login_url='/loginViews/')
def delete_supervisor(request, supervisorID):
    '''
    View function that enables one delete a given supervisor in a sacco
    '''
    
    Super_list.objects.filter(pk=supervisorID).delete()
    messages.error(
        request, f'Supervisor deleted!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Sacco section
@login_required(login_url='/loginViews/')
def profile(request):
    profile = Sacco.objects.get(user=request.user)
    return render(request, "sacco/all/profile.html", {"profile": profile})

@login_required(login_url='/loginViews/')
def edit_profile(request, sacco_id):
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES,instance = Sacco.objects.get(pk = sacco_id))
        if form.is_valid():
            form.save()
            messages.success(request, f'Success! Your edit has been successful!')
            return redirect('sacco:profile')
    else:
        form = SaccoForm(instance = Sacco.objects.get(pk = sacco_id))
    return render(request, 'sacco/all/editprofile.html', {"form": form})

@login_required(login_url='/loginViews/')
def delete_sacco(request, saccoID):
    '''
    View function that enables deletion of a sacco instance
    '''
    Sacco.objects.filter(pk=saccoID).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Owner section
def owner_details(request, ownerID):
    '''
    View function to display an owner and all their details.
    '''
    owner = Owner.objects.filter(id=ownerID)
    car_owned = Vehicle.objects.filter(owner=ownerID)
    return render(request, 'sacco/all/ownerdetails.html', {"owner": owner, "car_owned": car_owned})


def saccoFleet(request):
    '''
    View class to manage viewing all of the sacco fleet
    '''
    
    fleet = Vehicle.objects.filter(sacco = request.user.sacco.id)
    return render(request,'sacco/all/fleet.html',{'fleet':fleet})

def saccoMembers(request):
    '''
    View function to retrive all member instances of a particular sacco
    '''

    members = Owner.objects.filter(sacco = Sacco.objects.get(pk=request.user.sacco.id))
    return render(request,'sacco/all/members.html',{"members":members})

def saccoSupervisors(request):
    '''
    View function to retrieve all sacco supervisor instances
    '''
    supervisors = Super_list.objects.filter(sacco = Sacco.objects.get(pk=request.user.sacco.id))
    return render(request,'sacco/all/supervisors.html',{"supervisors":supervisors})
