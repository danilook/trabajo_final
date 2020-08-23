from django.db import models


class Empleado(models.Model): 
  id_empleado = models.AutoField (primary_key= True) 
  rol = models.CharField ( max_length = 200 , blank= False, null= False) 
  fecha_alta = models.DateField(blank= False, null= False)
  reputacion = models.IntegerField (blank= False, null= False)

