from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class Basket(models.Model):
    food = models.ForeignKey('food.Food', on_delete=models.CASCADE, related_name='oreder_basket')
    price = models.BigIntegerField()
    amount = models.BigIntegerField()
    order_created = models.DateTimeField()

    @property
    def amount_price(self):
        all_price = str(self.price * self.amount)
        return all_price

    def save(self, *args, **kwargs):
        if not self.price:
            if not self.price:
                self.price = self.food.food_price
                return super().save(*args, **kwargs)
