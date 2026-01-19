from datetime import timedelta, date
from personal.serializers import*
from django.utils.formats import date_format

def calcular_semana_actual():
    
    fecha_inicio = date.today()
    fecha_fin = fecha_inicio + timedelta(days=7)
    
    inicio_str = date_format(fecha_inicio, "d/m/Y")
    fin_str = date_format(fecha_fin, "d/m/Y")

    nombre = f"Horario semana {inicio_str} - {fin_str}"
    return fecha_inicio, fecha_fin, nombre
