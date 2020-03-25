from django.urls import path
from .views import (
    user_properties_view,
    account_retrieve_view,
    AccountListView,
)

app_name = 'account'

urlpatterns = [
    path('properties', user_properties_view, name='properties'),
    path('properties/<int:pk>', account_retrieve_view, name="account"),
    path('accounts', AccountListView.as_view(), name="accounts"),
]
