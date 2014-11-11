from django.db import models

class Client(models.Model):
    ip = models.CharField(max_length=30, default="http://127.0.0.1:8001/")
