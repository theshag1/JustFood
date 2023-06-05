from rest_framework import serializers
from .models import PayMethod


class OnlinePaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PayMethod
        fields = ('user', 'card_type', 'card_number', 'pay_amount', 'created_at')
        read_only_fields = ('id',)


class PaySerializer(serializers.Serializer):
    pay_amount = serializers.IntegerField()
