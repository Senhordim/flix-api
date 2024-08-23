from rest_framework import generics, permissions
from movies.models import Movie
from .serializers import MovieSerializer

class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (
      permissions.IsAuthenticated,
    )
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
      permissions.IsAuthenticated,
    )
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
