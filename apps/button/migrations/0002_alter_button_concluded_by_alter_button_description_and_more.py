# Generated by Django 4.2.6 on 2023-12-04 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('button', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='concluded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='concluded_by_button', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='button',
            name='description',
            field=models.TextField(default='', null=True, verbose_name='Descrição do alerta'),
        ),
        migrations.AlterField(
            model_name='button',
            name='problem_solving',
            field=models.TextField(blank=True, default='', max_length=500, null=True, verbose_name='Resolução do problema'),
        ),
        migrations.AlterField(
            model_name='button',
            name='responsible',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsible_button', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='button',
            name='updater_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updater_by_button', to=settings.AUTH_USER_MODEL),
        ),
    ]