from django.urls import path
from .views import*

urlpatterns = [
    path('registro', RegistroUsuario.as_view()),
    path('confirmar-cuenta/<str:token>', ValidarCuenta.as_view()),
    path('login', Login.as_view()),
    path('recuperar-password', RecuperarPassword.as_view()),
    path('cambiar-password/<str:token>', CambiarPassword.as_view())
]
