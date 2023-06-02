from rest_framework import serializers

from basket.models import Basket


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('food', 'amount',)
        read_only_fields = ('id', 'price', 'order_created')
