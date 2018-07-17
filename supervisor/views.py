from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SupervisorForm,DriverForm,ConductorForm, IssueForm
from .models import Supervisor,Driver,Conductor,AssignCrew, Issue
from owner.models import Vehicle,Owner
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/loginViews/')
def home(request):
	'''
	this view shows the dashboard view
	'''
	matatus =  Vehicle.objects.filter(sacco = request.user.supervisor.sacco_base)
	owners = Owner.objects.filter(sacco = request.user.supervisor.sacco_base)
	return render(request, 'supervisor/dashboard/index.html',{"matatus":matatus,"owners":owners})

@login_required(login_url='/loginViews/')
def editSupervisor(request):
	'''
	Edit a created supervisor
	'''
	if request.method == 'POST':
		form = SupervisorForm(request.POST,request.FILES,instance = Supervisor.objects.get(id = request.user.supervisor.id))
		if form.is_valid():
			form.save()
			messages.success(request, f'Success! Your edit has been successful!')
			return redirect('sup:profile')
	
	else:
		form = SupervisorForm(instance = Supervisor.objects.get(id = request.user.supervisor.id))
		return render(request,'supervisor/dashboard/edit.html',{"form":form})

@login_required(login_url='/loginViews/')
def createDriver(request):
	'''
	Create Driver crew member
	'''
	if request.method == 'POST':
		form = DriverForm(request.POST)
		if form.is_valid():
			driver = form.save(commit = False)
			driver.sacco = request.user.supervisor.sacco_base
			driver.save()
			messages.success(request,'Success! Driver Crew member succesfully created!')
			return redirect('sup:allDrivers')
	else:
		form = DriverForm()
		return render(request, 'supervisor/crew/createDriver.html',{"form":form})

@login_required(login_url='/loginViews/')
def editDriver(request,driverId):
	'''
	Edit driver instance
	'''
	if request.method == 'POST':
		form = DriverForm(request.POST,instance = Driver.objects.get(id = driverId))
		if form.is_valid():
			form.save()
			messages.success(request,'Success! Driver Crew member succesfully edited!')
			return redirect('sup:allDrivers')
	else:
		form = DriverForm(instance = Driver.objects.get(id = driverId))
		driver = Driver.objects.get(pk = driverId)
		return render(request, 'supervisor/crew/editDriver.html',{"form":form,"driver":driver})

@login_required(login_url='/loginViews/')
def allDrivers(request):
	'''
	View all Driver instances
	'''
	drivers = Driver.objects.filter(sacco = request.user.supervisor.sacco_base)
	return render(request,'supervisor/crew/allDrivers.html',{"drivers":drivers})

@login_required(login_url='/loginViews/')
def deleteDriver(request,driverId):
	'''
	Delete a driver instance
	'''
	Driver.objects.filter(pk = driverId).delete()
	messages.info(request,'Succesfully delete a driver')
	return redirect('sup:allDrivers')

@login_required(login_url='/loginViews/')
def createConductor(request):
	'''
	Create conductor instance
	'''
	if request.method == 'POST':
		form = ConductorForm(request.POST)
		if form.is_valid():
			conductor = form.save(commit = False)
			conductor.sacco = request.user.supervisor.sacco_base
			conductor.save()
			messages.success(request,'Success! Created a conductor crew member')
			return redirect('sup:allConductors')

	else:
		form = ConductorForm()
		return render(request,'supervisor/crew/createConductor.html',{"form":form})

@login_required(login_url='/loginViews/')
def editConductor(request,conductorId):
	'''
	Edit conductor instance
	'''
	if request.method == 'POST':
		form = ConductorForm(request.POST,instance = Conductor.objects.get(pk = conductorId))
		if form.is_valid():
			form.save()
			messages.success(request,'Succesfully edited a conductor instance')
			return redirect('sup:allConductors')
	else:
		form = ConductorForm(instance = Conductor.objects.get(pk = conductorId))
		cond = Conductor.objects.get(pk = conductorId)
		return render(request,'supervisor/crew/editConductor.html',{"form":form,"cond":cond})

@login_required(login_url='/loginViews/')
def allConductors(request):
	'''
	View all conductor instances
	'''
	conductors = Conductor.objects.filter(sacco = request.user.supervisor.sacco_base)
	return render(request,'supervisor/crew/allConductors.html',{"conductors":conductors})

@login_required(login_url='/loginViews/')
def deleteConductor(request,conductorId):
	'''
	Delete a conductor instance
	'''
	Conductor.objects.filter(pk = conductorId).delete()
	messages.error(request,'Succesfully deleted a conductor')
	return redirect('sup:allConductors')

@login_required(login_url='/loginViews/')
def profile(request):
	'''
	This view will render a supervisor profile instance
	'''
	profile = Supervisor.objects.get(user = request.user)
	return render(request,'supervisor/dashboard/profile.html',{"profile":profile})

@login_required(login_url='/loginViews/')
def allMatatus(request):
	'''
	This view will retrieve instances of all matatus
	'''
	matatus = Vehicle.objects.filter(sacco = request.user.supervisor.sacco_base)
	return render(request,'supervisor/dashboard/allMatatus.html',{"matatus":matatus})

@login_required(login_url='/loginViews/')
def allOwners(request):
	'''
	This view will retrieve instances of all matatu owners
	'''
	owners = Owner.objects.filter(sacco = request.user.supervisor.sacco_base)
	return render(request,'supervisor/dashboard/allOwners.html',{"owners":owners})

@login_required(login_url='/loginViews/')
def singleMatatu(request,matId):
	'''
	This view will retrieve a single matatu instance
	'''
	drivers = Driver.objects.filter(sacco = request.user.supervisor.sacco_base)
	conductors = Conductor.objects.filter(sacco = request.user.supervisor.sacco_base)
	matatu = Vehicle.objects.get(id = matId)
	crew = AssignCrew.objects.filter(vehicle_id = matId)
	return render(request,'supervisor/dashboard/singleMatatu.html',{"matatu":matatu,"drivers":drivers,"conductors":conductors,"crew":crew})

@login_required(login_url='/loginViews/')
def assignCrew(request,matId):
	'''
	This view will create or update an instance of a matatu crew in the assign cre table
	'''
	if AssignCrew.objects.filter(vehicle_id = matId).exists():
		if request.GET.get("driver"):
			AssignCrew.objects.filter(vehicle_id = matId).update(driver_id = request.GET.get("driver"))
		if request.GET.get("conductor"):
			AssignCrew.objects.filter(vehicle_id = matId).update(conductor_id = request.GET.get("conductor"))

		if request.GET.get("is_active") == "True":
			Vehicle.objects.filter(id = matId).update(is_active = True)
		elif request.GET.get("is_active") == "False":
			Vehicle.objects.filter(id = matId).update(is_active = False)

		messages.success(request,f'You have succesfully assigned a crew to the vehicle')
		return redirect(request.META.get('HTTP_REFERER'))
		
	else:
		if request.GET.get("driver") and request.GET.get("conductor"):

			AssignCrew(driver_id = Driver.objects.get(id = request.GET.get("driver")), conductor_id = Conductor.objects.get(id = request.GET.get("conductor")),vehicle_id = Vehicle.objects.get(id = matId)).save()
			
			if request.GET.get("is_active") == "True":
				Vehicle.objects.filter(id = matId).update(is_active = True)
			elif request.GET.get("is_active") == "False":
				Vehicle.objects.filter(id = matId).update(is_active = False)

			messages.success(request,f'You have succesfully assigned a crew to the vehicle')
			return redirect(request.META.get('HTTP_REFERER'))
		else:
			messages.error(request, 'You have to select both the driver and conductor fields to succesfully assign a crew!')
			return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/loginViews/')
def deleteCrew(request,matId):
	'''
	This view will delete a crew instance in the assign crew table
	'''
	AssignCrew.objects.filter(vehicle_id = matId).delete()
	Vehicle.objects.filter(id = matId).update(is_active = False)
	messages.success(request,'You have succesfully deleted the crew from this matatu')
	return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/loginViews/')
def create_issue(request):
	form = IssueForm()
	all_issues = Issue.objects.all().order_by('-id')
	issues = all_issues.filter(supervisor_started=request.user.supervisor)
	if request.method == 'POST':
		form = IssueForm(request.POST)
		if form.is_valid():
			issue = form.save(commit=False)
			issue.supervisor_started = request.user.supervisor
			issue = issue.save()
	else:
		form = IssueForm()
	return render(request, 'supervisor/dashboard/issue.html', {'form' : form, 'issues':issues,})

def singleOwner(request,ownerId):
	'''
	This view will retrieve an owner instance
	'''
	owner = Owner.objects.get(id = ownerId)
	vehicles = Vehicle.objects.filter(owner = ownerId)
	return render(request,'supervisor/dashboard/singleOwner.html',{"owner":owner,"vehicles":vehicles})