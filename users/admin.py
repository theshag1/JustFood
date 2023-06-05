from django.contrib import admin

from .models import User


# Register your models here.


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    readonly_fields = ('balance',)
    list_display = ['username', 'email']
