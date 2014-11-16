#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from soda.models import *
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
    	f = open('user_dump.txt')
    	lines = f.readlines()[0]
    	users = json.loads(lines)
    	for user in users:
    		exist = User.objects.filter(email=user['email'])
    		if not exist:
    			u = User(first_name=user['first_name'], last_name=user['last_name'], email=user['email'], password=user['password'])
    			u.save()
