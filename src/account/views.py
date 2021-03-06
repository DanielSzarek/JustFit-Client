from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Account
from .serializers import AccountSerializer, AccountNameSerializer


@swagger_auto_schema(method='post', responses={
    204: openapi.Response('response description'),
}, tags=['account-token'])
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def token_delete(request):
    """
    Use this view to simply logout user and destroy his token

    :param request:
    :return:
    """
    # I had to add a token for authorization
    # Tt will help in connection between client frontend and events frontend and be more secure as well
    request.user.auth_token.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='put', request_body=AccountSerializer, tags=['account-client'])
@swagger_auto_schema(methods=['get'], responses={
    200: openapi.Response('response description', AccountSerializer),
}, tags=['account-client'])
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication, TokenAuthentication])
def user_properties_view(request):
    """
    This view will be used by our clients to get their accounts

    :param request:
    :return Response:
    """
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        data = serializer.data
        is_admin = {'is_admin': account.is_admin}
        if account.is_admin:
            data.update(is_admin)
        return Response(data)

    if request.method == 'PUT':
        # Probably we will not need a PUT method for our small project
        # Lets keep it for now, maybe our frontend guys will be able to add it also
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=AccountSerializer, tags=['account-admin'])
@swagger_auto_schema(methods=['get'], responses={
    200: openapi.Response('response description', AccountSerializer),
}, tags=['account-admin'])
@api_view(['GET', 'PUT'])
@permission_classes([IsAdminUser])
@authentication_classes([BasicAuthentication, TokenAuthentication])
def account_retrieve_update_view(request, pk):
    """
    This view will be used by admins to retrieve and change data

    :param request:
    :param pk:
    :return Response:
    """
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['get'], manual_parameters=[
    openapi.Parameter('ids', openapi.IN_QUERY, "Account ids ex. ?ids=1,2,3", type=openapi.TYPE_STRING)],
                     responses={
    200: openapi.Response('response description', AccountSerializer)},
                     tags=['account-client'])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication, TokenAuthentication])
def accounts_retrieve_by_ids(request):
    """
    This endpoint will retrieve all user names by ids

    :param request:
    :return:
    """
    if request.method == 'GET':
        ids = request.query_params.get('ids', None)
        if ids is not None:
            ids = ids.split(',')
        else:
            return Response({'Nie podano parametru ids!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            accounts = Account.objects.filter(pk__in=ids)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AccountNameSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountListView(ListAPIView):
    """
    This view will be used by admins to find and filter clients.

    :return Response:
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes(BasicAuthentication)
    permission_classes = (IsAdminUser,)
    filter_backends = (SearchFilter, OrderingFilter)
    pagination_class = PageNumberPagination
    search_fields = ('email', 'username', 'first_name', 'last_name')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
