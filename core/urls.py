from django.conf.urls import url, include
from core.views import test

urlpatterns = [
    url(r'^$', test),
    url(r'^(?P<blog_id>\d+)/$', test),
    url(r'^(?P<post_id>\d+)/(?P<blog_id>\d+)/$', test),
]