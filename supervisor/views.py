from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SupervisorForm
# Create your views here.


def home(request):
    return render(request, 'supervisor/dashboard/index.html')

def editSupervisor(request):
	'''
	Edit a created supervisor
	'''
	if request.method == 'POST':
		form = SupervisorForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Success! Your edit has been successful!')
			return redirect('sup:dashboard')


	else:
		form = SupervisorForm()
		return render(request,'supervisor/dashboard/edit.html',{"form":form})


def supervisor(request):
    return render(request, 'supervisor/supervisor.html')


def new_supervisor(request):
    return render(request, 'supervisor/new_supervisor.html')
