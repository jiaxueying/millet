# Generated by Django 3.1 on 2020-08-18 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0009_dish_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='picture',
            field=models.ImageField(upload_to='', verbose_name='dish picture'),
        ),
    ]
