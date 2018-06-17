from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SupervisorForm,DriverForm
from .models import Supervisor,Driver,Conductor
# Create your views here.


def home(request):
    return render(request, 'supervisor/dashboard/index.html')

def editSupervisor(request):
	'''
	Edit a created supervisor
	'''
	if request.method == 'POST':
		form = SupervisorForm(request.POST,instance = Supervisor.objects.get(id = request.user.supervisor.id))
		if form.is_valid():
			form.save()
			messages.success(request, f'Success! Your edit has been successful!')
			return redirect('sup:dashboard')


	else:
		form = SupervisorForm(instance = Supervisor.objects.get(id = request.user.supervisor.id))
		return render(request,'supervisor/dashboard/edit.html',{"form":form})


def createDriver(request):
	'''
	Create Driver crew member
	'''
	if request.Post == 'POST':
		form = DriverForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Success! Driver Crew member succesfully created!')
			return redirect('sup:dashboard')
	else:
		form = DriverForm()
		return render(request, 'supervisor/crew/createDriver.html')


def editDriver(request,driverId):
	'''
	Edit driver instance
	'''
	if request.Post == 'POST':
		form = DriverForm(request.POST,instance = Driver.objects.get(id = driverId))
		if form.is_valid():
			form.save()
			messages.success(request,'Success! Driver Crew member succesfully edited!')
			return redirect('sup:dashboard')
	else:
		form = DriverForm(instance = Driver.objects.get(id = driverId))
		return render(request, 'supervisor/crew/editDriver.html')
