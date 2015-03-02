from django.conf.urls import patterns, url,include
from rango import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^add_category/$', views.add_category, name='add_category'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/',
                           include(patterns('',
                                            url(r'^$', views.category, name='category'),
                                            url(r'^add_page/$', views.add_page, name='add_page'),
                                            ))),
                       # url(r'^register/$', views.register, name='register'),
                       # url(r'^login/$', views.user_login, name='login'),
                       url(r'^password/change/done/$', views.password_change_done, name='auth_password_change_done'),
                       url(r'^restricted/', views.restricted, name='restricted'),
                       # url(r'^logout/$', views.user_logout, name='logout'),
                       )
