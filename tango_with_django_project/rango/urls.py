from django.conf.urls import patterns, url,include
from rango import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^add_category/$', views.add_category, name='add_category'),
                       url(r'^add_profile/$', views.register_profile, name='add_profile'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/',
                           include(patterns('',
                                            url(r'^$', views.category, name='category'),
                                            url(r'^add_page/$', views.add_page, name='add_page'),
                                            ))),
                       url(r'^change/done', views.password_change_done, name='auth_password_change_done'),
                       url(r'^goto/$', views.track_url, name='goto'),
                       url(r'^like_category/$', views.like_category, name='like_category'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^profile/$', views.profile, name='profile'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^restricted/', views.restricted, name='restricted'),
                       # url(r'^search/$', views.search, name='search'),
                       url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
                       )
