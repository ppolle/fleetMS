from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import get_user_model
from sacco.models import Sacco



class OwnerSignUpForm(UserCreationForm):
	'''
	Model form class to create a sign up form
	'''
	first_name = forms.CharField(max_length=30, required=False)
	last_name = forms.CharField(max_length=30, required=False)
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	national_id = forms.IntegerField()
	sacco =forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset = Sacco.objects.all(),required= False)
	
	class Meta:
		model = get_user_model()
		fields = ('username', 'first_name', 'last_name', 'email','national_id','sacco', 'password1', 'password2', )

	def __init__(self,*args, **kwargs):
		super(OwnerSignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] ='form-control'
		self.fields['email'].widget.attrs['class'] ='form-control'
		self.fields['first_name'].widget.attrs['class'] ='form-control'
		self.fields['national_id'].widget.attrs['class'] ='form-control'
		self.fields['last_name'].widget.attrs['class'] ='form-control'
		self.fields['password1'].widget.attrs['class'] ='form-control'
		self.fields['password2'].widget.attrs['class'] ='form-control'

class SaccoSignUpForm(UserCreationForm):
	'''
	Form class to create a sacco signup form
	'''
	name = forms.CharField(max_length = 100, required = True,widget=forms.TextInput(attrs={'class':'form-control'}))
	registration_no = forms.CharField(max_length = 100,required = True,widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = get_user_model()
		fields = ('name','username','registration_no','email','password1','password2',)
	
	def __init__(self,*args, **kwargs):
		super(SaccoSignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] ='form-control'
		self.fields['email'].widget.attrs['class'] ='form-control'
		self.fields['password1'].widget.attrs['class'] ='form-control'
		self.fields['password2'].widget.attrs['class'] ='form-control'	
	
class SupervisorSignupForm(UserCreationForm):
	'''
	Form class to create a supervisor signup form
	'''
	id_number = forms.IntegerField()
	
	
	class Meta:
		model = get_user_model()
		fields = ('username','first_name','last_name','id_number','email','password1','password2',)

	def __init__(self,*args, **kwargs):
		super(SupervisorSignupForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] ='form-control'
		self.fields['first_name'].widget.attrs['class'] ='form-control'
		self.fields['last_name'].widget.attrs['class'] ='form-control'
		self.fields['id_number'].widget.attrs['class'] ='form-control'
		self.fields['email'].widget.attrs['class'] ='form-control'
		self.fields['password1'].widget.attrs['class'] ='form-control'
		self.fields['password2'].widget.attrs['class'] ='form-control'	