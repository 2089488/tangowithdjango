from django.conf.urls import patterns, url
from alphabet import views

urlpatterns = patterns('',
                       url(r'^$', views.abc, name='spelling'),
                       url(r'^reverse/', views.reverse, name='reverse_alphabet'))