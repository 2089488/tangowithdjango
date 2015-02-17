from django.conf.urls import patterns, url
from aboutme import views

urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       url(r'myname/', views.myname, name='my_name'),
                       url(r'myage/', views.myage, name='my_age'),)