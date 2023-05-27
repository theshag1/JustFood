from django.contrib import admin

# Register your models here.

from .models import Food, Comment, LIkeDislike

admin.site.register(Food)


@admin.register(LIkeDislike)
class LIkeDislike(admin.ModelAdmin):
    list_display = ['food', 'user', 'type']


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ['food', 'user']
