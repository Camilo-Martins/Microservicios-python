"""
URL configuration for authMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view=get_schema_view(
       openapi.Info(
        title="Proyecto tienda ( Python/Django + Vue  + Docker )",
        name="Camilo Martns Oliva",
        description="""
            API Backend para sistema de tienda de barrio con gestión de empleados y horarios, desarrollada con Django y Docker ( Microservicios de Resgistro de usuarios ).

            🔗 Enlaces:
            - GitHub: https://github.com/Camilo-Martins/Microservicios-python
            - LinkedIn: https://www.linkedin.com/in/camilo-martins-oliva/
            - YouTube (demos): https://www.youtube.com/@Camilo-Martins
            """,
        email="camilo.s.martins.oliva@gmail.com",
        default_version='v1',
        terms_of_service="https://opensource.org/licenses/BSD-3-Clause",
        license=openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('register.urls')),

    #rutas swagger
    path('documentacion<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('documentacion/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
