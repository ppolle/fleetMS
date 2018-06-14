from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Sacco, Super_list
from .forms import SaccoForm, Super_listForm, EditProfile, EditSupervisor
from django.contrib import messages

# Create your views here.

def dashboard(request):
    '''
    View function to display all that a user will be interacting with fromm the onset of the app.
    '''
    supervisor = Super_list.objects.filter(sacco = Sacco.objects.get(pk=request.user.sacco.id))
    return render(request, 'all/dashboard.html', {"supervisor": supervisor})

# Supervisor section

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
    return render(request, 'all/supervisor.html', {"form": form})

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
    return render(request, 'all/editsupervisor.html', {"form": form, "supervisor":supervisor})

def delete_supervisor(request, supervisorID):
    '''
    View function that enables one delete a given supervisor in a sacco
    '''
    
    Super_list.objects.filter(pk=supervisorID).delete()
    messages.success(
        request, f'Supervisor deleted!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Sacco section

def profile(request, sacco_id):
    current_user = request.user
    profiles = Sacco.objects.filter(user__id__iexact=sacco_id)
    profile = Sacco.objects.get(user=sacco_id)
    all_profile = Sacco.objects.all()
    content = {
        "profiles": profiles,
        "profile": profile,
        "user": current_user,
        "profile_id": sacco_id,
        "all_profile": all_profile
    }
    return render(request, "all/profile.html", content)


def edit_profile(request, sacco_id):
    # profile = request.user.profile
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES,instance = Sacco.objects.get(pk = sacco_id))
        if form.is_valid():
            current_user = request.user
            form.save()
            return redirect('sacco:profile', current_user.sacco.id)
    else:
        form = EditProfile(instance = Sacco.objects.get(pk = sacco_id))
    return render(request, 'all/editprofile.html', {"form": form})

def delete_sacco(request, saccoID):
    '''
    View function that enables one delete a given sacco
    '''
    Sacco.objects.filter(pk=saccoID).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

