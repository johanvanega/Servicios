from django.contrib import admin
from.models import Servicio

# Registra modelos aca

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

admin.site.register(Servicio,ServicioAdmin)