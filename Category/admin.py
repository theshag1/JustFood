from django.contrib import admin

from .models import Category


# Register your models here.

@admin.register(Category)
class Admin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'position']


