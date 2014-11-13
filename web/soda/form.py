from django import forms

class signup_form(forms.Form):
	first_name = forms.CharField(required=True, label='First Name', max_length=30)
	last_name = forms.CharField(required=True, label='Last Name', max_length=30)
	email = forms.EmailField(required=True, label='Email')
	password = forms.CharField(required=True, label='Password', max_length=30)

class signin_form(forms.Form):
	email = forms.EmailField(required=True, label='Email')
	password = forms.CharField(required=True, label='Password', max_length=30)

class profile_form(forms.Form):
	github_url = forms.CharField(required=True, label='github_url', max_length=50)
	linkedin_url = forms.CharField(required=True, label='linkedin_url', max_length=50)
	personal_site_url = forms.CharField(required=True, label='personal_site_url', max_length=50)
	phone = forms.CharField(required=True, label='phone #', max_length=50)
	college = forms.CharField(required=True, label='college', max_length=50)
	gpa = forms.CharField(required=True, label='gpa', max_length=10)
	address = forms.CharField(required=True, label='address', max_length=30)
	city = forms.CharField(required=True, label='city', max_length=30)
	zipcode = forms.CharField(required=True, label='zipcode', max_length=30)
	resume = forms.FileField(required=True, label='resume')

class emaillist_form(forms.Form):
	email = forms.CharField(required=True, label='email')
