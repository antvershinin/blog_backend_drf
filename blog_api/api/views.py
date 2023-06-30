from rest_framework import generics, permissions
from .models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly
# Create your views here.


class PostAPIList(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailViewSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class PostAddAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostAddSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CommentAddAPIView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentAddSerializer
    permission_classes = (permissions.IsAuthenticated, )
