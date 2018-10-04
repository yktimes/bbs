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

from .utils.page import Pagination
def post_list(request):
    # 分页器

    data_list = Post.objects.all()
    current_page = int(request.GET.get("page",1)) # 当前页码
    data_count = Post.objects.all().count()    # 总页数
    base_path = request.path
    pagination = Pagination(current_page, data_count, base_path, request.GET, per_page_num=2, pager_count=8, )
    posts = data_list[pagination.start:pagination.end]
    print(pagination,posts)
    return render(request, 'post_list.html', {'posts':posts,'pagination':pagination})


def search(request):
    if request.method == 'POST':
        keyword = request.POST.get("keyword")
        posts = Post.objects.filter(content__contains=keyword)



    return render(request, 'search.html', {'posts':posts})
