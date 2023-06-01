from django.contrib import admin
from .models import Basket


class BasketAdmin(admin.ModelAdmin):
    list_display = ['food', 'price', 'amount', 'order_created', 'amount_price']
    readonly_fields = ['price']

    def save_model(self, request, obj, form, change):
        if not obj.price:
            obj.price = obj.food.food_price
        obj.save()


admin.site.register(Basket, BasketAdmin)
