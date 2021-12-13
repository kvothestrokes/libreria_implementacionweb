from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import escape
from .models import Libro, Cliente, Prestamo

# Create your views here.

def index(request):
    return render(request, 'vistas/home.html')

#CONTROLLERS LIBRO
def libros_index(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {
        'libros':libros
    })

def libro_create(request):
    autor = request.POST.get('autor', '')
    titulo = request.POST.get('titulo', '')
    editorial = request.POST.get('editorial', '')

    new_libro = Libro(titulo=titulo, autor= autor, editorial= editorial)
    new_libro.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/libros'))

def libro_update(request, pk):
    
    autor = request.POST.get('autor', '')
    titulo = request.POST.get('titulo', '')
    editorial = request.POST.get('editorial', '')    
    libro = Libro.objects.get(id = pk)
    Libro.objects.filter(id=pk).update(titulo=titulo, autor=autor, editorial=editorial)
   
    # libro.titulo = titulo
    # libro.autor = autor
    # libro.editorial = editorial
    # libro.save()    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def libro_del(request, pk):
    Libro.objects.filter(id=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# CONTROLLERS CLIENTE
def cliente_index(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente.html', {
        'clientes':clientes
    })

def cliente_create(request):
    nombre = request.POST.get('nombre', '')
    telefono = request.POST.get('tel', '')
    ine = request.POST.get('ine', '')

    new_client = Cliente(nombre=nombre, telefono=telefono, INE=ine)
    new_client.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/clientes'))

def cliente_update(request, pk):
    
    nombre = request.POST.get('nombre', '')
    telefono = request.POST.get('tel', '')
    ine = request.POST.get('ine', '')
    
    Cliente.objects.filter(id=pk).update(nombre=nombre, telefono=telefono, INE=ine)
       
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def cliente_del(request, pk):
    Cliente.objects.filter(id=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# CONTROLLERS PRESTAMOS
def prestamos_index(request):
    prestamos = Prestamo.objects.all()
    clientes = Cliente.objects.all()
    libros = Libro.objects.all()
    return render(request, 'prestamos.html', {
        'prestamos':prestamos,
        'clientes':clientes,
        'libros':libros
    })

def prestamos_create(request):
    cliente = request.POST.get('id_cliente', '')
    libro = request.POST.get('id_libro', '')
    f_prestamo = request.POST.get('f_prestamo', '')
    f_devolucion = request.POST.get('f_devolucion', '')    

    cliente_instance = Cliente.objects.get(id=cliente)
    libro_instance = Libro.objects.get(id=libro)

    new_prestamo = Prestamo(libro=libro_instance, cliente=cliente_instance, fecha_prestamo=f_prestamo, fecha_devolucion=f_devolucion)
    new_prestamo.save()    
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/prestamos'))

def prestamos_del(request, pk):
    Prestamo.objects.filter(id=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
