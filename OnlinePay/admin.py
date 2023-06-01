from django.contrib import admin
from .models import PayMethod


# Register your models here.


class OnlinePayAdmin(admin.ModelAdmin):
    list_display = ['user', 'card_type', 'balance']
    readonly_fields = ['balance']

    def save_model(self, request, obj, form, change):
        if not obj.balance:
            obj.balance = obj.pay_amount
        else:
            obj.balanse += obj.pay_amount
        obj.save()


admin.site.register(PayMethod, OnlinePayAdmin)
