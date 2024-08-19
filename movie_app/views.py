from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from rest_framework import status
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(director).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def director_list_api_view(request):
    director = Director.objects.all()
    list_ = DirectorSerializer(instance=director, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movie).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def movie_list_api_view(request):
    movie = Movie.objects.all()
    list_ = MovieSerializer(instance=movie, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    list_ = ReviewSerializer(instance=review, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def movie_review_api_view(request):
    movie = Movie.objects.all()
    list_ = MovieReviewSerializer(instance=movie, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)