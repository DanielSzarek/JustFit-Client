from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication, TokenAuthentication

from django.conf import settings
from .models import ClientProduct, ClientActivity
from .serializers import ClientActivitySerializer, ClientProductSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

ACCOUNT = settings.AUTH_USER_MODEL


@swagger_auto_schema(method='post', request_body=ClientProductSerializer, tags=['product'])
@swagger_auto_schema(methods=['get'], responses={
    200: openapi.Response('response description', ClientProductSerializer),
}, tags=['product'])
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication, TokenAuthentication])
def client_product_view(request):
    """
    These methods are responsible for merging clients with products from other API

    :param request:
    :return:
    """
    try:
        account = request.user
    except ACCOUNT.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    products = ClientProduct.objects.filter(user=account)

    if request.method == 'GET':
        serializer = ClientProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data.copy()
        # We check if someone from staff is using that method
        if not request.user.is_staff and not request.user.is_superuser:
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


@swagger_auto_schema(method='post', request_body=ClientActivitySerializer, tags=['activity'])
@swagger_auto_schema(methods=['get'], responses={
    200: openapi.Response('response description', ClientActivitySerializer),
}, tags=['activity'])
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication, TokenAuthentication])
def client_activity_view(request):
    """
    These methods are responsible for merging clients with activities from other API

    :param request:
    :return:
    """
    try:
        account = request.user
    except ACCOUNT.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    activities = ClientActivity.objects.filter(user=account)

    if request.method == 'GET':
        serializer = ClientActivitySerializer(activities, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data.copy()
        # We check if someone from staff is using that method
        if not request.user.is_staff and not request.user.is_superuser:
            data['user'] = account.pk

        serializer = ClientActivitySerializer(data=data)
        data_response = {}
        if serializer.is_valid():
            client_activity = serializer.save()
            data_response['id'] = client_activity.pk
            data_response['user'] = client_activity.user.pk
            data_response['id_activity'] = client_activity.id_activity
            data_response['active'] = client_activity.active
            return Response(data=data_response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
