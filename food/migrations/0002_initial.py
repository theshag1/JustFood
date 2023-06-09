# Generated by Django 4.2 on 2023-06-01 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Category', '0001_initial'),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='likedislike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_like_dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_category', to='Category.category'),
        ),
        migrations.AddField(
            model_name='comment',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='food.food'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_food', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='likedislike',
            unique_together={('food', 'user')},
        ),
    ]
