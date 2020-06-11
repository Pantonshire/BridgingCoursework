from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('post/compose', views.compose_post, name='compose_post'),
    path('post/<str:post_path>', views.post, name='post'),
    path('post/<str:post_path>/amend', views.amend_post, name='amend_post'),

    path('submit/post', views.submit_post, name='submit_post'),
]
