from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=5000)
    links = models.CharField(max_length=100)

daily_allowed_apps = 5
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
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

class Profile(models.Model):
    github_url = models.CharField(max_length=50)
    linkedin_url = models.CharField(max_length=50)
    personal_site_url = models.CharField(max_length=50)

    phone = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    gpa = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)

    resume = models.FileField(("Resume"), upload_to=upload_resume_to, blank=True)

class Application(models.Model):
    user = models.ForeignKey('User', null=True, default=None)
    company = models.ForeignKey('Company', null=True, default=None)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, default="pending")
