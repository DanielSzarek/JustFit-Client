from django.urls import path
from .views import (
    client_product_view,
    client_exercise_view
)

app_name = 'api'

urlpatterns = [
    path('product/', client_product_view, name='product'),
    path('exercise/', client_exercise_view, name="exercise"),
]
