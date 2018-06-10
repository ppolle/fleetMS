from django.shortcuts import render, redirect
from .models import Sacco, Super_list
from .forms import SaccoForm, Super_listForm, EditProfile

# Create your views here.

def dashboard(request):
    '''
    View function to display all that a user will be interacting with fromm the onset of the app.
    '''
    return render(request, 'all/dashboard.html')

# def sacco(request):
#     '''
#     View function to enable one register a new sacco
#     '''
#     current_user = request.user
#     if request.method == 'POST':
#         user_form = SaccoForm(data=request.POST)
#         if user_form.is_valid():
#             post = user_form.save(commit=False)
#             post.user = current_user
#             post.save()
#             return redirect('sacco_home')
#     else:
#         user_form = SaccoForm()
#     return render(request, 'all/sacco.html', {"user_form": user_form})


def superlist(request):
    current_user = request.user
    if request.method == 'POST':
        form = Super_listForm(request.POST)
        if form.is_valid():
            supervisor = form.save(commit=False)
            supervisor.user = current_user
            supervisor.save()
            return redirect('sacco_home')
    else:
        form = Super_listForm()
    return render(request, 'all/supervisor.html', {"form": form})


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


def edit_profile(request):
    # profile = request.user.profile
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile', current_user.id)
    else:
        form = EditProfile()
    return render(request, 'all/editprofile.html', {"form": form})
