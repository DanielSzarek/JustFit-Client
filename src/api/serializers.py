from rest_framework import serializers
from .models import ClientProduct, ClientExercise


class ClientProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProduct
        fields = (
            'id',
            'user',
            'id_product',
            'active',
        )

    def save(self):
        try:
            user = self.validated_data['user']
            id_product = self.validated_data['id_product']
            active = self.validated_data['active']

            client_product = ClientProduct(
                user=user,
                id_product=id_product,
                active=active,
            )
            client_product.save()
            return client_product
        except KeyError:
            raise serializers.ValidationError({"response": f"Nie podano wszystkich argumentów!"})


class ClientExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientExercise
        fields = (
            'id',
            'user',
            'id_exercise',
            'active',
        )

    def save(self):
        try:
            user = self.validated_data['user']
            id_exercise = self.validated_data['id_exercise']
            active = self.validated_data['active']

            client_exercise = ClientExercise(
                user=user,
                id_exercise=id_exercise,
                active=active,
            )
            client_exercise.save()
            return client_exercise
        except KeyError:
            raise serializers.ValidationError({"response": "Nie podano wszystkich argumentów!"})
