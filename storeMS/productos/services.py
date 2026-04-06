from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.db import transaction
from .models import*


class ProductoService:
    @staticmethod
    @transaction.atomic

    def get_productos(*, admin_id, proveedor=None, categoria=None):
        productos = Producto.objects.filter(admin_id=admin_id).order_by("-id")

        if proveedor:
            productos = productos.filter(proveedor__nombre_completo__icontains=proveedor)

        if categoria:
            productos = productos.filter(categoria=categoria)

        return productos
    
class NewProductoService:
    @staticmethod
    @transaction.atomic
    def crear_producto(*,admin_id, nombre_producto, descripcion=None, precio=0, categoria=None, proveedor_id=None, stock_actual=0, stock_minimo=0, observaciones=None):

        producto = Producto.objects.create(
            nombre_producto=nombre_producto,
            descripcion=descripcion,
            precio=precio,
            categoria=categoria,
            proveedor_id=proveedor_id,
            stock_actual=stock_actual,
            stock_minimo=stock_minimo,
            observaciones=observaciones,
            is_active=True,
            admin_id=admin_id

        )

        return producto
    

class EditProductoService:
    @staticmethod
    @transaction.atomic
    def editar_producto(*,  admin_id, id, nombre_producto=None, descripcion=None, precio=None, categoria=None, proveedor_id=None,
                        stock_actual=None, stock_minimo=None, observaciones=None, is_active=None):
        
        producto = get_object_or_404(
            Producto,
            admin_id=admin_id,
            id=id,
        )

        producto.nombre_producto = nombre_producto if nombre_producto is not None else producto.nombre_producto
        producto.descripcion = descripcion if descripcion is not None else producto.descripcion
        producto.proveedor_id = proveedor_id if proveedor_id is not None else proveedor_id
        producto.precio = precio if precio is not None else producto.precio
        producto.categoria = categoria if categoria is not None else producto.categoria
        producto.stock_actual = stock_actual if stock_actual is not None else producto.stock_actual
        producto.stock_minimo = stock_minimo if stock_minimo is not None else producto.stock_minimo
        producto.observaciones = observaciones if observaciones is not None else producto.observaciones
        producto.is_active = is_active if is_active is not None else producto.is_active 
        producto.save(update_fields=["nombre_producto", "descripcion", "precio", "categoria", "proveedor_id", "stock_actual",
                                      "stock_minimo", "observaciones", "is_active"])
        
        return producto