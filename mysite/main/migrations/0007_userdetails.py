# Generated by Django 2.2.4 on 2019-09-15 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190914_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(help_text='Required. Inform a valid email address.', max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('is_owner', models.BooleanField(default=False)),
            ],
        ),
    ]