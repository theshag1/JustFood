from rest_framework import serializers
from .models import Queue


class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = ('queue', 'created_at', 'user', 'is_being_prepared')
        read_only_fields = ('id',)

