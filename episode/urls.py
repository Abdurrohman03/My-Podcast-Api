from django.urls import path
from .views import index, episode, episodes, episode_views, get_ids_list, like

app_name = 'episode'

urlpatterns = [
    path('', index, name='index'),
    path('episodes/', episodes, name='episodes'),
    path('detail/<int:pk>/', episode_views, name='episode'),
    path('detail_views/<int:pk>/', episode, name='episode_views'),
    path('ids_list/', get_ids_list, name='get_ids_list'),
    path('like/', like, name='like'),
]
