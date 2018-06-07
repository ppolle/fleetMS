from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class OwnerSignUpForm(UserCreationForm):
	'''
	Model form class to create a sign up form
	'''
	first_name = forms.CharField(max_length=30, required=False)
	last_name = forms.CharField(max_length=30, required=False)
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	national_id = forms.IntegerField()
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email','national_id', 'password1', 'password2', )
	def __init__(self,*args, **kwargs):
		super(OwnerSignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] ='form-control'
		self.fields['email'].widget.attrs['class'] ='form-control'
		self.fields['first_name'].widget.attrs['class'] ='form-control'
		self.fields['national_id'].widget.attrs['class'] ='form-control'
		self.fields['last_name'].widget.attrs['class'] ='form-control'
		self.fields['password1'].widget.attrs['class'] ='form-control'
		self.fields['password2'].widget.attrs['class'] ='form-control'
