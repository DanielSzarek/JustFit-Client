from django.urls import path
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .views import (
    token_delete,
    user_properties_view,
    account_retrieve_update_view,
    AccountListView,
    accounts_retrieve_by_ids,
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

decorated_search_view = \
   swagger_auto_schema(
        method='get',
        tags=['account-admin']
   )(AccountListView.as_view())

decorated_token_view = \
   swagger_auto_schema(
        method='post',
        tags=['account-token'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Account username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Account password'),
            }
        ),
        operation_summary="Get auth token"
    )(obtain_auth_token)

urlpatterns = [
    path('token/create/', decorated_token_view, name='api_token_auth'),
    path('token/destroy/', token_delete, name='api_token_delete'),

    path('client/properties/', user_properties_view, name='properties'),
    path('properties/<int:pk>', account_retrieve_update_view, name="account"),
    path('search/', decorated_search_view, name="accounts"),
    path('clients/', accounts_retrieve_by_ids, name="accounts")
]
