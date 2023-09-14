# views.py

from rest_framework import generics
from .models import Movie
from .serailizer import MovieSerializer

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        genre_filter = self.request.query_params.get('genre')
        if genre_filter:
            return Movie.objects.filter(genres__name=genre_filter)
        return Movie.objects.all()
