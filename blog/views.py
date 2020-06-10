from django.shortcuts import render
from django.http import Http404
from . import models

def blog_index(request):
    return render(request, 'blog/index.html', {
        'posts': models.Post.objects.filter(published=True).order_by('-date')[:20],
    })

def post(request, post_path):
    requested_post = models.Post.objects.filter(published=True, path=post_path).first()
    if requested_post is None:
        raise Http404('Requested post not found')
    return render(request, 'blog/post.html', {
        'post': requested_post,
    })
