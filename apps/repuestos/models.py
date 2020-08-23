from django.db import models

class Repuesto (models.Model) : 
    id_repuesto = models.AutoField (primary_key= True)
    nombre = models.CharField ('nombre',max_length= 200, blank= False, null= False)
    stock = models.IntegerField(default= 0 )
    categoria = models.CharField ('categoria', max_length= 200, blank= False, null= False)
   