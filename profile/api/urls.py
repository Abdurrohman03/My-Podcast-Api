from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import MyProfile


urlpatterns = [
    path('login/', obtain_auth_token),
    path('my/profile/', MyProfile.as_view()),
]
