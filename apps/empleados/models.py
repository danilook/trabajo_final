from django.db import models
import datetime 


class Empleado(models.Model): 
  id_empleado = models.AutoField (primary_key = True)
  nombre = models.CharField (default='', max_length = 200, blank = False, null = False) 
  apellido = models.CharField (default='', max_length = 250, blank = False, null = False)
  dni = models.IntegerField (blank = True, null = True)
  rol = models.CharField (default= '', max_length = 200 , blank = False, null = False) 
  fecha_alta = models.DateField(blank = False, null = False)
  reputacion = models.IntegerField (blank = False, null = False)

