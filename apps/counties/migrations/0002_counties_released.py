# Generated by Django 4.2.6 on 2024-01-11 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='counties',
            name='released',
            field=models.BooleanField(default=False, verbose_name='Cidade liberada'),
        ),
    ]
