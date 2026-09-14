from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required

from .models import Veiculo

from .veiculos_api import (
    buscar_carros,
    buscar_motos,
    buscar_caminhoes,
    buscar_imagem,
)


# HOME

def home(request):
    return render(request, 'home.html')


# SOBRE

def sobre(request):
    return render(request, 'sobre.html')


# CONTATOS

def contatos(request):
    return render(request, 'contatos.html')


# API DE VEICULOS

def pagina_veiculos(request):

    # Veiculos cadastrados no banco pelo Admin
    veiculos = Veiculo.objects.all().order_by('-id')

    # Veiculos recebidos da API
    carros = buscar_carros()[:5]
    motos = buscar_motos()[:5]
    caminhoes = buscar_caminhoes()[:5]

    # Imagens dos carros
    for veiculo in carros:
        veiculo["imagem"] = buscar_imagem(
            veiculo["Make_Name"],
            veiculo["Model_Name"],
            "car"
        )

    # Imagens das motos
    for veiculo in motos:
        veiculo["imagem"] = buscar_imagem(
            veiculo["Make_Name"],
            veiculo["Model_Name"],
            "moto"
        )

    # Imagens dos caminhoes
    for veiculo in caminhoes:
        veiculo["imagem"] = buscar_imagem(
            veiculo["Make_Name"],
            veiculo["Model_Name"],
            "caminhao"
        )

    # Envia os dados para a pagina
    contexto = {
        "veiculos": veiculos,
        "carros": carros,
        "motos": motos,
        "caminhoes": caminhoes,
    }

    return render(
        request,
        "pagina_veiculos.html",
        contexto
    )



# DESLOGAR E VOLTAR PARA HOME

def deslogar(request):

    logout(request)

    return redirect('home')


# DETALHES DO VEICULO DA API

def ver_detalhes(request, tipo, marca, modelo):

    nomes_tipos = {
        "car": "Carro",
        "moto": "Moto",
        "caminhao": "Caminhão",
    }

    # Busca a imagem
    imagem = buscar_imagem(
        marca,
        modelo,
        tipo
    )

    # Dados do veiculo
    veiculo = {
        "marca": marca,
        "modelo": modelo,
        "tipo": nomes_tipos.get(tipo, "Veículo"),
        "imagem": imagem,
    }

    return render(
        request,
        "ver_detalhes.html",
        {
            "veiculo": veiculo
        }
    )



# crud pelo django admin



@staff_member_required(login_url='/admin/login/')
def lista_veiculos(request):

    # READ - carros cadastrados
    carros_cadastrados = Veiculo.objects.filter(
        tipo='carro'
    ).order_by('-id')

    # READ - motos cadastradas
    motos_cadastrados = Veiculo.objects.filter(
        tipo='moto'
    ).order_by('-id')

    # READ - caminhoes cadastrados
    caminhoes_cadastrados = Veiculo.objects.filter(
        tipo='caminhao'
    ).order_by('-id')

    return render(
        request,
        'lista_veiculos.html',
        {
            'carros_cadastrados': carros_cadastrados,
            'motos_cadastrados': motos_cadastrados,
            'caminhoes_cadastrados': caminhoes_cadastrados,
        }
    )