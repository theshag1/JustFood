# Generated by Django 4.2 on 2023-06-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.BigIntegerField()),
                ('amount', models.BigIntegerField()),
                ('order_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]