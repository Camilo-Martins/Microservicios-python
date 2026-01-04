from rest_framework import serializers
from .models import*
from dotenv import load_dotenv
import os

class EmpleadoSerializer(serializers.ModelSerializer):
   
    created_at = serializers.DateTimeField(format="%d/%m/%Y")#13/10/2025
     
    class Meta:
        model = Empleado
        fields = ("id", "admin_id", "nombre_completo", "telefono", 
                  "rol", "is_active", "pago_diario", "created_at")