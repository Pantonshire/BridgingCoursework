from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('post/<str:post_path>', views.post, name='post'),
]
