from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError

from django.db.models import Q
from .models import Cliente, Veiculo, OrdemServico, Contato
from .forms import VeiculoForm

from .veiculos_api import (
    buscar_carros,
    buscar_motos,
    buscar_caminhoes,
    buscar_imagem,
)



# PÁGINAS


def home(request):
    return render(request, 'home.html')


def sobre(request):
    return render(request, 'sobre.html')


def contatos(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')

        Contato.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            assunto=assunto,
            mensagem=mensagem
        )

        messages.success(
            request,
            'Sua mensagem foi enviada e salva com sucesso!'
        )

        return redirect('contatos')

    return render(
        request,
        'contatos.html'
    )



# API DE VEÍCULOS


def pagina_veiculos(request):

    # Veículos cadastrados no banco de dados
    veiculos = Veiculo.objects.all().order_by('-id')

    # Busca veículos na API
    carros = buscar_carros()[:5]
    motos = buscar_motos()[:5]
    caminhoes = buscar_caminhoes()[:5]

    # Busca imagens dos carros
    for veiculo in carros:
        veiculo["imagem"] = buscar_imagem(
            veiculo["Make_Name"],
            veiculo["Model_Name"],
            "car"
        )

    # Busca imagens das motos
    for veiculo in motos:
        veiculo["imagem"] = buscar_imagem(
            veiculo["Make_Name"],
            veiculo["Model_Name"],
            "moto"
        )

    # Busca imagens dos caminhões
    for veiculo in caminhoes:
        veiculo["imagem"] = buscar_imagem(
            veiculo["Make_Name"],
            veiculo["Model_Name"],
            "caminhao"
        )

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


# LOGOUT


def deslogar(request):

    logout(request)

    return redirect('home')



# DETALHES DO VEÍCULO DA API


def ver_detalhes(request, tipo, marca, modelo):

    nomes_tipos = {
        "car": "Carro",
        "moto": "Moto",
        "caminhao": "Caminhão",
    }

    imagem = buscar_imagem(
        marca,
        modelo,
        tipo
    )

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



# CRUD DE VEÍCULOS


@login_required(login_url='/admin/login/')
def cadastrar_veiculo(request, cliente_id=None):

    # Cliente
    cliente = None

    if cliente_id:
        cliente = get_object_or_404(
            Cliente,
            id=cliente_id
        )

    # Cadastro
    if request.method == 'POST':

        print("POST RECEBIDO")
        print(request.POST)
        print(request.FILES)

        form = VeiculoForm(
        request.POST,
        request.FILES
    )
        if form.is_valid():

            # Cria o veículo
            veiculo = form.save(commit=False)

            # Liga o veículo ao cliente
            if cliente:
                veiculo.cliente = cliente

            # Salva
            veiculo.save()

            messages.success(
                request,
                'Veículo cadastrado com sucesso!'
            )

            # Volta para o cliente
            if cliente:
                return redirect(
                    'detalhe_cliente',
                    cliente_id=cliente.id
                )

            # Volta para a lista
            return redirect(
                'lista_veiculos'
            )

    else:

        # Formulário vazio
        form = VeiculoForm()

    return render(
        request,
        'cadastrar_veiculo.html',
        {
            'form': form,
            'cliente': cliente
        }
    )
@login_required(login_url='/admin/login/')
def lista_veiculos(request):

    pesquisa = request.GET.get(
        'pesquisa',
        ''
    ).strip()

    veiculos = Veiculo.objects.select_related(
        'cliente'
    )

    if pesquisa:

        veiculos = veiculos.filter(

            Q(cliente__nome__icontains=pesquisa) |

            Q(marca__icontains=pesquisa) |

            Q(modelo__icontains=pesquisa) |

            Q(placa__icontains=pesquisa)

        )

    veiculos = veiculos.order_by('-id')

    carros_cadastrados = veiculos.filter(
        tipo='carro'
    )

    motos_cadastrados = veiculos.filter(
        tipo='moto'
    )

    caminhoes_cadastrados = veiculos.filter(
        tipo='caminhao'
    )

    return render(
        request,
        'lista_veiculos.html',
        {
            'carros_cadastrados': carros_cadastrados,
            'motos_cadastrados': motos_cadastrados,
            'caminhoes_cadastrados': caminhoes_cadastrados,
            'pesquisa': pesquisa,
        }
    )


@login_required(login_url='/admin/login/')
def editar_veiculo(request, id):

    veiculo = get_object_or_404(
        Veiculo,
        id=id
    )

    if request.method == 'POST':

        form = VeiculoForm(
            request.POST,
            request.FILES,
            instance=veiculo
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Veículo atualizado com sucesso!'
            )

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

        messages.success(
            request,
            'Veículo excluído com sucesso!'
        )

        return redirect('lista_veiculos')

    return render(
        request,
        'excluir_veiculo.html',
        {
            'veiculo': veiculo
        }
    )



# CRUD DE CLIENTES


@login_required(login_url='/admin/login/')
def cadastrar_cliente(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')

        # Verifica CPF/CNPJ
        if Cliente.objects.filter(
            cpf_cnpj=cpf_cnpj
        ).exists():

            messages.error(
                request,
                'Já existe um cliente cadastrado com este CPF/CNPJ.'
            )

            return render(
                request,
                'cadastrar_cliente.html'
            )

        # Cadastra cliente
        Cliente.objects.create(
            nome=nome,
            cpf_cnpj=cpf_cnpj,
            telefone=telefone,
            email=email,
            endereco=endereco
        )

        messages.success(
            request,
            'Cliente cadastrado com sucesso!'
        )

        return redirect('lista_clientes')

    return render(
        request,
        'cadastrar_cliente.html'
    )


@login_required(login_url='/admin/login/')
def lista_clientes(request):

    clientes = Cliente.objects.all().order_by('nome')

    return render(
        request,
        'lista_clientes.html',
        {
            'clientes': clientes
        }
    )


@login_required(login_url='/admin/login/')
def detalhe_cliente(request, cliente_id):

    # Busca o cliente
    cliente = get_object_or_404(
        Cliente,
        id=cliente_id
    )

    # Busca os veículos do cliente
    veiculos = (
        Veiculo.objects
        .filter(cliente=cliente)
        .prefetch_related('ordens_servico')
        .order_by('-id')
    )

    return render(
        request,
        'detalhe_cliente.html',
        {
            'cliente': cliente,
            'veiculos': veiculos,
        }
    )


@login_required(login_url='/admin/login/')
def editar_cliente(request, id):

    cliente = get_object_or_404(
        Cliente,
        id=id
    )

    if request.method == 'POST':

        cliente.nome = request.POST.get('nome')
        cliente.cpf_cnpj = request.POST.get('cpf_cnpj')
        cliente.telefone = request.POST.get('telefone')
        cliente.email = request.POST.get('email')
        cliente.endereco = request.POST.get('endereco')

        cliente.save()

        messages.success(
            request,
            'Cliente atualizado com sucesso!'
        )

        return redirect('lista_clientes')

    return render(
        request,
        'editar_cliente.html',
        {
            'cliente': cliente
        }
    )

@login_required(login_url='/admin/login/')
def excluir_cliente(request, id):

    cliente = get_object_or_404(
        Cliente,
        id=id
    )

    if request.method == 'POST':

        try:

            cliente.delete()

            messages.success(
                request,
                'Cliente excluído com sucesso!'
            )

            return redirect('lista_clientes')

        except ProtectedError:

            messages.error(
                request,
                'Não é possível excluir este cliente porque existem veículos vinculados a ele.'
            )

            return redirect(
                'detalhe_cliente',
                cliente_id=cliente.id
            )

    return render(
        request,
        'excluir_cliente.html',
        {
            'cliente': cliente
        }
    )


# CRUD DE ORDENS DE SERVIÇO


@login_required(login_url='/admin/login/')
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

        messages.success(
            request,
            'Ordem de serviço cadastrada com sucesso!'
        )

        return redirect('lista_ordens_servico')

    veiculos = Veiculo.objects.select_related(
        'cliente'
    ).all()

    return render(
        request,
        'cadastrar_ordem_servico.html',
        {
            'veiculos': veiculos,
        }
    )


@login_required(login_url='/admin/login/')
def cadastrar_ordem_servico_veiculo(request, veiculo_id):

    # Busca o veículo
    veiculo = get_object_or_404(
        Veiculo,
        id=veiculo_id
    )

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

        messages.success(
            request,
            'Ordem de serviço cadastrada com sucesso!'
        )

        return redirect('lista_ordens_servico')

    return render(
        request,
        'cadastrar_ordem_servico.html',
        {
            'veiculo': veiculo,
            'veiculos': Veiculo.objects.select_related(
                'cliente'
            ).all(),
        }
    )


@login_required(login_url='/admin/login/')
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


@login_required(login_url='/admin/login/')
def lista_ordens_servico(request):

    ordens = OrdemServico.objects.select_related(
        'veiculo',
        'veiculo__cliente'
    ).all().order_by('-id')

    return render(
        request,
        'lista_ordens_servico.html',
        {
            'ordens': ordens,
        }
    )


@login_required(login_url='/admin/login/')
def editar_ordem_servico(request, id):

    ordem = get_object_or_404(
        OrdemServico,
        id=id
    )

    if request.method == 'POST':

        ordem.veiculo_id = request.POST.get('veiculo')
        ordem.tipo_servico = request.POST.get('tipo_servico')
        ordem.descricao = request.POST.get('descricao')
        ordem.status = request.POST.get('status')
        ordem.valor = request.POST.get('valor')

        ordem.save()

        messages.success(
            request,
            'Ordem de serviço atualizada com sucesso!'
        )

        return redirect('lista_ordens_servico')

    veiculos = Veiculo.objects.select_related(
        'cliente'
    ).all()

    return render(
        request,
        'editar_ordem_servico.html',
        {
            'ordem': ordem,
            'veiculos': veiculos,
        }
    )


@login_required(login_url='/admin/login/')
def excluir_ordem_servico(request, id):

    ordem = get_object_or_404(
        OrdemServico,
        id=id
    )

    if request.method == 'POST':

        ordem.delete()

        messages.success(
            request,
            'Ordem de serviço excluída com sucesso!'
        )

        return redirect('lista_ordens_servico')

    return render(
        request,
        'excluir_ordem_servico.html',
        {
            'ordem': ordem,
        }
    )