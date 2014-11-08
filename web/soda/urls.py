from django.conf.urls import patterns, url
from soda import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="home"),
    url(r'^search/$', views.search, name="search"),
    url(r'^company/(?P<company_id>[-\w]+)/$', views.company, name="company"),
    url(r'^profile/$', views.profile, name="profile"),
	url(r'^signup/$', views.signup, name="signup"),
	url(r'^signin/$', views.signin, name="signin"),
    # url(r'^logout/$', views.logout, name="logout"),
    # url(r'^plan/$', views.plan, name="plan"),
)