from rest_framework import serializers
from .models import*
from dotenv import load_dotenv
import os

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioSemanal
        fields = ("id", "admin_id", "nombre" , "is_active", "fecha_inicio", "fecha_fin")