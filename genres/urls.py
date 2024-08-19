from django.contrib import admin
from django.urls import path

from genres.views import (
    GenreCreateListView,
    GenreRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', GenreCreateListView.as_view(), name='genre_list_all'),
    path('<int:pk>', GenreRetrieveUpdateDestroyView.as_view(), name='genre_detail_update_and_delete'),
]
