from django.db import models


# Create your models here.
class Basket(models.Model):
    food = models.ForeignKey('food.Food', on_delete=models.CASCADE, related_name='order_basket')
    price = models.BigIntegerField()
    amount = models.BigIntegerField()
    order_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.food} : {self.amount}'

    @property
    def amount_price(self):
        all_price = str(self.price * self.amount)
        return all_price

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.food.food_price
        return super().save(*args, **kwargs)
