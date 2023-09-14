from django.urls import path
from movieapp.views import MovieListView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
]