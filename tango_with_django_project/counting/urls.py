from django.conf.urls import patterns, url
from counting import views

urlpatterns = patterns('',
                       url(r'^$', views.about, name='about'),
                       url(r'^reverse', views.reverse, name='reverse'),
                       )
