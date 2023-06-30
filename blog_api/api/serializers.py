from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Comments
        fields = ['author', 'text']


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Post
        fields = ['title', 'text', 'author']


class PostAddSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ['title', 'text', 'author']


class PostDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author']


class PostDetailViewSerializer(serializers.ModelSerializer):
    comments_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['author', 'text', 'comments_set']


class CommentAddSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comments
        fields = '__all__'
