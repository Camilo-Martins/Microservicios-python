from rest_framework import serializers
from .models import*
from dotenv import load_dotenv
from personal.serializers import*
import os

class EmpleadoMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ["id", "nombre_completo"]


class AsignacionSerializer(serializers.ModelSerializer):
    empleado = EmpleadoMiniSerializer(read_only=True)
    class Meta:
        model = AsignacionDia
        fields = ["id", "empleado"]


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