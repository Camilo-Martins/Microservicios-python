from django.urls import path
from .views import*

urlpatterns = [
    path('registro', RegistroUsuario.as_view())
]
