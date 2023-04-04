from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, reverse, get_object_or_404
from episode.models import Category, Tag
from .forms import CommentFormBlog
from .models import Blog


def blog_list(request):
    blogs = Blog.objects.order_by('-id')
    category_list = Category.objects.all()
    tags = Tag.objects.all()
    search = request.GET.get('search')
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    if search:
        blogs = blogs.filter(title__icontains=search)
    if tag:
        blogs = blogs.filter(tags__title__exact=tag)
    if cat:
        blogs = blogs.filter(category__title__exact=cat)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(blogs, 2)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        'object_list': page_obj,
        'category_list': category_list,
        'tags': tags,
    }
    return render(request, 'podcast/blog.html', ctx)


def blog_detail_views(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    blog.views += 1
    blog.save()
    return redirect(reverse('blog:blog_detail', kwargs={'pk': pk}))


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    category_list = Category.objects.all()
    tags = Tag.objects.all()
    form = CommentFormBlog()
    if request.method == 'POST':
        form = CommentFormBlog(request.POST)
        if not request.user.is_authenticated:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.article_id = blog.id
                obj.save()
                return redirect('.')
        else:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.author_id = request.user.profile.id
                obj.name = request.user.profile.full_name
                obj.article_id = blog.id
                obj.save()
                return redirect('.')
    ctx = {
        'object': blog,
        'form': form,
        'category_list': category_list,
        'tags': tags,
    }
    return render(request, 'podcast/blog_detail.html', ctx)

