# Generated by Django 4.2.1 on 2023-06-01 00:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.PositiveIntegerField(blank=True, unique=True, verbose_name='D.N.I')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre/s')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido/s')),
                ('ciudad', models.CharField(max_length=30, verbose_name='Ciudad')),
                ('direccion', models.CharField(max_length=30, verbose_name='Direccion')),
                ('telefono', models.PositiveIntegerField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('fecha_alta', models.DateField(blank=True, default=datetime.datetime(2023, 5, 31, 21, 33, 57, 575597), max_length=15, verbose_name='Fecha de alta')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'db_table': 'cliente',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_chip', models.IntegerField(blank=True, unique=True, verbose_name='Numero de chip')),
                ('nombre_mascota', models.CharField(max_length=30, verbose_name='Nombre de mascota')),
                ('tipo_mascota', models.CharField(max_length=30, verbose_name='Tipo de mascota')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Veterinaria.cliente', verbose_name='propietario')),
            ],
            options={
                'db_table': 'mascota',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_consulta', models.DateField(blank=True, default=datetime.datetime(2023, 5, 31, 21, 33, 57, 576597), max_length=15, verbose_name='Fecha de consulta')),
                ('observaciones', models.TextField(max_length=500, verbose_name='Observaciones')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('mascota_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Veterinaria.mascota', verbose_name='mascota')),
            ],
            options={
                'db_table': 'historia_clinica',
                'ordering': ['id'],
            },
        ),
    ]
