# Generated by Django 3.0.6 on 2020-05-20 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200519_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub',
            name='image',
        ),
    ]
