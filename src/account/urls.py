from django.urls import path
from .views import (
    token_delete,
    user_properties_view,
    account_retrieve_view,
    AccountListView,
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('token/create/', obtain_auth_token, name='api_token_auth'),
    path('token/destroy/', token_delete, name='api_token_delete'),

    path('client/properties/', user_properties_view, name='properties'),
    path('properties/<int:pk>', account_retrieve_view, name="account"),
    path('search/', AccountListView.as_view(), name="accounts"),
]
