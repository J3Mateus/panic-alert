# Generated by Django 4.2.6 on 2023-11-03 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='COP',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, verbose_name='Excluído')),
                ('name', models.CharField(max_length=500, verbose_name='Nome da delegacia')),
                ('address', models.CharField(max_length=500, verbose_name='Endereço da delegacia')),
                ('geolocation', models.CharField(max_length=500, verbose_name='Geolocalização da delegacia')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_cop', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deleted_cop', to=settings.AUTH_USER_MODEL)),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsible_cop', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cop',
            },
        ),
    ]