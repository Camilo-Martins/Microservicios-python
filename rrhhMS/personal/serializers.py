from rest_framework import serializers
from .models import*
from dotenv import load_dotenv
import os
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

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


class NewPersonalSerializer(serializers.Serializer):
    nombre_completo = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )
    telefono = serializers.CharField(
        required=True,
        allow_blank=False,
        min_length=11,
        max_length=11,
        validators=[
        RegexValidator(
            regex=r'^[0-9]+$',
            message="El nombre solo puede contener letras, números y espacios."
        )
    ])
    rol = serializers.CharField(required=False,  allow_blank=True)
    medio_pago = serializers.CharField(required=False, allow_blank=True)
    pago_diario = serializers.CharField(required=False,  allow_blank=True)
    rut = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=13,
    )
	
    def validate_rut(self, value):
        if Empleado.objects.filter(rut=value).exists():
            raise serializers.ValidationError("Personal ya existe.")
        return value


    def validate_telefono(self, value):
        if Empleado.objects.filter(telefono=value).exists():
            raise serializers.ValidationError("Personal ya existe.")
        return value

#Cambia el estado de activado/desactivado
class SetPersonalSerializer(serializers.Serializer):
    admin_id = serializers.CharField(
        required=True,
        allow_blank=False,
    )
    id = serializers.CharField(
        required=True,
        allow_blank=False,
    )

    def validate_admin_id(self, value):
        if not Empleado.objects.filter(admin_id=value).exists():
            raise serializers.ValidationError("No tienes los permisos")
        return value


    def validate_admin(self, value):
        if not Empleado.objects.filter(id=value).exists():
            raise serializers.ValidationError("No existe la persona")
        return value
    


class GetPersonalListSerializer(serializers.Serializer):
    admin_id = serializers.CharField(
        required=True,
        allow_blank=False,
    )
 
    def validate_admin_id(self, value):
        if not Empleado.objects.filter(admin_id=value).exists():
            raise serializers.ValidationError("No tienes eres admin")
        return value


class PersonalActiveSerializer(serializers.Serializer):
    admin_id = serializers.CharField(
        required=True,
        allow_blank=False,
    )
    id = serializers.CharField(required=False, allow_blank=True)
    rol = serializers.CharField(required=False, allow_blank=True)
    nombre_completo = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = Empleado
        fields = ["id", "nombre_completo", "rol", "admin_id"]


class GetPersonalSerializer(serializers.Serializer):
    admin_id = serializers.CharField(
        required=True,
        allow_blank=False,
    )
    id = serializers.CharField(
        required=True,
        allow_blank=False,
    )

    def validate_admin_id(self, value):
        if not Empleado.objects.filter(admin_id=value).exists():
            raise serializers.ValidationError("No tienes eres admin")
        return value
    
    def validate_id(self, value):
        if not Empleado.objects.filter(id=value).exists():
            raise serializers.ValidationError("No tienes eres admin")
        return value 
    


class EditPersonalSerializer(serializers.Serializer):
    nombre_completo = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )
    telefono = serializers.CharField(
        required=True,
        allow_blank=False,
        min_length=11,
        max_length=11,
        validators=[
        RegexValidator(
            regex=r'^[0-9]+$',
            message="El nombre solo puede contener letras, números y espacios."
        )
    ])
    rol = serializers.CharField(required=False,  allow_blank=True)
    medio_pago = serializers.CharField(required=False, allow_blank=True)
    pago_diario = serializers.CharField(required=False,  allow_blank=True)
    rut = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=13,
    )
	
    def validate_rut(self, value):
        id = self.context.get("id")
        if Empleado.objects.filter(rut=value).exclude(id=id).exists():
            raise serializers.ValidationError("Personal ya existe.")
        return value
    
    def validate_telefono(self, value):
        id = self.context.get("id")
        if Empleado.objects.filter(telefono=value).exclude(id=id).exists():
            raise serializers.ValidationError("Personal ya existe.")
        return value