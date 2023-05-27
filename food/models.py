from django.db import models
from django.utils.text import slugify


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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            return super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='comment_food')
    body = models.TextField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='comment')


class LIkeDislike(models.Model):
    class Textchoices(models.TextChoices):
        Like = '+',
        DIslike = '-'

    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_like_dislike')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='food_like_dislike')
    type = models.CharField(max_length=10, choices=Textchoices.choices)

    class Meta:
        unique_together = ['food', 'user']

    def __str__(self):
        return f'{self.user}'
