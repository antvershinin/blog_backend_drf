from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE)


class Comments(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
