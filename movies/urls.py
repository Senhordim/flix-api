from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='movies_list_all'),
    path('movies/<int:pk>', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie_detail_update_and_delete'),
]
