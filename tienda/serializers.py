from rest_framework import serializers
from .models import *

class ProductoTerceroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosTerceros
        fields = '__all__'
        
                
class ProductoTerceroCreateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ProductosTerceros
        fields = '__all__'