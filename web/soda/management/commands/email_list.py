#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from soda.models import *
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        email_list = ""
        for user in users:
        	if "@" in user.email and "." in user.email:
        		email_list += user.email
        		email_list += ";"
        print email_list
