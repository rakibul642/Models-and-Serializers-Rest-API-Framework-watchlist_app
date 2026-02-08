from rest_framework import serializers
from watchlist_app import models

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieList
        fields = '__all__'