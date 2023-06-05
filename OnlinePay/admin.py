from django.contrib import admin
from .models import PayMethod


# Register your models here.


class OnlinePayAdmin(admin.ModelAdmin):
    list_display = ['user', 'card_type']


admin.site.register(PayMethod, OnlinePayAdmin)
