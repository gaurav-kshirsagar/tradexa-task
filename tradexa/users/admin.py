from django.contrib import admin

# Register your models here.
from .models import PostUser, Post

admin.site.register(Post)
admin.site.register(PostUser)