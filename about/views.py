from django.shortcuts import render, redirect
from contact.forms import NewsletterForm
from blog.models import Blog
from episode.models import Podcast, Like


def index(request):
    form = NewsletterForm(request.POST or None)
    blogs = Blog.objects.all().count()
    podcasts = Podcast.objects.all().count()
    likes = Like.objects.all().count()
    views = 0
    for i in Podcast.objects.all():
        views += i.views
    for i in Blog.objects.all():
        views += i.views
    if form.is_valid():
        form.save()
        return redirect('.')
    ctx = {
        'form1': form,
        'blogs': blogs,
        'podcasts': podcasts,
        'likes': likes,
        'views': views,
    }
    return render(request, 'podcast/about.html', ctx)
