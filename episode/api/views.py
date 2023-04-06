from rest_framework import generics, permissions

from ..models import Tag, Category, Podcast, Comment, Like, PlaylistBase, PlaylistSingle, Season
from .serializers import TagSerializer, CategorySerializer, PodcastGETSerializer, PodcastPOSTSerializer, \
    ComentGETSerializer, ComentPOSTSerializer, LikeGETSerializer, PlaylistSerializer, SeasonSerializer, \
    PlaylistSingleSerializer, LikePOSTSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminUserOrReadOnly


class TagListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/episode/tag-list-create/
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class TagRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/episode/tag-rud/<int:pk>/
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/episode/category-list-create/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CategoryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/episode/category-rud/<int:pk>/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class PodcastListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/episode/episode-list-create/
    queryset = Podcast.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PodcastGETSerializer
        return PodcastPOSTSerializer


class PodcastRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/episode/episode-rud/<int:pk>/
    queryset = Podcast.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PodcastGETSerializer
        return PodcastPOSTSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/episode/comment-list-create/<int:article_id>/
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ComentGETSerializer
        return ComentPOSTSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        episode_id = self.kwargs.get('episode_id')
        if episode_id:
            qs = qs.filter(article_id=episode_id)
            return qs
        return qs

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['episode_id'] = self.kwargs.get('episode_id')
        return ctx


class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/episode/comment-rud/<int:pk>/
    queryset = Comment.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ComentGETSerializer
        return ComentPOSTSerializer


class SeasonListAPIView(generics.ListAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastGETSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        season_id = self.kwargs.get('season_id')
        if season_id:
            qs = qs.filter(season_id=season_id)
            return qs
        return qs


class LikeListAPIView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeGETSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        author = self.request.user.profile
        if author:
            qs = qs.filter(author=author)
            return qs
        return qs


class LikePOSTAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePOSTSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['music_id'] = self.kwargs.get('music_id')
        return ctx


class LikeDELETEAPIView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikePOSTSerializer
    permission_classes = [permissions.IsAuthenticated]



