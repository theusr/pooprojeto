# Generated by Django 2.1.7 on 2019-06-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transplante', '0006_auto_20190618_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='NameObjects',
        ),
    ]
