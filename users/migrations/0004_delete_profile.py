# Generated by Django 3.1.4 on 2020-12-24 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
