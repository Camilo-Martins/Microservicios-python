from django.db import models


# Create your models here.
class Proveedor(models.Model):
    
    admin_id = models.IntegerField(db_index=True)  # dueño / jefe (auth-ms)
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=20, blank=True, null=True)
    rut = models.CharField(max_length=12, blank=True, null=True)
    nombre_empresa = models.CharField(max_length=150, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo
    
    class Meta:
        db_table='proveedores'
        verbose_name='Proveedores'
        verbose_name_plural='Proveedores'