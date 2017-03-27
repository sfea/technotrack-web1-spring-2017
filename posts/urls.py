# -*- coding: utf-8 -*-
from django.conf.urls import url
from posts.views import BlogView, PostView, BlogsList, CreateBlog, UpdateBlog
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^blogs/$', BlogsList.as_view(), name="allblogs"),
    url(r'^blogs/new/$', login_required(CreateBlog.as_view()), name="createblog"),
    url(r'^blogs/(?P<pk>\d+)/$', BlogView.as_view(), name="blog"),
    url(r'^blogs/(?P<pk>\d+)/edit/$', login_required(UpdateBlog.as_view()), name="editblog"),
    url(r'^posts/(?P<pk>\d+)/$', PostView.as_view(), name="post"),
]