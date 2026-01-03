from django.db import models

class Empleado(models.Model):
 
    admin_id = models.IntegerField(db_index=True)  # dueño / jefe (auth-ms)
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    rol = models.CharField(max_length=100, blank=True, null=True)
   
    is_active = models.BooleanField(default=True)
    
    pago_diario = models.IntegerField(
        help_text="Monto acordado por día trabajado"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Referencia de cuándo comenzaron a trabajar juntos"
    )
   
    def __str__(self):
        return self.nombre_completo
    
    class Meta:
        db_table='empleado'
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        