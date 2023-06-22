# Generated by Django 4.2.1 on 2023-06-05 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0010_alter_cliente_fecha_alta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 5, 14, 55, 50, 208888, tzinfo=datetime.timezone.utc), verbose_name='Fecha de alta'),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='fecha_consulta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 5, 14, 55, 50, 209888, tzinfo=datetime.timezone.utc), verbose_name='Fecha de consulta'),
        ),
    ]
