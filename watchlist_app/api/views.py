from watchlist_app import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def movie_list(request):
    movies = models.MovieList.objects.all() # python objects
    serializer = serializers.MovieListSerializer(movies, many=True) # python object ke json a convert korbe
    return Response(serializer.data)
