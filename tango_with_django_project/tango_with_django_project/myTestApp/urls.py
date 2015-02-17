from django.conf.urls import patterns, url
from myTestApp import views

urlpatterns = patterns('',
                       url(r'^$', views.about, name='about'))
