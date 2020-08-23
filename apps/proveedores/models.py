from django.db import models

class Proveedor (models.Model):
    id_proveedor = models.AutoField (primary_key= True)
    nombre= models.CharField (max_length = 200, blank= False, null= False)
    apellido = models.CharField (max_length= 200, blank= False, null= False)
    dni = models.IntegerField ()
    categoria = models.CharField (max_length= 250, blank= False, null= False)
    telefono = models.IntegerField ()
    correo = models.CharField (max_length=100 , blank= False, null= False)
    direccion = models.CharField (max_length= 250, blank= False, null= False)
