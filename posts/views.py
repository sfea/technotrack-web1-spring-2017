# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, resolve_url
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DeleteView
from django.views.generic import TemplateView

from posts.forms import SortForm, BlogForm
from .models import Blog, Post, Category, Like, Dislike
from comments.models import Comment
from django.views.generic import ListView, DetailView, UpdateView


class MainPage(TemplateView):

    template_name = 'posts/mainpage.html'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data()
        context['blog_quant'] = Blog.objects.all().count()
        context['post_quant'] = Post.objects.all().count()
        context['comment_quant'] = Comment.objects.all().count()
        return context


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
                self.sortform.cleaned_data['sort'] = 'updated_at'
            if self.sortform.cleaned_data['sort'] == 'updated_at':
                qs = qs.order_by(self.sortform.cleaned_data['sort']).reverse()
            else:
                qs = qs.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                qs = qs.filter(title__icontains=self.sortform.cleaned_data['search'])
        return qs


class BlogView(DetailView):

    queryset = Blog.objects.all()
    template_name = 'posts/blog.html'
    blogform = None


class CreateBlog(CreateView):

    template_name = "posts/addblog.html"
    model = Blog
    fields = ('category', 'title', 'description', 'rate')

    def get_success_url(self):
        return resolve_url('posts:blog', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateBlog, self).form_valid(form)


class DeleteBlog(DeleteView):
    template_name = "posts/blog_confirm_delete.html"
    model = Blog

    def get_success_url(self):
        return resolve_url('posts:allblogs')


class UpdateBlog(UpdateView):

    template_name = "posts/editblog.html"
    model = Blog
    fields = ('category', 'title', 'description', 'rate')

    def get_success_url(self):
        return resolve_url('posts:blog', pk=self.object.pk)

    def get_queryset(self):
        return super(UpdateBlog, self).get_queryset().filter(author=self.request.user)


class CreatePost(CreateView):

    template_name = "posts/addpost.html"
    model = Post
    fields = ('title', 'text', 'rate')

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.blogobject = get_object_or_404(Blog, id=pk)
        return super(CreatePost, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return resolve_url('posts:post', pk=self.object.id)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self.blogobject
        return super(CreatePost, self).form_valid(form)


class UpdatePost(UpdateView):

    template_name = "posts/editpost.html"
    model = Post
    fields = ('title', 'text', 'rate')

    def get_success_url(self):
        return resolve_url('posts:post', pk=self.object.pk)

    def get_queryset(self):
        return super(UpdatePost, self).get_queryset().filter(author=self.request.user)


class DeletePost(DeleteView):
    template_name = "posts/post_confirm_delete.html"
    model = Post

    def get_success_url(self):
        return resolve_url('posts:blog', pk=self.object.blog.id)


class UpdateComment(UpdateView):

    template_name = "posts/editcomment.html"
    model = Comment
    fields = ('comment', )

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.postobject = get_object_or_404(Post, id=pk)
        return super(UpdateComment, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return resolve_url('posts:post', pk=self.postobject.id)

    def get_queryset(self):
        return super(UpdateComment, self).get_queryset().filter(author=self.request.user)


class PostView(CreateView):

    model = Comment
    template_name = 'posts/post.html'
    fields = ('comment',)
    postobject = None

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.postobject = get_object_or_404(Post, id=pk)
        return super(PostView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['post'] = self.postobject
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.postobject
        return super(PostView, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('posts:post', pk=self.postobject.pk)


class PostLikeAjaxView(View):

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.postobject = get_object_or_404(Post, id=pk)
        return super(PostLikeAjaxView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        if not Like.objects.all().filter(post=self.postobject).filter(author=self.request.user).exists():
            new_like = Like()
            new_like.post = self.postobject
            new_like.author = self.request.user
            new_like.save()
        return HttpResponse(Like.objects.filter(post=self.postobject).count())


class PostDislikeAjaxView(View):

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.postobject = get_object_or_404(Post, id=pk)
        return super(PostDislikeAjaxView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        if not Dislike.objects.all().filter(post=self.postobject).filter(author=self.request.user).exists():
            new_dislike = Dislike()
            new_dislike.post = self.postobject
            new_dislike.author = self.request.user
            new_dislike.save()
        return HttpResponse(Dislike.objects.filter(post=self.postobject).count())


class PostCommentsView(DetailView):

    queryset = Post.objects.all()
    template_name = 'comments/comments_list.html'
