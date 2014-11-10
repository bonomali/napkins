from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('soda.urls')),
    url(r'^', include('dwinelle.urls')),
)
