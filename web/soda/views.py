from __future__ import division
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout as lgout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User as SysUser
import datetime
from soda.models import *
from soda.form import signup_form, signin_form, profile_form, emaillist_form
from soda.email import company_app_data_email

def index(request):
	context = {}
	return render(request, 'index.html', context)

def search(request):
	context = {}
	context['companies'] = Company.objects.all()
	form = emaillist_form()
	context['form'] = form
	return render(request, 'search.html', context)

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
	# import requests
	# from multiprocessing.dummy import Pool
	# pool = Pool(processes=1)
	# def ok():
	# 	url = 'http://127.0.0.1:8000/fill'
	# 	param = {'user':":LASDASDAS"}
	# 	r = requests.get(url, params=param)
	# pool.apply_async(ok)
	return HttpResponse("LOL, so we didnt do this part.")

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
	return HttpResponseRedirect('/search/')

@login_required(login_url='/signin/')
def profile(request):
	user = User.objects.get(email=request.user)
	if request.method == "GET":
		form = profile_form()
		if user.profile:
			form = profile_form({'github_url': user.profile.github_url, 'linkedin_url': user.profile.linkedin_url, 'personal_site_url':user.profile.personal_site_url, 'phone': user.profile.phone, 'college': user.profile.college, 'gpa': user.profile.gpa, 'resume': user.profile.resume})
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
		user.save()
		print user.profile
		print not user.profile
		return HttpResponseRedirect('/search/')

def emaillist(request):
	if request.method == 'POST':
		email = request.POST['email']
		emailMem = EmailList(email=email)
		emailMem.save()
		company_app_data_email(email)
		return HttpResponse("We hv sent the list! Happy job surfing!")
