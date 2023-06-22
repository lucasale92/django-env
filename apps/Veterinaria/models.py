
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager



# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

#Clase Cliente
class Cliente(models.Model):
    dni = models.PositiveIntegerField(verbose_name="D.N.I", unique=True, blank=True)
    nombre= models.CharField(verbose_name="Nombre/s", max_length=30)
    apellido=models.CharField(verbose_name="Apellido/s", max_length=30)
    ciudad=models.CharField(verbose_name="Ciudad", max_length=30)
    direccion=models.CharField(verbose_name="Direccion", max_length=30)
    telefono = models.PositiveIntegerField(verbose_name='Telefono', null= True, blank=True)
    fecha_alta=models.DateField(verbose_name="Fecha de alta", default=timezone.now(), blank=True)
    estado=models.BooleanField(verbose_name="Estado", default=True)
    objects = UserManager()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['id']
         
#Clase Mascota
class Mascota(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name= "propietario" )
    numero_chip = models.IntegerField(verbose_name="Numero de chip", unique=True, blank=True)
    nombre_mascota = models.CharField(verbose_name="Nombre de mascota", max_length=30)
    tipo_mascota = models.CharField(verbose_name="Tipo de mascota", max_length=30,null= True, blank=True)
    estado=models.BooleanField(verbose_name="Estado", default=True)

    def __str__(self):
        return f"{self.tipo_mascota}"
    
    class Meta:
        verbose_name =  'Mascota'
        verbose_name_plural =  'Mascotas'
        db_table = 'mascota'
        ordering = ['id']

#Clase Historia Clinica
class HistoriaClinica(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT, verbose_name= 'mascota')
    fecha_consulta=models.DateField(verbose_name="Fecha de consulta",default=timezone.now() , blank=True)
    observaciones = models.TextField(verbose_name= "Observaciones", max_length=500)
    estado=models.BooleanField(verbose_name="Estado", default=True)

    def __str__(self):
        return f"{self.fecha_consulta}"
    
    class Meta:
        verbose_name =  'Historia clinica'
        verbose_name_plural =  'Historias clinicas'
        db_table = 'historia_clinica'
        ordering = ['id']
        

