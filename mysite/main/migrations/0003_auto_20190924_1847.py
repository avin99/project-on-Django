# Generated by Django 2.2.4 on 2019-09-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dish_name',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='price',
            field=models.IntegerField(default=''),
        ),
    ]
