from django.urls import path
from .  import views

urlpatterns = [
    path('', views.index, name='index'),
    # Rutas Libro
    path('libros', views.libros_index, name="libros"),    
    path('libros/crear', views.libro_create, name="crear_libro"),
    path('libros/actualizar/<int:pk>', views.libro_update, name="actualizar_libro"),
    path('libros/borrar/<int:pk>', views.libro_del, name="borrar_libro"),
    # Rutas Cliente
    path('clientes', views.cliente_index, name="clientes"),    
    path('clientes/crear', views.cliente_create, name="crear_cliente"),
    path('clientes/actualizar/<int:pk>', views.cliente_update, name="actualizar_cliente"),
    path('clientes/borrar/<int:pk>', views.cliente_del, name="borrar_cliente"),
    # Rutas Préstamos
    path('prestamos', views.prestamos_index, name="prestamos"),    
    path('prestamos/crear', views.prestamos_create, name="crear_prestamo"),    
    path('prestamos/borrar/<int:pk>', views.prestamos_del, name="borrar_prestamo")

]