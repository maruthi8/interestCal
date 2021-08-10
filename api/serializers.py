from rest_framework import serializers

from api.models import FinanceUser, AmountDetails


class FinanceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceUser
        fields = ("phone_number", "password", "user_type")


class AmountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmountDetails
        fields = "__all__"
