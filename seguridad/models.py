from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    cargos = ((u'1',u'Gerente'),(u'2',u'Supervisor'),
		(u'3',u'Trabajador'),)
    cargo = models.CharField(max_length=50,choices=cargos,default='3')

    class Meta:
        db_table = 'auth_user'

class Trabajo(models.Model):
    creador = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha 	= models.DateField(blank=True)
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre
