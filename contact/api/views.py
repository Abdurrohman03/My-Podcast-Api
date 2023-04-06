from .serializers import ContactSerializer, NewsletterSerializer
from rest_framework import generics, permissions
from ..models import Contact, Newsletter
from .permissions import IsAdminUserOrReadOnly, IsAdminUser


class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SubscribeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class SubscribeRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [IsAdminUserOrReadOnly]

