from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('project.accounts.urls', namespace='accounts')),
    url(r'^timer/', include('project.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
)
