from django.db import models
from clientes.models import Persona

class Empleado(Persona): 
   id_empleado = models.AutoField (primary_key= True) 
   rol = models.CharField ( max_length = 200 , blank= False, null= False) 
   fecha_alta = models.DateField(blank= False, null= False)
   reputacion = models.IntegerField (blank= False, null= False)
