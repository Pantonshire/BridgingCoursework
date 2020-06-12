from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('posts', lambda request : views.post_list(request, 1), name='post_list_first'),
    path('posts/<int:page_no>', views.post_list, name='post_list'),
    path('compose', views.compose_post, name='compose_post'),
    path('post/<str:post_path>', views.post, name='post'),
    path('post/<str:post_path>/amend', views.amend_post, name='amend_post'),

    path('submit/post/compose', views.submit_compose_post, name='submit_compose_post'),
    path('submit/post/<str:post_path>/amend', views.submit_amend_post, name='submit_amend_post'),
]
