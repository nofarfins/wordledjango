from django.shortcuts import render
from models import *
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from serializers import *
# Create your views here.

LEVELS = {
    'EASY': -1,
    'MEDIUM': 10,
    'HARD': 6
}


@api_view(['POST'])
def signup(request):
    User.objects.create_user(
        username=request.data['username'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        password_first=request.data['password'],
        password_second = request.data['confirm']
    )

    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def current_user(request):
    if request.method == 'GET':
        data = {
            'username': request.user.username,
            'userId': request.user.id
        }
        return Response(data)

    if request.method == 'PUT':
        user = User.objects.get(pk=request.user.id)
        user['first_name'] = request.data.first_name
        user['last_name'] = request.data.last_name



@api_view(['GET'])
def start_game(request, difficulty, game_category):
    if request == 'GET':
        random_question = {}
        if game_category == 'NBA':
            random_question = nba1.get_random_question(difficulty)
        elif game_category == "animals":
            pass
        elif game_category == 'movies':
            pass
        elif game_category == 'country':
            pass

@api_view(['GET', 'POST', 'PUT'])
def user_results(request, pk):
    try:
        results = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProfileSerializer(results)
        return Response(serializer.data)

    elif request.method == 'PUT':
        results['games'] += 1
        if request.data['result'] == 1:
            results['wins'] += 1
        if request.data['result'] == 0:
            results['losses'] += 1
        results.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

