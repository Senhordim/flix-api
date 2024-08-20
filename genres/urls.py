from django.urls import path

from . import views

urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name='genre_list_all'),
    path('genres/<int:pk>', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre_detail_update_and_delete'),
]
