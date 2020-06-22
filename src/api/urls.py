from django.urls import path
from .views import (
    client_product_view,
    client_activity_view,
)

app_name = 'api'

urlpatterns = [
    path('product/', client_product_view, name='product'),
    path('activity/', client_activity_view, name="activity"),
]
