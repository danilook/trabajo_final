from django import forms    
from .models import Cliente

class clienteForm (forms.ModelForm): 
    class Meta:
        model = Cliente
        Fields = ['nombre', 'apellido','dni','direccion','correo','edad']
