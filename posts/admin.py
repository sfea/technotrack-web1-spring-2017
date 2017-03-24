from django.contrib import admin
from .models import Blog
from .models import Post

admin.site.register(Blog)
admin.site.register(Post)