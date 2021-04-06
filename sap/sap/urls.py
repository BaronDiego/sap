"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from personas.views import detalleDomicilio, detallePersona, editarDomicilio, editarPersona, eliminarDomicilio, eliminarPersona, listadoDomicilios, nuevaPersona, nuevoDomicilio
from webapp.views import index
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('detalle_persona/<int:id>', detallePersona, name='detalle_persona'),
    path('nueva_persona/', nuevaPersona, name='nueva_persona'),
    path('editar_persona/<int:id>', editarPersona, name='editar_persona'),
    path('eliminar_persona/<int:id>', eliminarPersona, name='eliminar_persona'),
    path('domicilios/', listadoDomicilios, name='domicilios'),
    path('nuevo_domicilio/', nuevoDomicilio, name='nuevo_domicilio'),
    path('editar_domicilio/<int:id>', editarDomicilio, name='editar_domicilio'),
    path('detalle_domicilio/<int:id>', detalleDomicilio, name='detalle_domicilio'),
    path('elimiar_domicilio/<int:id>', eliminarDomicilio, name='eliminar_domicilio')

]
