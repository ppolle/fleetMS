from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import OwnerSignUpForm,SaccoSignUpForm
from sacco.models import Sacco
from owner.models import Owner
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
	return render(request,'authentication/choice.html')

def logout(request):
	'''
	View function to handle loggin out users
	'''
	logout(request)
	messages.success(request, 'Successfully logged-Out. Please come back again!')
	return redirect('home')

def ownerSignup(request):
	'''
	View function that will manage user signup
	'''
	if request.method == 'POST':
		form = OwnerSignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit = False)
			user.roles = 'owner'
			user.save()
			# user.refresh_from_db()
			# user.owner.nat_id = form.cleaned_data.get('national_id')
			# user.owner.sacco = form.cleaned_data.get('sacco')
			

			owner= Owner.objects.create(user=user)
			owner.refresh_from_db()
			owner.nat_id = form.cleaned_data.get('national_id')
			owner.sacco = form.cleaned_data.get('sacco')
			owner.save()
			
			# user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username = user.username,password = raw_password)
			login(request,user)
			messages.success(request, 'Success! Signup was a success!')
			return redirect ('home')
	else:
		form = OwnerSignUpForm()
		return render(request,'authentication/owner_signup.html',{"form":form})

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
			user.sacco.registration_no = form.cleaned_data.get('registration_no')

			user.save()

			# user.refresh_from_db()
			# sacco = Sacco.objects.create(user = user)
			# sacco.refresh_from_db()


			# sacco.name = form.cleaded_data.get('name')
			# sacco.registration_no =  forms.cleaned_data.get('registration_no')
			# sacco.save()

			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username = user.username,password = raw_password)
			login(request,user)
			messages.success(request, 'Success! You have succesfullly created a new sacco!')
			return render(request,'home/home.html')
	else:
		form = SaccoSignUpForm()
		return render(request,'authentication/sacco_signup.html',{"form":form})

