from django.db import models

class  Persona(models.Model): 
   id_persona = models.AutoField (primary_key= True) 
   nombre = models.CharField(max_length = 220, blank = False, null = False)
   apellido = models.CharField(max_length = 220, blank = False, null = False)
   dni = models.IntegerField ()
   direccion = models.CharField(max_length = 220, blank = False, null = False)
   correo = models.CharField(max_length = 100, blank = False, null = False)
   edad = models.IntegerField ()
   

class Cliente (Persona) : 
   id_cliente = models.AutoField (primary_key= True)

   class Meta:
      verbose_name = 'Cliente'
      verbose_name_plural = 'Clientes'
      ordering = ['nombre']

   def  __str__(self):
      return self.nombre  

class Motovehiculo (models.Model):
   id_motovehiculo = models.AutoField (primary_key= True)
   patente = models.CharField ('Patente',default="" ,max_length= 100 , blank= False , null= False) 
   tipo_motovehiculo = models.CharField ('Tipo del motovehiculo' ,default= "", max_length= 200 , blank= False , null= False)
   cilindrada = models.IntegerField ()
   trasmision = models.CharField ('Trasmision del motovehiculo', default= "", max_length= 200 , blank= False, null= False)
   color = models.CharField ('Color del motovehicuio', default= "", max_length= 100 , blank= False , null= False)   
   Marca = models.CharField('Marca del motovehiculo', default="", max_length= 100, blank= False, null=False)

   class meta:
      verbose_name = 'Motovehiculo'
      verbose_name_plural = 'Motovehiculos'
      ordering = ['marca']

   def __str__(self):
      return self.patente
