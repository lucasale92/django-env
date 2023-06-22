# Generated by Django 4.2.1 on 2023-06-21 17:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0018_remove_cliente_password_alter_cliente_fecha_alta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_alta',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 21, 17, 22, 22, 485248, tzinfo=datetime.timezone.utc), verbose_name='Fecha de alta'),
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_chip', models.IntegerField(blank=True, unique=True, verbose_name='Numero de chip')),
                ('nombre_mascota', models.CharField(max_length=30, verbose_name='Nombre de mascota')),
                ('tipo_mascota', models.CharField(max_length=30, verbose_name='Tipo de mascota')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Veterinaria.cliente', verbose_name='propietario')),
            ],
            options={
                'verbose_name': 'Mascota',
                'verbose_name_plural': 'Mascotas',
                'db_table': 'mascota',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_consulta', models.DateField(blank=True, default=datetime.datetime(2023, 6, 21, 17, 22, 22, 486247, tzinfo=datetime.timezone.utc), verbose_name='Fecha de consulta')),
                ('observaciones', models.TextField(max_length=500, verbose_name='Observaciones')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Veterinaria.mascota', verbose_name='mascota')),
            ],
            options={
                'verbose_name': 'Historia clinica',
                'verbose_name_plural': 'Historias clinicas',
                'db_table': 'historia_clinica',
                'ordering': ['id'],
            },
        ),
    ]