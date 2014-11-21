from __future__ import division
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout as lgout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User as SysUser
import datetime
import random
import requests
from multiprocessing.dummy import Pool
from soda.models import *
from soda.form import signup_form, signin_form, profile_form, coverletter_form
from dwinelle.user import *
from dwinelle.form import form_dict
from dwinelle.preview import *
from dwinelle.models import *
from soda.email import *

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
	user = User.objects.get(email=request.user)
	context = {}
	context['num_apps_left_today'] = user.num_apps_left_today
	context['companies'] = Company.objects.all()
	context['user'] = request.user
	return render(request, 'search.html', context)

@login_required(login_url='/signin/')
def company(request, company_id):
	context = {}
	context['company'] = Company.objects.filter(id=company_id)[0]
	return render(request, 'company.html', context)

@login_required(login_url='/signin/')
def company_preview(request, company_id):
	user = User.objects.get(email=request.user)
	if not user.profile:
		return HttpResponseRedirect("/profile")
	company = Company.objects.filter(id=company_id)[0]
	user = UserPlain(user)
	form = form_dict[company.name]
	fields = preview(user, form).iteritems()
	context = {'fields':fields, 'company':company}
	return render(request, 'preview.html', context)

@login_required(login_url='/signin/')
def apply(request, company_id):
	user = User.objects.get(email=request.user)
	company = Company.objects.filter(id=company_id)[0]
	if not user.profile or not user.profile.address:
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
		url = random.choice(Client.objects.all()).ip + "fill"
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

def feedback(request):
	context = {}
	return render(request, 'feedback.html', context)

@login_required(login_url='/signin/')
def profile(request):
	user = User.objects.get(email=request.user)
	if request.method == "GET":
		form = profile_form()
		if user.profile:
			form = profile_form({'github_url': user.profile.github_url, 'linkedin_url': user.profile.linkedin_url, 'personal_site_url':user.profile.personal_site_url, 'phone': user.profile.phone, 'college': user.profile.college, 'gpa': user.profile.gpa, 'address': user.profile.address, 'city': user.profile.city, 'zipcode': user.profile.zipcode,'state': user.profile.state,'resume': user.profile.resume})
		context = {'form' : form, 'has_coverletter':False}
		if user.profile and user.profile.coverletter:
			context['has_coverletter'] = True
		if user.profile and user.profile.resume:
			context['resume_url'] = user.profile.resume.url
		else:
			context['resume_url'] = None
		return render(request, 'profile.html', context)
	elif request.method == 'POST':
		github_url = request.POST['github_url']
		linkedin_url = request.POST['linkedin_url']
		personal_site_url = request.POST['personal_site_url']
		phone = request.POST['phone']
		college = request.POST['college']
		gpa = request.POST['gpa']
		address = request.POST['address']
		city = request.POST['city']
		state = request.POST['state']
		zipcode = request.POST['zipcode']
		has_resume = 'resume' in request.FILES.keys()
		if has_resume:
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
		profile.state = state
		profile.zipcode = zipcode
		if has_resume:
			profile.resume = resume
		profile.save()
		user.profile = profile
		user.save()
		return HttpResponseRedirect('/search/')


@login_required(login_url='/signin/')
def coverletter(request):
	user = User.objects.get(email=request.user)
	if request.method == "GET":
		if not user.profile:
			p = Profile()
			p.save()
			user.profile = p
			user.save()
		profile = user.profile
		form = coverletter_form()
		if user.profile.coverletter:
			form = coverletter_form({'coverletter': user.profile.coverletter})
		context = {'form' : form}
		return render(request, 'coverletter.html', context)
	elif request.method == "POST":
		coverletter = request.POST['coverletter']
		p = user.profile
		p.coverletter = coverletter
		p.save()
		return HttpResponseRedirect('/profile/')


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

def data(request):
	users = User.objects.all()
	profiles = Profile.objects.all()
	apps = Application.objects.all()
	context = {}
	context['user_len'] = len(users)
	context['profile_len'] = len(profiles)
	context['app_len'] = len(apps)
	return render(request, 'data.html', context)

def share(request, user_id):
	user = User.objects.get(id=user_id)
	user.num_apps_left_today += 2
	user.save()
	return HttpResponse("Ok!!")
