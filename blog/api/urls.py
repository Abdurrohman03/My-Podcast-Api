from django.urls import path
from .views import BlogListCreateAPIView, BlogRUDAPIView, CommentListCreateAPIView, CommentRUDAPIView


urlpatterns = [

    path('blog-list-create/', BlogListCreateAPIView.as_view()),
    path('blog-rud/<int:pk>/', BlogRUDAPIView.as_view()),

    path('comment/article/<int:article_id>/', CommentListCreateAPIView.as_view()),
    path('comment/<int:pk>/', CommentRUDAPIView.as_view()),

]
