from rest_framework import serializers
from watchlist_app import models



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reviews
        fields = '__all__' 

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieList
        fields = '__all__'               