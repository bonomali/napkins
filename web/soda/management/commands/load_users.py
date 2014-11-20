#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from soda.models import *
import json
from django.contrib.auth.models import User as SysUser


class Command(BaseCommand):
    def handle(self, *args, **options):
		f = open('user_dump.txt')
		lines = f.readlines()[0]
		users = json.loads(lines)
		for user in users:
			exist = User.objects.filter(email=user['email'])
			if not exist:
				system_user = SysUser.objects.create_user(user['email'], user['email'], user['password'])
				system_user.is_active = True
				system_user.save()
				u = User(first_name=user['first_name'], last_name=user['last_name'], email=user['email'], password=user['password'])
				u.save()
