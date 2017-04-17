# -*- coding: utf-8 -*-
from django.conf.urls import url
from posts.views import BlogView, PostView, BlogsList, CreateBlog, UpdateBlog, CreatePost, UpdatePost, DeleteBlog, \
    DeletePost, PostLikeAjaxView, PostCommentsView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^blogs/$', BlogsList.as_view(), name="allblogs"),

    url(r'^blogs/(?P<pk>\d+)/$', BlogView.as_view(), name="blog"),
    url(r'^blogs/(?P<pk>\d+)/delete/$', DeleteBlog.as_view(), name="deleteblog"),
    url(r'^blogs/new_blog/$', login_required(CreateBlog.as_view()), name="createblog"),
    url(r'^blogs/(?P<pk>\d+)/edit/$', UpdateBlog.as_view(), name="editblog"),

    url(r'^posts/(?P<pk>\d+)/$', PostView.as_view(), name="post"),
    url(r'^posts/(?P<pk>\d+)/comments/$', PostCommentsView.as_view(), name="postcomments"),
    url(r'^posts/(?P<pk>\d+)/delete/$', DeletePost.as_view(), name="deletepost"),
    url(r'^(?P<pk>\d+)/posts/new_post/$', login_required(CreatePost.as_view()), name="createpost"),
    url(r'^posts/(?P<pk>\d+)/edit/$', login_required(UpdatePost.as_view()), name="editpost"),
    url(r'^posts/(?P<pk>\d+)/post_like/$', login_required(PostLikeAjaxView.as_view()), name="postlike"),
]