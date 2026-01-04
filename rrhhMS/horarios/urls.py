from django.urls import path
from .views import*

urlpatterns = [
    path('obtener-horarios', Clasel.as_view()),
    path('obtener-horario/<int:id>', Clasel.as_view()),
    path('nuevo-horario', Clasel.as_view()),
    path('desactivar-horario/<int:id>', Clasel.as_view()),
]
