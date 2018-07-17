from django import forms
from sacco.models import Sacco, Super_list

class SaccoForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the name of the sacco")
    registration_no = forms.CharField(help_text="Enter the registration number for your sacco")
    office_location = forms.CharField(help_text="Please enter a detail description of whwre your offices are located")
    office_telephone = forms.CharField(help_text="Please enter the telephone contacts for the sacco")
    office_email = forms.EmailField(help_text="Please enter the sacco's official email address")
    
    details = forms.CharField(help_text="Please enter all relevant details for your sacco(Eg. The routes and route number)")

    class Meta:
        model = Sacco
        fields = ('name', 'registration_no',
                  'office_location', 'office_telephone', 'office_email', 'details')

class Super_listForm(forms.ModelForm):
    class Meta:
        model = Super_list
        fields = ('full_name', 'id_number')


class EditProfile(forms.ModelForm):
    class Meta:
        model = Sacco
        fields = ('name', 'registration_no', 'office_location', 'office_telephone', 'office_email', 'details')


class EditSupervisor(forms.ModelForm):
    class Meta:
        model = Super_list
        fields = ('full_name', 'id_number')
