# Generated by Django 4.2.1 on 2023-11-26 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpComercial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
                ('surnames', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('op_comercial', models.CharField(choices=[('En Proceso', 'En Proceso'), ('Desiste', 'Desiste'), ('Completado', 'Completado')], default='En Proceso', max_length=30, verbose_name='Oportunidad Comercial')),
                ('user_creation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_creation', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Oportunidad Comercial',
                'verbose_name_plural': 'Oportunidades Comerciales',
                'ordering': ['id'],
            },
        ),
    ]