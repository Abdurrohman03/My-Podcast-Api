from django.urls import path
from .views import CommentRUDAPIView, CommentListCreateAPIView, PodcastListCreateAPIView, CategoryListCreateAPIView, \
    TagListCreateAPIView, TagRUDAPIView, CategoryRUDAPIView, PodcastRUDAPIView, SeasonListAPIView, LikeListAPIView, \
    LikePOSTAPIView

urlpatterns = [
    # tag
    path('tag-list-create/', TagListCreateAPIView.as_view()),
    path('tag-rud/<int:pk>/', TagRUDAPIView.as_view()),

    # category
    path('category-list-create/', CategoryListCreateAPIView.as_view()),
    path('category-rud/<int:pk>/', CategoryRUDAPIView.as_view()),

    # podcast
    path('episode-list-create/', PodcastListCreateAPIView.as_view()),
    path('episode-rud/<int:pk>/', PodcastRUDAPIView.as_view()),

    # comment
    path('comment-list-create/<int:episode_id>/', CommentListCreateAPIView.as_view()),
    path('comment-rud/<int:pk>/', CommentRUDAPIView.as_view()),

    # season
    path('season-list/<int:season_id>/', SeasonListAPIView.as_view()),

    # like
    path('like-list/', LikeListAPIView.as_view()),
    path('like/<int:music_id>/', LikePOSTAPIView.as_view()),
]
