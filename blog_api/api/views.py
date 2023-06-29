from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
