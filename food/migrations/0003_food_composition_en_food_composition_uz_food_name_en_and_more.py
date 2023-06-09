# Generated by Django 4.2 on 2023-06-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='composition_en',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='composition_uz',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='name_en',
            field=models.CharField(max_length=1500, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='food',
            name='name_uz',
            field=models.CharField(max_length=1500, null=True, unique=True),
        ),
    ]
