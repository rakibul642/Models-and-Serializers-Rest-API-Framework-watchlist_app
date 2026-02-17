from watchlist_app import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics

'''
@api_view()
def movie_list(request):
    movies = models.MovieList.objects.all() # python objects
    serializer = serializers.MovieListSerializer(movies, many=True) # python object ke json a convert korbe
    return Response(serializer.data)
'''
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
    
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# PUT --> update(whole object kei pathate hoy)
# PATCH --> je part ta change korbo setake pathalei hobe
def movie_detail(request, pk):
    movie = get_object_or_404(models.MovieList, pk=pk)   

    if request.method == 'GET':
        serializer = serializers.MovieListSerializer(movie) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = serializers.MovieListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = serializers.MovieListSerializer(movie, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        movie.delete()
        return Response({'message' : 'Movie deleted successfully!!'})
        '''
# 1. List of all movies , create a new movie
class MovieListCreateView(generics.ListAPIView):
    queryset = models.MovieList.objects.all()
    serializer_class = serializers.MovieListSerializer


# 2.single movie/update/delete
class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MovieList.objects.all()
    serializer_class = serializers.MovieListSerializer