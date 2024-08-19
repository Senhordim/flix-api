from django.urls import path

from actors.views import (
    ActorCreateListView,
    ActorRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', ActorCreateListView.as_view(), name='actors'),
    path('<int:pk>', ActorRetrieveUpdateDestroyView.as_view(), name='actor_detail_update_and_delete'),
]
