# Generated by Django 4.2 on 2023-05-29 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1500, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('food_price', models.BigIntegerField()),
                ('composition', models.CharField(max_length=1500)),
                ('image', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_category', to='Category.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='food.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_food', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeDislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('+', 'Like'), ('-', 'Dislike')], max_length=10)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_like_dislike', to='food.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_like_dislike', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('food', 'user')},
            },
        ),
    ]
