from django.contrib import admin
from .models import Libro, Cliente, Prestamo
# Register your models here.

admin.site.register(Libro)
admin.site.register(Cliente)
admin.site.register(Prestamo)


