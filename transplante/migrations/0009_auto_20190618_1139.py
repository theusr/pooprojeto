# Generated by Django 2.1.7 on 2019-06-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transplante', '0008_auto_20190618_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
