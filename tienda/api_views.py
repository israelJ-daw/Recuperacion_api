# tienda_api/api_views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ProductosTerceros
from .serializers import *
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['GET'])
@authentication_classes([OAuth2Authentication])
@permission_classes([IsAuthenticated])
def listar_productos(request):
    productos = ProductosTerceros.objects.all()
    serializer = ProductoTerceroSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([OAuth2Authentication])
@permission_classes([IsAuthenticated])
def obtener_producto(request, producto_id):
    try:
        producto = ProductosTerceros.objects.get(id=producto_id)
    except ProductosTerceros.DoesNotExist:
        return Response({"detail": "Producto no encontrado."}, status=404)
    serializer = ProductoTerceroSerializer(producto)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([OAuth2Authentication])
@permission_classes([IsAuthenticated])
def crear_producto(request):
    # Aquí estamos recibiendo los datos de un coche desde la vista
    serializer = ProductoTerceroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@authentication_classes([OAuth2Authentication])
@permission_classes([IsAuthenticated])
def eliminar_producto(request, producto_id):
    producto = ProductosTerceros.objects.get(id=producto_id)
    try:
        producto.delete()
        return Response("Producto Eliminado")
    except Exception as error:
        return Response(error, status=404)

    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductosTerceros # Asegúrate de que el modelo Producto esté en tu aplicación de API
from tienda.models import Tienda  # Importa el modelo Tienda desde tu aplicación normal
import requests

class AgregarProductoATienda(APIView):
    """
    Agregar un producto desde la API externa a una tienda (en tu aplicación normal).
    """
    def post(self, request, *args, **kwargs):
        # Obtener el producto_id y la tienda_id desde la solicitud
        producto_id = request.data.get('producto_id')
        tienda_id = request.data.get('tienda')

        if not producto_id or not tienda_id:
            return Response({"error": "producto_id y tienda son requeridos"}, status=status.HTTP_400_BAD_REQUEST)

        # Verificar si la tienda existe en la base de datos normal (en tu app)
        try:
            tienda = Tienda.objects.get(id=tienda_id)
        except Tienda.DoesNotExist:
            return Response({"error": "Tienda no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        # Obtener el producto desde la API externa
        token = "hydM8WXEPTEjVIm2n8T8BN0nIst7iz"
        url = f"http://127.0.0.1:8000/api/v1/productos/{producto_id}/"
        headers = {"Authorization": f"Bearer {token}"}

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                producto_data = response.json()
                producto_nombre = producto_data['nombre']
                producto_precio = producto_data['precio']

                # Crear o asociar el producto a la tienda
                producto, created = Producto.objects.get_or_create(
                    id=producto_id,
                    defaults={'nombre': producto_nombre, 'precio': producto_precio}
                )

                # Relacionar el producto con la tienda
                tienda.productos.add(producto)  # Esto agregará el producto a la tienda
                tienda.save()

                return Response({"message": "Producto agregado a la tienda correctamente"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "No se pudo obtener el producto desde la API externa"}, status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.RequestException as e:
            return Response({"error": f"Error al hacer la solicitud a la API externa: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
