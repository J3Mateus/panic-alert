# Generated by Django 4.2.6 on 2023-11-16 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.AddField(
            model_name='address',
            name='location',
            field=models.CharField(max_length=100, null=True, verbose_name='Localidade'),
        ),
        migrations.AlterModelTable(
            name='address',
            table='address',
        ),
    ]
