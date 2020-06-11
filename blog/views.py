from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound
from . import models, forms

def blog_index(request):
    return render(request, 'blog/index.html', {
        'posts': models.Post.objects.filter(published=True).order_by('-date')[:20],
    })

def post(request, post_path):
    requested_post = models.Post.objects.filter(published=True, path=post_path).first()
    if requested_post is None:
        return HttpResponseNotFound('Requested post not found')
    return render(request, 'blog/post.html', {
        'post': requested_post,
    })

def compose_post(request):
    return render(request, 'blog/compose_post.html', {
        'form': forms.ManagePostForm(),
    })

def amend_post(request, post_path):
    requested_post = models.Post.objects.filter(path=post_path).first()
    if requested_post is None:
        return HttpResponseNotFound('Requested post not found')
    return render(request, 'blog/amend_post.html', {
        'post': requested_post,
        'form': forms.ManagePostForm(initial={
            'title': requested_post.title,
            'content': requested_post.content,
            'published': requested_post.published,
        }),
    })

def submit_post(request):
    if request.method == "POST":
        form = forms.ManagePostForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest('Invalid form')
        post = form.save(commit=False)
        post.author = request.user
        post.update_path()
        post.update_time()
        post.save()
        return redirect('post', post_path=post.path)
    elif request.method == "PUT":
        #TODO
        pass
    else:
        return HttpResponseBadRequest('Bad method')
