from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import Nota

#Serializer para obtener notas
class NotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nota
        fields = ("id", "admin_id", "nombre_nota", "is_active", "observaciones", "created_at")

class ObtenerNotasSerializer(serializers.Serializer):
    admin_id = serializers.CharField(
        required=True,
        allow_blank=False,
    )
    id = serializers.CharField(required=False, allow_blank=True)
    nombre_nota = serializers.CharField(required=False, allow_blank=True)
    is_active = serializers.BooleanField(required=False)
    observaciones = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = Nota
        fields = ("id", "admin_id", "nombre_nota", "is_active", "observaciones", "created_at")

# Seralizer para crear una nueva nota
class NewNotaSerializer(serializers.Serializer):

    nombre_nota = serializers.CharField(
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

    observaciones = serializers.CharField(
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

# Seralizer para editar una nota existente  
class EditNotaSerializer(serializers.Serializer):

    nombre_nota = serializers.CharField(
        required=False,
        allow_blank=False,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    observaciones = serializers.CharField(
        required=False,
        allow_blank=False,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    is_active = serializers.BooleanField(required=False, allow_null=False)