from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.db import transaction
from ..models import*
from horarios.models import*

REQUIRED_FIELDS = [
    "nombre_completo",
    "telefono",
    "rol",
    "pago_diario",
    "rut",
]

# services/empleado_service.py

   
class PersonalService:
    @staticmethod
    @transaction.atomic
    def obtener_empleado(*, admin_id, id):
    
        empleado = get_object_or_404(
            Empleado,
            admin_id=admin_id,
            id=id
        )

        asistencias = Asistencia.objects.filter(empleado=empleado)
        pagos = Pago.objects.filter(empleado=empleado)

        return empleado, asistencias, pagos

class NewPersonalService:
    @staticmethod
    @transaction.atomic
    def crear_empleado(*,admin_id, nombre_completo, telefono, rol, rut, pago_diario, medio_pago):

        if not pago_diario or pago_diario == None:
            pago_diario = 0

        personal = Empleado.objects.create(
            nombre_completo=nombre_completo,
            telefono=telefono,
            rol=rol,
            pago_diario=pago_diario,
            rut=rut,
            medio_pago=medio_pago,
            is_active=True,
            admin_id=admin_id
        )

        return personal


class SetPerfilService:
    staticmethod
    @transaction.atomic
    def desactivar_empleado(*, admin_id, id):
        
        empleado = get_object_or_404(
        Empleado,
            admin_id=admin_id,
            id=id
        )

        empleado.is_active = not empleado.is_active
        empleado.save(update_fields=["is_active"])

        return empleado.is_active

class PersonalListService:
    staticmethod
    @transaction.atomic
    def obtener_empleados_por_admin(*, admin_id):
        
        personalList = Empleado.objects.filter(admin_id=admin_id).order_by("id")
        return personalList
  

class PersonalActiveListService:
    staticmethod
    @transaction.atomic
    def obtener_empleados_por_admin(*, admin_id):
        
        personalList = Empleado.objects.filter(admin_id=admin_id, is_active=True ).order_by("id")
        return personalList
  


class EditPersonalService:
    @staticmethod
    @transaction.atomic
    def editar_empleado(*, admin_id, id, nombre_completo, telefono, rol, pago_diario, rut, medio_pago):
    
        empleado = get_object_or_404(
            Empleado,
            admin_id=admin_id,
            id=id
        )
    
        if not pago_diario or pago_diario == None:
            pago_diario = 0

        empleado.nombre_completo=nombre_completo
        empleado.telefono=telefono
        empleado.rol=rol
        empleado.pago_diario=pago_diario
        empleado.rut=rut
        empleado.medio_pago=medio_pago
        empleado.admin_id=admin_id
        empleado.save(update_fields=["nombre_completo", "telefono", "rol", "pago_diario", "rut", "medio_pago"])

        return empleado



def asistencia_empleado(admin_id, id, data):

    horario = get_object_or_404(
        HorarioSemanal,
        admin_id=admin_id,
        id=id
    )

    empleado = get_object_or_404(
        Empleado,
        admin_id=admin_id,
        id=data["empleado_id"]
    )

    fecha_asistencia = horario.fecha_inicio + timedelta(days=data["dia"] - 1)

    return Asistencia.objects.create(
        empleado=empleado, 
        asistio = data["asistencia"],
        fecha = fecha_asistencia)


def pago_empleado(admin_id, id, data):

    horario = get_object_or_404(
        HorarioSemanal,
        admin_id=admin_id,
        id=id
    )
    
    fecha_pago = horario.fecha_inicio + timedelta(days=data["dia"] - 1)

    asistencia = get_object_or_404(
        Asistencia,
        id=data["asistencia_id"],
        empleado_id=data["empleado_id"],
        asistio=1
    )
    
    empleado = get_object_or_404(
        Empleado,
        id=data["empleado_id"]
    )

    return Pago.objects.create(
            empleado=empleado, 
            pagado = data["pagado"],
            monto = data["monto"],
            fecha = fecha_pago)

