from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication

from django.conf import settings
from .models import ClientProduct, ClientExercise
from .serializers import ClientExerciseSerializer, ClientProductSerializer


ACCOUNT = settings.AUTH_USER_MODEL


@api_view(['GET', 'POST'])
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

    if request.method == 'POST':
        data = request.data
        # We check if someone from staff giving a product
        if data['user'] is None and not request.user.is_staff and not request.user.is_superuser:
            data['user'] = account.pk
        serializer = ClientProductSerializer(data=data)
        data_response = {}
        if serializer.is_valid():
            client_product = serializer.save()
            data_response['id'] = client_product.pk
            data_response['user'] = client_product.user.pk
            data_response['id_product'] = client_product.id_product
            data_response['active'] = client_product.active
            return Response(data=data_response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
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

    if request.method == 'POST':
        data = request.data
        # We check if someone from staff giving a product
        if not request.user.is_staff and not request.user.is_superuser:
            data['user'] = account.pk

        serializer = ClientExerciseSerializer(data=data)
        data_response = {}
        if serializer.is_valid():
            client_exercise = serializer.save()
            data_response['id'] = client_exercise.pk
            data_response['user'] = client_exercise.user.pk
            data_response['id_exercise'] = client_exercise.id_exercise
            data_response['active'] = client_exercise.active
            return Response(data=data_response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
