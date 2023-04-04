from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import CommentForm
from .models import Podcast, Category, Tag, Like


def index(request):
    audio = Podcast.objects.get(id=1)
    audios = Podcast.objects.order_by('-id')
    podcasts_4 = Podcast.objects.all()[:4]
    try:
        user_id = request.user.profile.id
    except:
        user_id = None
    my_liked_musics = Like.objects.filter(author_id=user_id).values_list('music_id')
    my_liked_musics_list = [i[0] for i in my_liked_musics]
    ctx = {
        'audio': audio,
        'object_list': audios,
        '4_podcasts': podcasts_4,
        'my_liked_musics_list': my_liked_musics_list,
    }
    return render(request, 'podcast/index.html', ctx)


def episodes(request):
    audios = Podcast.objects.order_by('-id')
    category_list = Category.objects.all()
    tags = Tag.objects.all()
    search = request.GET.get('search')
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    if search:
        audios = audios.filter(title__icontains=search)
    if tag:
        audios = audios.filter(tags__title__exact=tag)
    if cat:
        audios = audios.filter(category__title__exact=cat)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(audios, 2)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    try:
        user_id = request.user.profile.id
    except:
        user_id = None
    my_liked_musics = Like.objects.filter(author_id=user_id).values_list('music_id')
    my_liked_musics_list = [i[0] for i in my_liked_musics]
    ctx = {
        'object_list': page_obj,
        'category_list': category_list,
        'tags': tags,
        'my_liked_musics_list': my_liked_musics_list,
    }
    return render(request, 'podcast/episodes.html', ctx)


def episode_views(request, pk):
    audio = get_object_or_404(Podcast, id=pk)
    audio.views += 1
    audio.save()
    return redirect(reverse('episode:episode_views', kwargs={'pk': pk}))


def episode(request, pk):
    audio = get_object_or_404(Podcast, id=pk)
    form = CommentForm()
    category_list = Category.objects.all()
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if not request.user.is_authenticated:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.article_id = audio.id
                obj.save()
                return redirect('.')
        else:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.author_id = request.user.profile.id
                obj.name = request.user.profile.full_name
                obj.article_id = audio.id
                obj.save()
                return redirect('.')
    try:
        user_id = request.user.profile.id
    except:
        user_id = None
    my_liked_musics = Like.objects.filter(author_id=user_id).values_list('music_id')
    my_liked_musics_list = [i[0] for i in my_liked_musics]
    ctx = {
        'object': audio,
        'form': form,
        'category_list': category_list,
        'tags': tags,
        'my_liked_musics_list': my_liked_musics_list,
    }
    return render(request, 'podcast/episode.html', ctx)


def get_ids_list(request):
    musics = Podcast.objects.order_by('-id')
    ids_list = [i.id for i in musics]
    return JsonResponse({'ids_list': ids_list})


@csrf_exempt
def like(request):
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "You should authorize"}, status=401)
    if request.method == "POST":
        music_id = int(request.POST.get('music_id'))
        user_id = request.user.profile.id
        likes = Like.objects.values_list('music_id', 'author_id')
        if (music_id, user_id) in likes:
            Like.objects.get(music_id=music_id, author_id=user_id).delete()
            return JsonResponse({'detail': "Un-Liked"})
        Like.objects.create(music_id=music_id, author_id=user_id)
        return JsonResponse({'detail': 'Liked'})
    return JsonResponse({'detail': 'Method Not allowed'}, status=405)


