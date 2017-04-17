from __future__ import unicode_literals

from django.utils.timezone import now
from datetime import datetime, timedelta
from django.conf import settings
from django.db import models


class Comment(models.Model):
    comment = models.TextField(max_length=255)
    post = models.ForeignKey('posts.Post')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created_at',)

    def __unicode__(self):
        return self.comment