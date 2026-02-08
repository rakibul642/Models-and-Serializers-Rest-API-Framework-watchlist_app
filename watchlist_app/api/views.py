from watchlist_app import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

'''
@api_view()
def movie_list(request):
    movies = models.MovieList.objects.all() # python objects
    serializer = serializers.MovieListSerializer(movies, many=True) # python object ke json a convert korbe
    return Response(serializer.data)
'''
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = models.MovieList.objects.all() # python objects
        serializer = serializers.MovieListSerializer(movies, many=True) # python object ke json a convert korbe
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.MovieListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)