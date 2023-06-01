from rest_framework import serializers

from Category.models import Category


class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'slug', 'image', 'position')
        read_only_fields = ('id', 'title')
