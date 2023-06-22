# Generated by Django 4.2.1 on 2023-06-22 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0025_remove_historiaclinica_tipo_mascota_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 22, 16, 40, 47, 527844, tzinfo=datetime.timezone.utc), verbose_name='Fecha de alta'),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='fecha_consulta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 22, 16, 40, 47, 527844, tzinfo=datetime.timezone.utc), verbose_name='Fecha de consulta'),
        ),
    ]
