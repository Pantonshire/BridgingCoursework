from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.post_list_first, name='blog_index'),

    #re_path(r'^.+/$', views.remove_trailing_slash),

    path('posts', views.post_list_first, name='post_list_first'),
    path('posts/<int:page_no>', views.post_list, name='post_list'),
    path('archive', views.post_archive, name='post_archive'),
    path('compose', views.compose_post, name='compose_post'),
    path('post/<str:post_path>', views.post, name='post'),
    path('post/<str:post_path>/amend', views.amend_post, name='amend_post'),

    path('submit/post/compose', views.submit_compose_post, name='submit_compose_post'),
    path('submit/post/<str:post_path>/amend', views.submit_amend_post, name='submit_amend_post'),
    path('submit/comment/<str:post_path>', views.submit_comment, name='submit_comment'),

    path('login', LoginView.as_view(template_name='blog/login.html'), name='login'),
]
