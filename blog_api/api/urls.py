from django.urls import path
from api.views import *


urlpatterns = [
    path('posts/', PostAPIList.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view()),
    path('addcomment/',
         CommentAddAPIView.as_view()),

]
