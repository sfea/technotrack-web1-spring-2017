from django.shortcuts import render
from .models import Blog, Post
from comments.models import Comment
from django.views.generic import ListView, DetailView
from django import forms

class SortForm(forms.Form):

    sort = forms.CharField(required=True)
    rate = forms.IntegerField()


class BlogsList(ListView):

    queryset = Blog.objects.all()
    template_name = "posts/blogs.html"

    def get_context_data(self, **kwargs):
        context = super(BlogsList, self).get_context_data(**kwargs)
        context['sortform'] = SortForm()
        return context

    def get_queryset(self):
        sorting = self.request.GET.get('sort', 'title')
        if sorting not in ('title', 'rate', 'description'):
            sorting = 'title'
        qs = super(BlogsList, self).get_queryset()
        qs = qs.order_by(sorting)
        return qs


class BlogView(DetailView):

    queryset = Blog.objects.all()
    template_name = 'posts/blog.html'


class PostView(DetailView):

    queryset = Post.objects.all()
    template_name = 'posts/post.html'

    def get_context_data(self, **kwargs):
        context = super(BlogsList, self).get_context_data(**kwargs)
        sortform = SortForm(self.request.GET)
        context['sortform'] = SortForm()
        return context

    def get_queryset(self):
        qs = super(BlogsList, self).get_queryset()
        sortform = SortForm(self.request.GET)
        if sortform.is_valid():
            qs = qs.order_by(sortform.cleaned_data['sort'])
        return qs


def show_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'posts/blogs.html', {'blogs': blogs})


def show_blog(request, blog_id=None):
    blog = Blog.objects.get(id=blog_id)
    posts = Post.objects.filter(blog=blog)
    return render(request, 'posts/blog.html', {'blog':blog, 'posts':posts})


def show_post(request, blog_id=None, post_id=None):
    blog = Blog.objects.get(id=blog_id)
    post = Post.objects.filter(id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'posts/post.html', {'post':post, 'comments':comments, 'blog':blog})