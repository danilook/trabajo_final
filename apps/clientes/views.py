from django.shortcuts import render,redirect
from .forms import clienteForm

def Home (request):
    return render(request,'index.html')

def crearCliente (request) :
    if request.method == 'POST':
        cliente_form = clienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('index')
    else:
        cliente_form = clienteForm ()
    return  render(request,'clientes/crear_cliente.html' ,{'cliente_form':cliente_form})


