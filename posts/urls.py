# -*- coding: utf-8 -*-
from django.conf.urls import url
from posts.views import show_blogs, show_blog, show_post

urlpatterns = [
    url(r'^$', show_blogs, name="allblogs"),
    url(r'^(?P<blog_id>\d+)/$', show_blog, name="blog"),
    url(r'^(?P<blog_id>\d+)/(?P<post_id>\d+)/$', show_post, name="post")
]