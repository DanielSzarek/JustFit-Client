from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'phone_number',
        )


class AccountNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'id',
            'first_name',
        )
