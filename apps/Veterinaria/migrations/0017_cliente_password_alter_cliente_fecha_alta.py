# Generated by Django 4.2.1 on 2023-06-21 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0016_alter_cliente_fecha_alta'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='password',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 21, 14, 35, 2, 998978, tzinfo=datetime.timezone.utc), verbose_name='Fecha de alta'),
        ),
    ]