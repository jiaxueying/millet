# Generated by Django 3.1 on 2020-08-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0008_auto_20200810_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='weight of single product'),
            preserve_default=False,
        ),
    ]