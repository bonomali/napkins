#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from soda.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        k = 0
        emaillists = EmailList.objects.all()
        for email in emaillists:
            if '@' in email.email:
                k += 1
        print k
