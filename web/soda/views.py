from __future__ import division
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout as lgout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User as SysUser
from soda.models import *
from soda.form import signup_form, signin_form

def index(request):
	context = {}
	return render(request, 'index.html', context)

def search(request):
	context = {}
	context['companies'] = Company.objects.all()
	return render(request, 'search.html', context)

def company(request, company_id=None):
	context = {}
	context['company'] = Company.objects.filter(id=company_id)[0]
	return render(request, 'company.html', context)

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
			return HttpResponseRedirect('/search')
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

def profile(request):
	context = {}
	return render(request, 'profile.html', context)


