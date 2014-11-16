from django.core.management.base import BaseCommand, CommandError
from dwinelle.models import *
import sys

class Command(BaseCommand):
    def handle(self, *args, **options):
        past_ips = Client.objects.all()
        for past_ip in past_ips:
            past_ip.delete()
        ip = "http://127.0.0.1:8001/"
        if len(sys.argv) <= 2:
            c = Client()
            c.ip = ip
            c.save()
        else:
            for ip in sys.argv[2:]:
                c = Client()
                c.ip = ip
                c.save()
                print "added " + ip
