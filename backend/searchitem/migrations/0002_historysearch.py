# Generated by Django 3.0.2 on 2020-01-28 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('searchitem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorySearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='datetime')),
                ('searchitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searchitem.SearchItem', verbose_name='searchitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='user')),
            ],
            options={
                'verbose_name': 'HistorySearch',
                'verbose_name_plural': 'HistorySearches',
            },
        ),
    ]