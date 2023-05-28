from django.db import models
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(null=False)
    position = models.IntegerField(default=1)

    def __str__(self):
        return self.title
