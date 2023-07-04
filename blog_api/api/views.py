from rest_framework import generics, permissions
from .models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
# Create your views here.


class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailViewSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]


class CommentAddAPIView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentAddSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    permission_classes = [permissions.IsAuthenticated]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
