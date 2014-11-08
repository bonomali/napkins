from django import forms

class signup_form(forms.Form):
	first_name = forms.CharField(required=True, label='First Name', max_length=30)
	last_name = forms.CharField(required=True, label='Last Name', max_length=30)
	email = forms.EmailField(required=True, label='Email')
	password = forms.CharField(required=True, label='Password', max_length=30)

class signin_form(forms.Form):
	email = forms.EmailField(required=True, label='Email')
	password = forms.CharField(required=True, label='Password', max_length=30)
