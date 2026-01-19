from django.urls import path
from .views import*

urlpatterns = [
    path('agregar', RegistroEmpleado.as_view()),
    path('obtener-personal', ObtenerEmpleados.as_view()),
    path('personal-activo', ObtenerEmpleadosActivos.as_view()),
    path('persona/<int:id>', ObtenerEmpleado.as_view()),
    path('desactivar/<int:id>', DesactivarEmpleado.as_view()),
    path('editar/<int:id>', EditarEmpleado.as_view()),
    path('asistencia-empleado/<int:id>', AsistenciaEmpleado.as_view()),
    path('pago-empleado/<int:id>', PagoEmpleado.as_view())
]
