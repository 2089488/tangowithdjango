from django import patterns, url

urlpatterns = patterns('',
                       url(r'info/', views.info, name='info'),
                       url(r'name/', views.name, name='name'),
                       url(r'age/', views.age, name='age'))