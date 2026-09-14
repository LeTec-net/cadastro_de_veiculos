from django.contrib import admin

from .models import Veiculo


# Template personalizado da tela de login do Django Admin
admin.site.login_template = 'admin/custom_login.html'

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'tipo',
        'marca',
        'modelo',
        'placa',
        'ano',
        'cor',
        'combustivel',
        'quilometragem',
        'data_cadastro',
    )

    list_filter = (
        'tipo',
        'combustivel',
        'ano',
    )

    search_fields = (
        'marca',
        'modelo',
        'placa',
    )

    ordering = (
        '-data_cadastro',
    )