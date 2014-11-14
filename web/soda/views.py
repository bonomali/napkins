from __future__ import division
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout as lgout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User as SysUser
import datetime
import requests
from multiprocessing.dummy import Pool
from soda.models import *
from soda.form import signup_form, signin_form, profile_form, emaillist_form
from soda.email import company_app_data_email
from dwinelle.user import *
from dwinelle.models import *

def index(request):
	user = User.objects.filter(email=request.user)
	if user:
		return HttpResponseRedirect("/search/")
	context = {}
	return render(request, 'index.html', context)

def about(request):
	context = {}
	return render(request, 'about.html', context)

@login_required(login_url='/signin/')
def search(request):
	context = {}
	context['companies'] = Company.objects.all()
	form = emaillist_form()
	context['form'] = form
	context['user'] = request.user
	return render(request, 'search.html', context)

@login_required(login_url='/signin/')
def company(request, company_id):
	context = {}
	context['company'] = Company.objects.filter(id=company_id)[0]
	return render(request, 'company.html', context)

@login_required(login_url='/signin/')
def apply(request, company_id):
	user = User.objects.get(email=request.user)
	company = Company.objects.filter(id=company_id)[0]
	if not user.profile:
		return HttpResponseRedirect('/profile/')
	if user.num_apps_left_today == 0:
		context = {}
		context['message'] = 'Sorry, you have exceeded max number of apps available per day. We are forced to have a cap because of limited server capabilities.'
		return render(request, 'thankyou.html', context)
	app = Application(user=user, company=company)
	app.save()
	user.num_apps_left_today -= 1
	user.save()
	pool = Pool(processes=1)
	def fill():
		url = Client.objects.all()[0].ip + "fill"
		user_json = UserToJson(UserPlain(user))
		param = {'user':user_json, 'company_name':company.name, 'app_id':app.id}
		r = requests.get(url, params=param)
	pool.apply_async(fill)
	context = {}
	context['message'] = 'Thanks for applying. Our automated system will be filling out your app in the next 10 mins. Check your email for confirmation.'
	return render(request, 'thankyou.html', context)

def signup(request):
	if request.method == 'GET':
		if request.user.is_authenticated():
			return HttpResponseRedirect('/search/')
		form = signup_form()
		context = {'form':form}
		return render(request, 'signup.html', context)
	elif request.method == 'POST':
		form = signup_form(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			system_user = SysUser.objects.create_user(email, email, password)
			system_user.is_active = True
			system_user.save()
			our_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
			our_user.save()
			return HttpResponseRedirect('/signin')
        return HttpResponseRedirect('/signup')

def signin(request):
	if request.method == 'GET':
		if request.user.is_authenticated():
			return HttpResponseRedirect('/search/')
		form = signin_form()
		context = {'form':form}
		return render(request, 'signin.html', context)
	elif request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = auth.authenticate(username=email, password=password)
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/search/')
		return HttpResponseRedirect('/signin/')

def logout(request):
	lgout(request)
	return HttpResponseRedirect('/')

@login_required(login_url='/signin/')
def profile(request):
	user = User.objects.get(email=request.user)
	if request.method == "GET":
		form = profile_form()
		if user.profile:
			form = profile_form({'github_url': user.profile.github_url, 'linkedin_url': user.profile.linkedin_url, 'personal_site_url':user.profile.personal_site_url, 'phone': user.profile.phone, 'college': user.profile.college, 'gpa': user.profile.gpa, 'address': user.profile.address, 'city': user.profile.city, 'zipcode': user.profile.zipcode,'resume': user.profile.resume})
		context = {'form' : form}
		return render(request, 'profile.html', context)
	elif request.method == 'POST':
		form = profile_form(request.POST)
		github_url = request.POST['github_url']
		linkedin_url = request.POST['linkedin_url']
		personal_site_url = request.POST['personal_site_url']
		phone = request.POST['phone']
		college = request.POST['college']
		gpa = request.POST['gpa']
		address = request.POST['address']
		city = request.POST['city']
		zipcode = request.POST['zipcode']
		resume = request.FILES['resume']
		profile = Profile()
		if user.profile:
			profile = user.profile
		else:
			user.profile = profile
		profile.linkedin_url = linkedin_url
		profile.github_url = github_url
		profile.personal_site_url = personal_site_url
		profile.phone = phone
		profile.college = college
		profile.gpa = gpa
		profile.address = address
		profile.city = city
		profile.zipcode = zipcode
		profile.resume = resume
		profile.save()
		user.profile = profile
		user.save()
		return HttpResponseRedirect('/search/')

@login_required(login_url='/signin/')
def history(request):
	user = User.objects.get(email=request.user)
	apps = Application.objects.filter(user=user).order_by('-date')
	context = {}
	context['apps'] = apps
	return render(request, 'history.html', context)

def confirm_app(request):
	app_id = request.GET['app_id']
	app = Application.objects.filter(id=app_id)[0]
	app.status = request.GET['status']
	app.save()
	return HttpResponse("yay")
