from rest_framework import serializers

from basket.models import Basket


class BassketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('food', 'price', 'amount', 'order_created',)
        read_only_fields = ('id', 'price')
