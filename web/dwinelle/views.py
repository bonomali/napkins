from __future__ import division
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout as lgout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User as SysUser
import datetime
from dwinelle.user import *
from dwinelle.form import *

def fill(request):
	json = request.GET['user']
	user = JsonToUser(json)
	user.getResume()
	company_name = request.GET['company_name']
	form = form_dict[company_name]
	form_fill(user, form)
	user.deleteResume()
	return HttpResponse("lol")
