# Generated by Django 2.2.5 on 2019-09-22 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190922_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='items',
            new_name='items_json',
        ),
    ]
