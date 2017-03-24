from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Comment(models.Model):
    comment = models.TextField(max_length=255)
    post = models.ForeignKey('posts.Post')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)