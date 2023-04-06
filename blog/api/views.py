from django.db.models import Q
from rest_framework import generics, permissions
from ..models import Blog, CommentBlog
from .serializers import BlogGETSerializer, BlogPOSTSerializer, CommentGETSerializer, CommentPOSTSerializer
from .permissions import IsOwnerOrReadOnly


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BlogGETSerializer
        return BlogPOSTSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')
        q_condition = Q()
        if q:
            q_condition = Q(title__icontains=q)
        q_category = Q()
        if cat:
            q_category = Q(category__title__exact=cat)
        q_tag = Q()
        if tag:
            q_tag = Q(tags__title__exact=tag)
        qs = qs.filter(q_condition, q_category, q_tag)
        return qs


class BlogRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BlogGETSerializer
        return BlogPOSTSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = CommentBlog.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentGETSerializer
        return CommentPOSTSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            qs = qs.filter(article_id=article_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx


class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentBlog.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentGETSerializer
        return CommentPOSTSerializer

