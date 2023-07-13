from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment on post #{self.post.id}'
