from django import forms    
from .models import Cliente

class clienteForm (forms.ModelForm): 
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido','dni','direccion','correo','edad']
