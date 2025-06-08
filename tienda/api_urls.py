# tienda_api/api_urls.py
from django.urls import path
from .api_views import *

urlpatterns = [
    path('productos/', listar_productos, name='listar_productos'),  # Para listar todos los productos
    path('producto-api/<int:producto_id>/', obtener_producto, name='obtener_producto'),  # Para obtener un producto específico
    path('producto-api/crear/', crear_producto, name='crear_producto'),  # Para crear un producto
    path('producto-api/eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),  # Para eliminar un producto
]
