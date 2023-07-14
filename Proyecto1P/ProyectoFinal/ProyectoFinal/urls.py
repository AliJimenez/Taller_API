"""
URL configuration for ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import routers

from empleados.views import agregar_empleado, ver_empleado, editar_empleado, eliminar_empleado, generar_reporte
from quickstart import views
from webapp.views import mostrar_empleados


router = routers.DefaultRouter()
router.register(r'empleados', views.EmpleadoViewSet)
router.register(r'departamentos', views.DepartamentoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar_empleados, name='inicio'),
    path('agregar_empleado/', agregar_empleado),
    path('ver_empleado/<int:idEmpleado>', ver_empleado),
    path('editar_empleado/<int:idEmpleado>', editar_empleado),
    path('eliminar_empleado/<int:idEmpleado>', eliminar_empleado),
    path('generar_reporte/', generar_reporte),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
