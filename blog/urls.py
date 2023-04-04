from django.urls import path
from .views import blog_list, blog_detail, blog_detail_views

app_name = 'blog'

urlpatterns = [
    path('blog_detail/<int:pk>/', blog_detail, name='blog_detail'),
    path('views/blog_detail/<int:pk>/', blog_detail_views, name='blog_detail_views'),
    path('blog/', blog_list, name='list'),
]
