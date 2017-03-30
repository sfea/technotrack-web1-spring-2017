# -*- coding: utf-8 -*-
from django.conf.urls import url
from posts.views import BlogView, PostView, BlogsList, CreateBlog, UpdateBlog, CreatePost, UpdatePost, CreateComment, \
    UpdateComment
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^blogs/$', BlogsList.as_view(), name="allblogs"),
    url(r'^blogs/new/$', login_required(CreateBlog.as_view()), name="createblog"),
    url(r'^blogs/(?P<pk>\d+)/$', BlogView.as_view(), name="blog"),
    url(r'^blogs/(?P<blog_id>\d+)/posts/new/$', login_required(CreatePost.as_view()), name="createpost"),
    url(r'^posts/(?P<pk>\d+)/edit/$', login_required(UpdatePost.as_view()), name="editpost"),
    url(r'^posts/(?P<pk>\d+)/$', PostView.as_view(), name="post"),
    url(r'^blogs/(?P<pk>\d+)/edit/$', UpdateBlog.as_view(), name="editblog"),
    url(r'^posts/(?P<post_id>\d+)/new_comment$', login_required(CreateComment.as_view()), name="addcomment"),
    url(r'^posts/(?P<post_id>\d+)/comment/(?P<pk>\d+)/edit$', UpdateComment.as_view(), name="editcomment"),
]