from django.contrib import admin

# Register your models here.

from .models import Food, Comment, LikeDislike


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(LikeDislike)
class LIkeDislike(admin.ModelAdmin):
    list_display = ['user', 'food', 'type']


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ['food', 'user']
