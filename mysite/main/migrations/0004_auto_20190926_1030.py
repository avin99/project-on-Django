# Generated by Django 2.2.4 on 2019-09-26 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190924_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='dish_name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='price',
            field=models.IntegerField(),
        ),
    ]