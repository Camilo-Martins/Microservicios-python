from rest_framework import serializers
from .models import*
from dotenv import load_dotenv
import os



class DiaHorarioSerializer(serializers.ModelSerializer):
    dia_nombre = serializers.CharField(source="get_dia_display")

    class Meta:
        model = DiaHorario
        fields = ["id", "dia", "dia_nombre"]

class HorarioSerializer(serializers.ModelSerializer):
    dias = DiaHorarioSerializer(many=True, read_only=True)
    class Meta:
        model = HorarioSemanal
        fields = ("id", "admin_id", "nombre" , "is_active", "fecha_inicio", "fecha_fin", "dias")