from django import forms
from .models import Supervisor, Driver,Conductor

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = ('id_number','mobile_phone_number','profile_picture')
        