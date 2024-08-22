from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from rest_framework import status
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieReviewSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(http_method_names=['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        list_ = DirectorSerializer(instance=director, many=True).data
        return Response(data=list_, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'Post'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        list_ = MovieSerializer(instance=movie, many=True).data
        return Response(data=list_, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id)
        return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie_id = request.data.get('movie_id')
        return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        list_ = ReviewSerializer(instance=review, many=True).data
        return Response(data=list_, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        review = Review.objects.create(
            text=text,
            stars=stars,
            movie_id=movie_id
        )
        return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_review_api_view(request):
    movie = Movie.objects.all()
    list_ = MovieReviewSerializer(instance=movie, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)