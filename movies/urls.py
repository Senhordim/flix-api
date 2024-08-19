from django.urls import path

from movies.views import (
    MovieCreateListView,
    MovieRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', MovieCreateListView.as_view(), name='movies_list_all'),
    path('<int:pk>', MovieRetrieveUpdateDestroyView.as_view(), name='movie_detail_update_and_delete'),
]
