from rest_framework import generics, permissions
from actors.models import Actor
from .serializers import ActorSerializer

class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (
      permissions.IsAuthenticated,
    )
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer



class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
      permissions.IsAuthenticated,
    )
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
