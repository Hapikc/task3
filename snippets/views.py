from rest_framework import generics
from django.contrib.auth.models import User
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):
   queryset = Snippet.objects.all()
   serializer_class = SnippetSerializer
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]

   def perform_create(self, serializer):
       serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Snippet.objects.all()
   serializer_class = SnippetSerializer
   permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class UserList(generics.ListAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
