from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
<<<<<<< HEAD
    url(r'^aboutme/', include('aboutme.urls')),
=======
>>>>>>> master
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
<<<<<<< HEAD
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
=======
        (r'media/(?P<path>.*)',
        'serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
>>>>>>> master
