from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'name movies_count'.split()

    def get_movies_count(self, obj):
        return obj.movies.count()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieReviewSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title reviews rating'.split()
        # depth = 1

    def get_rating(self, obj):
        try:
            reviews = obj.reviews.all()
            stars = sum([i.stars for i in reviews])/len(reviews)
            return stars
        except:
            return None