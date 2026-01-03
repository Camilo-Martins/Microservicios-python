from django.urls import path
from .views import*

urlpatterns = [
    path('registro-empleado', Clasel.as_view()),
]
