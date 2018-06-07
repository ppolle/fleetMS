from django.shortcuts import render

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