from django.shortcuts import render, redirect, HttpResponse
from .models import *


# Create your views here.

def create(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")

        # 过滤功能未加

        post = Post.objects.create(title=title, content=content)
        return redirect('/post/read/?post_id=%d' % post.id)
    return render(request, 'create.html')


def edit(request):
    post_id = int(request.GET.get("post_id"))
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")

        # 过滤功能未加

        post = Post.objects.filter(id=post_id)
        post.update(title=title,content=content)
        return redirect('/post/read/?post_id=%d' % post_id)
    else:

        post = Post.objects.get(id=post_id)
    return render(request, 'edit.html', {'post': post})


def read(request):
    post_id = int(request.GET.get("post_id"))
    post = Post.objects.get(id=post_id)

    return render(request, 'read.html', {'post': post})


def post_list(request):
    return render(request, 'post_list.html', {})


def search(request):
    if request.method == 'POST':
        keyword = request.POST.get("keyword")
        post = Post.objects.filter(title=keyword)
        print(post)


    return render(request, 'search.html', {'posts':post})
