from django.contrib import admin
from django.utils.html import format_html

from .models import Veiculo, OrdemServico


# Template personalizado da tela de login
admin.site.login_template = 'admin/custom_login.html'


# Mostra as ordens de serviço dentro do veículo
class OrdemServicoInline(admin.TabularInline):

    model = OrdemServico
    extra = 0


# Administração dos veículos
@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):

    # Campos exibidos na lista
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

    # Filtros laterais
    list_filter = (
        'tipo',
        'combustivel',
        'ano',
    )

    # Campo de pesquisa
    search_fields = (
        'marca',
        'modelo',
        'placa',
    )

    # Ordena pelos veículos mais recentes
    ordering = (
        '-data_cadastro',
    )

    # Mostra as ordens de serviço dentro do veículo
    inlines = (
        OrdemServicoInline,
    )


# Administração das ordens de serviço
@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):

    # Ordena pelas ordens mais recentes
    ordering = (
        '-id',
    )