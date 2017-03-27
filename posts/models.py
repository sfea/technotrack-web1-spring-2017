# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings

class Category(models.Model):
    title = models.CharField(max_length=255)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    rate = models.IntegerField()
    blog = models.ForeignKey('posts.Blog', default='')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)