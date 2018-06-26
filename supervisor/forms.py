from django import forms
from .models import Supervisor,Driver,Conductor
from django.conf import settings
from django.contrib.auth import get_user_model

# user = get_user_model().objects.filter(is_authenticated = True)

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = ('id_number','mobile_phone_number','profile_picture')

class DriverForm(forms.ModelForm):
	class Meta:
		model = Driver
		fields = ('fullname','id_number','profile_picture')

class ConductorForm(forms.ModelForm):
	class Meta:
		model = Conductor
		fields = ('fullname','id_number','profile_picture')

class AssignCrewForm(forms.Form):
	conductor = forms.ModelChoiceField(widget=forms.Select(
		attrs={'class': 'form-control'}),queryset = Conductor.objects.filter(sacco = 2),required= False)