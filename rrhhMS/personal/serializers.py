from rest_framework import serializers
from .models import*
from dotenv import load_dotenv
import os

class EmpleadoSerializer(serializers.ModelSerializer):
   
    created_at = serializers.DateTimeField(format="%d/%m/%Y")#13/10/2025
     
    class Meta:
        model = Empleado
        fields = ("id", "admin_id", "nombre_completo", "telefono", "rut","medio_pago",
                  "rol", "is_active", "pago_diario", "created_at")
        

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ["id", "fecha", "asistio"]

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ["id", "fecha", "monto"]
