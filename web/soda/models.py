from django.db import models
from storages.backends import s3boto

class Company(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=5000)
    img = models.CharField(max_length=500)
    links = models.CharField(max_length=500)

daily_allowed_apps = 5
class User(models.Model):
    fb_id = models.CharField(max_length=200, default=None)
    first_name = models.CharField(max_length=130)
    last_name = models.CharField(max_length=130)
    email = models.EmailField()
    password = models.CharField(max_length=130)
    num_apps_left_today = models.IntegerField(default=daily_allowed_apps)
    profile = models.ForeignKey('Profile', null=True, default=None)

def upload_resume_to(instance, filename):
    import os
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'profiles/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )

public_storage = s3boto.S3BotoStorage(
  querystring_expire=600000000,
)

class Profile(models.Model):
    github_url = models.CharField(max_length=250, default="")
    linkedin_url = models.CharField(max_length=250, default="")
    personal_site_url = models.CharField(max_length=250, default="")

    phone = models.CharField(max_length=50, default="")
    college = models.CharField(max_length=150, default="")
    gpa = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=230, default="")
    city = models.CharField(max_length=130, default="")
    state = models.CharField(max_length=130, default="")
    zipcode = models.CharField(max_length=130, default="")

    coverletter = models.CharField(max_length=15000, default="")
    resume = models.FileField(("Resume"), upload_to=upload_resume_to, blank=True, default=None, storage=public_storage)

class Application(models.Model):
    user = models.ForeignKey('User', null=True, default=None)
    company = models.ForeignKey('Company', null=True, default=None)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, default="pending")
