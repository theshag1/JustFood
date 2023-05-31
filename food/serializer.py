from rest_framework import serializers

from food.models import Food, LikeDislike, Comment


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'name',
            'slug',
            'food_price',
            'composition',
            'image',
            'category',
            'likes',
            'dislike',
        ]
        read_only_fields = ('id', 'price')


class LikeDislikeSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=LikeDislike.Textchoices.choices)


class UserLikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeDislike
        fields = (
            'food',
            'user',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'body', 'food')
        read_only_fields = ('id',)
