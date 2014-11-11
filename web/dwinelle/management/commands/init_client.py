from django.core.management.base import BaseCommand, CommandError
from dwinelle.models import *
import sys

class Command(BaseCommand):
    def handle(self, *args, **options):
    	ip = "http://127.0.0.1:8001/"
    	if len(sys.argv) > 1:
    		ip = sys.argv[1]
    	client = Client(ip=ip)
    	client.save()
