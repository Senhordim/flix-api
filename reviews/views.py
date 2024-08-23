from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (
      permissions.IsAuthenticated,
    )
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
      permissions.IsAuthenticated,
    )
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
