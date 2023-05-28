from django.db import models


# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=1500, unique=True, null=False)
    slug = models.SlugField(unique=True, null=False)
    price = models.BigIntegerField(null=False)
    composition = models.CharField(max_length=1500)
    image = models.ImageField(null=False)
    category = models.ForeignKey('Category.Category', on_delete=models.CASCADE, related_name='food_category')

    def __str__(self):
        return self.name

    @property
    def likes(self):
        return self.food_like_dislike.filter(type=LikeDislike.Textchoices.Like).count()

    @property
    def dislike(self):
        return self.food_like_dislike.filter(type=LikeDislike.Textchoices.Dislike).count()

    @property
    def comment(self):
        return self.comment.count()


class Comment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='comment_food')
    body = models.TextField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return self.body


class LikeDislike(models.Model):
    class Textchoices(models.TextChoices):
        Like = '+',
        Dislike = '-'

    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_like_dislike')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='food_like_dislike')
    type = models.CharField(max_length=10, choices=Textchoices.choices)

    class Meta:
        unique_together = ['food', 'user']

    def __str__(self):
        return f'{self.user}'
