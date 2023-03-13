from django.contrib import admin
from gerencia import forms, models

@admin.register(models.ModeloForm)

class FormularioAdmin(admin.ModelAdmin):
    form = forms.DjangoForm