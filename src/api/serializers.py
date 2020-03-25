from rest_framework import serializers
from .models import ClientProduct, ClientExercise


# TODO Add some validation and change fields
class ClientProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProduct
        fields = "__all__"


class ClientExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientExercise
        fields = "__all__"
