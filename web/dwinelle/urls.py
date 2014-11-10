from django.conf.urls import patterns, url
from dwinelle import views

urlpatterns = patterns('',
    # url(r'^$', views.index, name="home"),
    url(r'^fill/$', views.fill, name="fill"),
)