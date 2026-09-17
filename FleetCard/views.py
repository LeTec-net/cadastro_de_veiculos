from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Veiculo, OrdemServico
from .forms import VeiculoForm

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


@login_required(login_url='/admin/login/')
def editar_veiculo(request, id):

    veiculo = Veiculo.objects.get(id=id)

    if request.method == 'POST':

        form = VeiculoForm(
            request.POST,
            request.FILES,
            instance=veiculo
        )

        if form.is_valid():

            form.save()

            return redirect('lista_veiculos')

    else:

        form = VeiculoForm(
            instance=veiculo
        )

    return render(
        request,
        'editar_veiculo.html',
        {
            'form': form,
            'veiculo': veiculo
        }
    )


@login_required(login_url='/admin/login/')
def excluir_veiculo(request, id):

    veiculo = get_object_or_404(
        Veiculo,
        id=id
    )

    if request.method == 'POST':

        veiculo.delete()

        return redirect('lista_veiculos')

    return render(
        request,
        'excluir_veiculo.html',
        {
            'veiculo': veiculo
        }
    )


@login_required(login_url='/admin/login/')
def cadastrar_veiculo(request):

    if request.method == 'POST':

        form = VeiculoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()

            return redirect('lista_veiculos')

    else:

        form = VeiculoForm()

    return render(
        request,
        'cadastrar_veiculo.html',
        {
            'form': form
        }
    )


# crud pelo django admin
@login_required(login_url='/admin/login/')
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


# crud ordem serviço
def cadastrar_ordem_servico(request):
    if request.method == 'POST':
        veiculo_id = request.POST.get('veiculo')
        tipo_servico = request.POST.get('tipo_servico')
        descricao = request.POST.get('descricao')
        status = request.POST.get('status')
        valor = request.POST.get('valor')

        OrdemServico.objects.create(
            veiculo_id=veiculo_id,
            tipo_servico=tipo_servico,
            descricao=descricao,
            status=status,
            valor=valor
        )

        return redirect('lista_ordens_servico')

    veiculos = Veiculo.objects.all()

    return render(
        request,
        'cadastrar_ordem_servico.html',
        {
            'veiculos': veiculos,
        }
    )


def cadastrar_ordem_servico_veiculo(request, veiculo_id):

    veiculo = get_object_or_404(Veiculo, id=veiculo_id)

    if request.method == 'POST':

        tipo_servico = request.POST.get('tipo_servico')
        descricao = request.POST.get('descricao')
        status = request.POST.get('status')
        valor = request.POST.get('valor')

        OrdemServico.objects.create(
            veiculo=veiculo,
            tipo_servico=tipo_servico,
            descricao=descricao,
            status=status,
            valor=valor
        )

        return redirect('lista_ordens_servico')

    return render(
        request,
        'cadastrar_ordem_servico.html',
        {
            'veiculo': veiculo,
            'veiculos': Veiculo.objects.all(),
        }
    )


def ordens_servico_veiculo(request, veiculo_id):

    veiculo = get_object_or_404(
        Veiculo,
        id=veiculo_id
    )

    ordens = OrdemServico.objects.filter(
        veiculo=veiculo
    ).order_by('-id')

    return render(
        request,
        'ordens_servico_veiculo.html',
        {
            'veiculo': veiculo,
            'ordens': ordens,
        }
    )

def lista_ordens_servico(request):

    ordens = OrdemServico.objects.select_related('veiculo').all().order_by('-id')

    return render(
        request,
        'lista_ordens_servico.html',
        {
            'ordens': ordens,
        }
    )




def editar_ordem_servico(request, id):

    ordem = get_object_or_404(OrdemServico, id=id)

    if request.method == 'POST':

        ordem.veiculo_id = request.POST.get('veiculo')
        ordem.tipo_servico = request.POST.get('tipo_servico')
        ordem.descricao = request.POST.get('descricao')
        ordem.status = request.POST.get('status')
        ordem.valor = request.POST.get('valor')

        ordem.save()

        return redirect('lista_ordens_servico')

    veiculos = Veiculo.objects.all()

    return render(
        request,
        'editar_ordem_servico.html',
        {
            'ordem': ordem,
            'veiculos': veiculos,
        }
    )


def excluir_ordem_servico(request, id):

    ordem = get_object_or_404(OrdemServico, id=id)

    if request.method == 'POST':
        ordem.delete()
        return redirect('lista_ordens_servico')

    return render(
        request,
        'excluir_ordem_servico.html',
        {
            'ordem': ordem,
        }
    )