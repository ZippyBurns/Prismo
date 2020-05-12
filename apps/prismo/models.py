from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    image = models.ImageField(upload_to='profile_image', blank=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Status(models.Model):
    status = models.TextField()
    likes = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_post = models.ForeignKey(
        User,
        related_name="user_posts",
        on_delete = models.CASCADE
      )

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status,
        related_name="posts",
        on_delete=models.CASCADE
    )
    user_comment = models.ForeignKey(
        User,
        related_name="user_comments",
        on_delete = models.CASCADE
    )