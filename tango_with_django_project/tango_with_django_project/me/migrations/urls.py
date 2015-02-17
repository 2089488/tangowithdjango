from django.conf.urls import patterns, url
from me import views

urlpatterns = patterns('',
                       url(r'^$', views.info, name='info'),
                       url(r'name/', views.name, name='name'),
                       url(r'age/', views.age, name='age'),
                       )