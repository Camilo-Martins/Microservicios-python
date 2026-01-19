from django.urls import path
from .views import*

urlpatterns = [
    path('obtener-horarios', ObtenerHorarios.as_view()),
    path('obtener-horario', ObtenerHorario.as_view()),
    path('crear', CrearHorario.as_view()),
    path('desactivar-horario/<int:id>', DesactivarHorario.as_view()),
    path('asignacion-empleados/<int:id>', AsignarSemana.as_view()),
]
