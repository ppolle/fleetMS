from django import forms
from owner.models import Owner, Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('number_plate', 'capacity')


class EditProfile(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ( 'nat_id', 'telephone')


   
