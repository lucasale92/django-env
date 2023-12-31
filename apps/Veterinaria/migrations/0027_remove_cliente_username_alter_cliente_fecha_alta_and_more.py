# Generated by Django 4.2.1 on 2023-06-22 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0026_alter_cliente_fecha_alta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='username',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 22, 17, 29, 39, 632700, tzinfo=datetime.timezone.utc), verbose_name='Fecha de alta'),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='fecha_consulta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 22, 17, 29, 39, 633702, tzinfo=datetime.timezone.utc), verbose_name='Fecha de consulta'),
        ),
    ]
