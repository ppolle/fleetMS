from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import (Http404, HttpResponse, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import redirect, render
from django.urls import reverse

from owner.models import Owner
from sacco.models import Sacco, Super_list
from supervisor.models import Supervisor

from .forms import OwnerSignUpForm, SaccoSignUpForm, SupervisorSignupForm

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
            return redirect('fleet:index')

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
            return redirect('sacco:edit', user.sacco.id)
    else:
        form = SaccoSignUpForm()
    return render(request, 'authentication/sacco_signup.html', {"form": form})


def supSignup(request):
    '''
    View function that will manage supervisor signup
    '''
    if request.method == 'POST':
        form = SupervisorSignupForm(request.POST)

        if form.is_valid():
            if Super_list.objects.filter(id_number=form.cleaned_data.get('id_number')).exists():
                user = form.save(commit=False)
                user.roles = 'supervisor'
                user.sacco_base = Super_list
                user.save()

                supervisor = Supervisor.objects.create(user=user)
                supervisor.refresh_from_db()
                supervisor.id_number = form.cleaned_data.get('id_number')
                supervisor.date_of_birth = form.cleaned_data.get('birth_date')
                supervisor.save()

                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username,
                                    password=raw_password)
                user_login(request, user)
                messages.success(request, f'Success! Welcome to you new dahsboard {user.first_name}')
                return render(request, 'home/home.html')

            else:
                messages.error(
                    request, 'Error! Make sure your respective sacco has already registered you on the platform!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = SupervisorSignupForm()
        return render(request, 'authentication/supervisor_signup.html', {"form": form})


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

                messages.success(request, f'Welcome back {request.user.first_name} {request.user.last_name}!')
                return redirect('fleet:index')
            else:
                messages.success(request, f'Success! {request.user.sacco.name} has succesfully logged in!')
                return redirect('sacco:sacco_home')
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
    return redirect('fleet:index')
