# Generated by Django 2.1.7 on 2019-06-18 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transplante', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='author',
        ),
    ]
