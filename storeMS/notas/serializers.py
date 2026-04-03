from rest_framework import serializers
from django.core.validators import RegexValidator
from models import Nota

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
 
    def validate_admin_id(self, value):
        if not Nota.objects.filter(admin_id=value).exists():
            raise serializers.ValidationError("No tienes los permisos")
        return value


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

    admin_id = serializers.CharField(
        required=True,
        allow_blank=False,
    )

    id = serializers.CharField(
        required=True,
        allow_blank=False,
    )

    def validate_admin_id(self, value):
        if not Nota.objects.filter(admin_id=value).exists():
            raise serializers.ValidationError("No tienes los permisos")
        return value


    def validate_admin(self, value):
        if not Nota.objects.filter(id=value).exists():
            raise serializers.ValidationError("No existe la nota")
        return value
