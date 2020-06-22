from rest_framework import serializers
from .models import ClientProduct, ClientActivity


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


class ClientActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientActivity
        fields = (
            'id',
            'user',
            'id_activity',
            'active',
        )

    def save(self):
        try:
            user = self.validated_data['user']
            id_activity = self.validated_data['id_activity']
            active = self.validated_data['active']

            client_activity = ClientActivity(
                user=user,
                id_activity=id_activity,
                active=active,
            )
            client_activity.save()
            return client_activity
        except KeyError:
            raise serializers.ValidationError({"response": "Nie podano wszystkich argumentów!"})
