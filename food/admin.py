from django.contrib import admin

# Register your models here.

from .models import Food, Comment, LikeDislike

admin.site.register(Food)


@admin.register(LikeDislike)
class LIkeDislike(admin.ModelAdmin):
    list_display = ['user', 'food', 'type']


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ['food', 'user']
