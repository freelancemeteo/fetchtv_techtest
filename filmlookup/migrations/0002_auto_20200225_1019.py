# Generated by Django 3.0.3 on 2020-02-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmlookup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='link',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='results',
            name='title',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='results',
            name='year',
            field=models.TextField(default=''),
        ),
    ]
