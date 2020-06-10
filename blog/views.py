from django.shortcuts import render
from . import models

def blog_index(request):
    return render(request, 'blog/index.html', {
        'posts': models.Post.objects.filter(published=True).order_by('-date'),
    })
