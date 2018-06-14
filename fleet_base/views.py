from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import (Http404, HttpResponse, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import redirect, render

from owner.models import Owner
from sacco.models import Sacco
from supervisor.views import supervisor

from .forms import OwnerSignUpForm, SaccoSignUpForm

# Create your views here.


def home(request):
    '''
    Function to render the home page
    '''
    return render(request, 'home/home.html')


def select(request):
    '''
    View function to select the apppropriate signup page
    '''
    return render(request, 'authentication/choice.html')


def ownerSignup(request):
    '''
    View function that will manage user signup
    '''
    if request.method == 'POST':
        form = OwnerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.roles = 'owner'
            user.save()

            owner = Owner.objects.create(user=user)
            owner.refresh_from_db()
            owner.nat_id = form.cleaned_data.get('national_id')
            owner.sacco = form.cleaned_data.get('sacco')
            owner.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            user_login(request, user)
            messages.success(request, 'Success! Signup was a success!')
            return render(request, 'home/home.html')
    else:
        form = OwnerSignUpForm()
        return render(request, 'authentication/owner_signup.html', {"form": form})


def saccoSignup(request):
    '''
    View function that will manage sacco signup
    '''
    if request.method == 'POST':
        form = SaccoSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            user.refresh_from_db()
            user.roles = 'sacco'
            user.sacco.name = form.cleaned_data.get('name')
            user.sacco.registration_no = form.cleaned_data.get(
                'registration_no')

            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            user_login(request, user)
            messages.success(
                request, 'Success! You have succesfullly created a new sacco!')
            return render(request, 'home/home.html')
    else:
        form = SaccoSignUpForm()
        return render(request, 'authentication/sacco_signup.html', {"form": form})


def login(request):
    '''
    View function that will manage user authentication
    '''
    if request.GET.get('username') and request.GET.get("password"):
        username = request.GET.get("username")
        password = request.GET.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)

            if user.roles == 'owner':

                messages.success(
                    request, 'Success! Owner has succesfully logged in!')
                return render(request, 'home/home.html')
            else:
                messages.success(
                    request, 'Success! Sacco has succesfully logged in!')
                return render(request, 'home/home.html')
        else:
            messages.error(
                request, 'wrong username or password combination. try again!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(
            request, 'You did not input any username or password. Try Again!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def loginViews(request):
    '''
    View function to render login page
    '''
    return render(request, 'authentication/login.html')


def logout(request):
    '''
    View function to handle loggin out users
    '''
    user_logout(request)
    messages.error(request, 'Successfully logged-Out. Please come back again!')
    return redirect('home')
