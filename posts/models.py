# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.timezone import now
from datetime import datetime
from django.db import models
from django.conf import settings

class Like(models.Model):
    post = models.ForeignKey('posts.Post')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)



class Category(models.Model):
    title = models.TextField(max_length=255)

    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    def __unicode__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    rate = models.IntegerField()
    blog = models.ForeignKey('posts.Blog')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)

    def __unicode__(self):
        return self.title