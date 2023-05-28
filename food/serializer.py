from rest_framework import serializers

from food.models import Food, LikeDislike, Comment


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = (
            'name',
            'slug',
            'price',
            'composition',
            'image',
            'category'
        )
        read_only_fields = ('id',)


class LikeDislikeSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=LikeDislike.Textchoices.choices)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'body', 'food')
        read_only_fields = ('id',)
