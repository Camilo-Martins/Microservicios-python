from django.db import models


# Create your models here.
class Nota(models.Model):
    
    admin_id = models.IntegerField(db_index=True)  # dueño / jefe (auth-ms)
    nombre_nota = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_nota
    
    class Meta:
        db_table='notas'
        verbose_name='Notas'
        verbose_name_plural='Notas'