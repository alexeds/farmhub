from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/$', 'search', name="business.search"),
    url(r'^(?P<id>\d+)/$', 'detail', name="business.detail"),
)