from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication

from django.conf import settings
from .models import ClientProduct, ClientExercise
from .serializers import ClientExerciseSerializer, ClientProductSerializer


ACCOUNT = settings.AUTH_USER_MODEL

# TODO Both endpoints needs POST method!


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def client_product_view(request):
    try:
        account = request.user
    except ACCOUNT.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    products = ClientProduct.objects.filter(user=account)

    if request.method == 'GET':
        serializer = ClientProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def client_exercise_view(request):
    try:
        account = request.user
    except ACCOUNT.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    exercises = ClientExercise.objects.filter(user=account)

    if request.method == 'GET':
        serializer = ClientExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
