# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import TemplateView

from .models import Blog, Post
from comments.models import Comment
from django.views.generic import ListView, DetailView, UpdateView
from django import forms

class MainPage(TemplateView):

    template_name = 'posts/mainpage.html'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data()
        context['blog_quant'] = Blog.objects.all().count()
        context['post_quant'] = Post.objects.all().count()
        return context


class SortForm(forms.Form):

    sort = forms.ChoiceField(
        choices=(
            ('title', u'Title'),
            ('rate', u'Rate'),
            ('description', u'Description'),
        ),
        required=False
    )
    search = forms.CharField(required=False)

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'description', 'rate')

class UpdateBlog(UpdateView):

    template_name = "posts/editblog.html"
    model = Blog
    fields = ('category', 'title', 'description')

    def get_success_url(self):
        return reverse('posts:allblogs')

    def get_queryset(self):
        return super(UpdateBlog, self).get_queryset().filter(author=self.request.user)


class UpdatePost(UpdateView):

    template_name = "posts/editpost.html"
    model = Post
    fields = ('title', 'text', 'rate')

    def get_success_url(self):
        return reverse('posts:allblogs')

    def get_queryset(self):
        return super(UpdatePost, self).get_queryset().filter(author=self.request.user)


class UpdateComment(UpdateView):

    template_name = "posts/editcomment.html"
    model = Comment
    fields = ('comment', )

    def get_success_url(self):
        return reverse('posts:allblogs')

    def get_queryset(self):
        return super(UpdateComment, self).get_queryset().filter(author=self.request.user)


class CreateBlog(CreateView):

    template_name = "posts/addblog.html"
    model = Blog
    fields = ('category', 'title', 'description')

    def get_success_url(self):
        return reverse('posts:allblogs')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(CreateBlog, self).form_valid(form)


class CreatePost(CreateView):

    template_name = "posts/addpost.html"
    model = Post
    fields = ('title', 'text', 'rate')
    def get_success_url(self):
        return reverse('posts:allblogs')

    def dispatch(self, request, blog_id=None, *args, **kwargs):
        self.blogobject = get_object_or_404(Blog, id=blog_id)
        return super(CreatePost, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self.blogobject
        form.instance.rate = 0
        return super(CreatePost, self).form_valid(form)


class CreateComment(CreateView):

    template_name = "posts/addcomment.html"
    model = Comment
    fields = ('comment',)

    def get_success_url(self):
        return reverse('posts:allblogs')

    def dispatch(self, request, post_id=None, *args, **kwargs):
        self.postobject = get_object_or_404(Post, id=post_id)
        return super(CreateComment, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.postobject
        return super(CreateComment, self).form_valid(form)


class BlogsList(ListView):

    queryset = Blog.objects.all()
    template_name = "posts/blogs.html"
    sortform = None

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortForm(self.request.GET)
        return super(BlogsList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogsList, self).get_context_data(**kwargs)
        context['sortform'] = self.sortform
        return context

    def get_queryset(self):
        qs = super(BlogsList, self).get_queryset()
        if self.sortform.is_valid():
            if self.sortform.cleaned_data['sort']:
                pass
            else:
                self.sortform.cleaned_data['sort'] = 'title'
            qs = qs.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                qs = qs.filter(title__icontains=self.sortform.cleaned_data['search'])
        return qs


class BlogView(DetailView):

    queryset = Blog.objects.all()
    template_name = 'posts/blog.html'


class PostView(DetailView):

    queryset = Post.objects.all()
    template_name = 'posts/post.html'