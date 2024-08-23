from rest_framework import generics, permissions
from genres.models import Genre
from .serializers import GenreSerializer

class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (
      permissions.IsAuthenticated,
    )
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
      permissions.IsAuthenticated,
    )
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
