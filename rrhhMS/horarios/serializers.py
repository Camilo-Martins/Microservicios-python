from rest_framework import serializers
from .models import*
from datetime import timedelta, date
from dotenv import load_dotenv
from personal.serializers import*
from django.utils.formats import date_format
from django.core.exceptions import ValidationError
from .utils import horario_utils

import os

class EmpleadoMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ["id", "nombre_completo", "telefono"]


class AsignacionSerializer(serializers.ModelSerializer):
    empleado = EmpleadoMiniSerializer(read_only=True)
    class Meta:
        model = AsignacionDia
        fields = ["id", "empleado", ]


class DiaHorarioSerializer(serializers.ModelSerializer):
    dia_nombre = serializers.CharField(source="get_dia_display")
    asignaciones = AsignacionSerializer(many=True, read_only=True)
    class Meta:
        model = DiaHorario
        fields = ["id", "dia", "dia_nombre", "asignaciones"]


class HorarioSerializer(serializers.ModelSerializer):
    dias = DiaHorarioSerializer(many=True, read_only=True)
    class Meta:
        model = HorarioSemanal
        fields = ("id", "admin_id", "nombre" , "is_active", "fecha_inicio", "fecha_fin", "dias")


class CreateHorarioSerializer(serializers.Serializer):
    admin_id = serializers.CharField(
        required=True,
        allow_blank=False,
    )
 
    def validate_admin_id(self, value):
        if not HorarioSemanal.objects.filter(admid_id=value).exists():
            raise serializers.ValidationError("No tienes los permisos.")
        return value
    

class CreateHorarioSerializer(serializers.Serializer):
    admin_id = serializers.CharField(
        required=True,
        allow_blank=False,
    )
 
class GetHorarioSerializer(serializers.Serializer):
    admin_id = serializers.CharField(
        required=True,
        allow_blank=False,
    )


class AsignarDiaSerializer(serializers.Serializer):
    admin_id = serializers.IntegerField( required=False,  )
    id = serializers.IntegerField(  required=False,  )
    personal = serializers.IntegerField(  required=False, )
    dia = serializers.IntegerField( required=False,   )
    telefono = serializers.IntegerField( required=False,   )

    def validate_asignacion_dia(self,value):
        dia = self.context.get("dia")
        personal = self.context.get("personal")
        existe = AsignacionDia.objects.filter(
                dia=dia,
                empleado=personal
            ).exists()

        if existe:
            raise serializers.ValidationError(
                "El personal ya está asignado a este día."
            )
        
        return existe

    def validate_asignacion(self,value):
        empleado = self.context.get("personal")
        dia = self.context.get("dia")
        asignacion = AsignacionDia.objects.filter(empleado=empleado,dia=dia).exists()
        if asignacion:
            raise serializers.ValidationError("El Personal ya se encuentra asignado.")


        return asignacion