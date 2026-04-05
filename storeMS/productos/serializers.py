from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    
    admin_id = serializers.CharField(
        required=True,
        allow_blank=False,
    )

    class Meta:
        model = Producto
        fields = '__all__'

class NewProductoSerializer(serializers.Serializer):
    
    nombre_producto = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'required': 'El nombre del producto es requerido.',
            'blank': 'El nombre del producto no puede estar vacío.',
        },
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    descripcion = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=500,
    )

    precio = serializers.DecimalField(
        required=True,
        max_digits=10,
        decimal_places=2,
        error_messages={
            'required': 'El precio es obligatorio.',
            'invalid': 'Ingrese un precio válido.',
        }
    )

    stock_minimo = serializers.IntegerField(
        required=False,
        min_value=0,
        error_messages={
            'required': 'El stock es obligatorio.',
            'invalid': 'Ingrese un número entero válido para el stock.',
            'min_value': 'El stock no puede ser negativo.',
        }
    )

    stock_actual = serializers.IntegerField(
        required=False,
        min_value=0,
        error_messages={
            'required': 'El stock es obligatorio.',
            'invalid': 'Ingrese un número entero válido para el stock.',
            'min_value': 'El stock no puede ser negativo.',
        }
    )

    proveedor_id = serializers.IntegerField(
        required=True,
        error_messages={
            'required': 'El proveedor es obligatorio.',
            'invalid': 'Ingrese un ID de proveedor válido.',
        }
    )

    categoria_id = serializers.IntegerField(
        required=False,
        error_messages={
            'invalid': 'Ingrese un ID de categoría válido.',
        }
    )

    observaciones = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    is_active = serializers.BooleanField(required=False, allow_null=False)

class EditarProductoSerializer(NewProductoSerializer):
    
    nombre_producto = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'required': 'El nombre del producto es requerido.',
            'blank': 'El nombre del producto no puede estar vacío.',
        },
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    descripcion = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=500,
    )

    precio = serializers.DecimalField(
        required=True,
        max_digits=10,
        decimal_places=2,
        error_messages={
            'required': 'El precio es obligatorio.',
            'invalid': 'Ingrese un precio válido.',
        }
    )

    stock_minimo = serializers.IntegerField(
        required=False,
        min_value=0,
        error_messages={
            'required': 'El stock es obligatorio.',
            'invalid': 'Ingrese un número entero válido para el stock.',
            'min_value': 'El stock no puede ser negativo.',
        }
    )

    stock_actual = serializers.IntegerField(
        required=False,
        min_value=0,
        error_messages={
            'required': 'El stock es obligatorio.',
            'invalid': 'Ingrese un número entero válido para el stock.',
            'min_value': 'El stock no puede ser negativo.',
        }
    )

    proveedor_id = serializers.IntegerField(
        required=True,
        error_messages={
            'required': 'El proveedor es obligatorio.',
            'invalid': 'Ingrese un ID de proveedor válido.',
        }
    )

    categoria_id = serializers.IntegerField(
        required=False,
        error_messages={
            'invalid': 'Ingrese un ID de categoría válido.',
        }
    )

    observaciones = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ]+$',
                message="El nombre solo puede contener letras, números y espacios."
            )
        ]
    )

    is_active = serializers.BooleanField(required=False, allow_null=False)
