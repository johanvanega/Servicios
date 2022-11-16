from django.contrib import admin
from .models import Categoria,post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

class postAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(post,postAdmin)