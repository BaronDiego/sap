from django.contrib import admin
from .models import Persona, Domicilio

# Register your models here.

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email']


@admin.register(Domicilio)
class DomicilioAdmin(admin.ModelAdmin):
    list_display = ['calle', 'no_calle', 'pais']
