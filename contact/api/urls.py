from django.urls import path
from .views import ContactListCreateAPIView, ContactRUDAPIView, SubscribeListCreateAPIView, SubscribeRUDAPIView


urlpatterns = [
    # Contact
    path('contact-list-create/', ContactListCreateAPIView.as_view()),
    path('contact-rud/<int:pk>/', ContactRUDAPIView.as_view()),

    # Subscribe
    path('subscribe-list-create/', SubscribeListCreateAPIView.as_view()),
    path('subscribe-rud/<int:pk>/', SubscribeRUDAPIView.as_view()),
]
