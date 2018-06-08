from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import OwnerSignUpForm
# from .models import Neighbourhood,Business,Profile,Join,Posts,Comments
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
	'''
	Function to render the home page
	'''
	return render(request, 'home/home.html')

def ownerSignup(request):
	'''
	View function that will manage user signup
	'''
	if request.method == 'POST':
		form = OwnerSignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit = False)
			user.roles = 'owner'
			user.refresh_from_db()
			user.owner.nat_id = form.cleaned_data.get('national_id')
			# user.owner.sacco = form.cleaned_data.get('sacco')
			
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username = user.username,password = raw_password)
			login(request,user)
			messages.success(request, 'Success! Signup was a success!')
			return redirect ('home')
	else:
		form = OwnerSignUpForm()
		return render(request,'authentication/owner_signup.html',{"form":form})