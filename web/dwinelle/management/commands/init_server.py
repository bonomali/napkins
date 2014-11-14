from django.core.management.base import BaseCommand, CommandError
from dwinelle.models import *
import sys

class Command(BaseCommand):
    def handle(self, *args, **options):
    	past_ips = Server.objects.all()
    	for past_ip in past_ips:
    		past_ip.delete()
    	ip = "http://127.0.0.1:8000/"
    	if len(sys.argv) > 2:
    		ip = sys.argv[2]
    	s = Server()
    	s.ip = ip
    	s.save()
