# Generated by Django 2.2.7 on 2019-12-03 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20191203_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dresses',
            name='user',
        ),
    ]
