#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from soda.models import *
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        user_list = []
        for user in users:
            user_dict = {'first_name':user.first_name, 'last_name':user.last_name, 'email':user.email, 'password': user.password}
            user_list += [user_dict]
        f = open('user_dump.txt','wb')
        f.write(json.dumps(user_list))

