🚗 FLEETCARD

Sistema de Gestão e Cadastro de Veículos

Atividade Avaliativa Prática — Grupo 3
Curso: Programador Back-End Python
Unidade Curricular: Desenvolvimento Web com Django
Turma: 2026.2

👥 Equipe — Grupo 3

Integrante

Função

Raphael Farias

Desenvolvedor

Kayke Cansanção

Desenvolvedor

Letícia

Desenvolvedora

Fabiano

Desenvolvedor

GitHub: chavierwebmidia2026-glitch/cadastro_de_veiculos

📌 Sobre o Projeto

O FleetCard é uma aplicação web desenvolvida com Django para cadastro e gerenciamento de veículos.

O sistema permite realizar operações completas de CRUD (Create, Read, Update e Delete) para veículos e também para Ordens de Serviço, mantendo o relacionamento entre cada ordem e seu respectivo veículo.

Além disso, o projeto possui formulário de contatos com persistência no banco de dados, autenticação de usuários, Django Admin personalizado, integração com API e interface responsiva.

✨ Funcionalidades

🚗 CRUD completo de veículos

🛠️ CRUD completo de Ordens de Serviço

🔎 Listagem e consulta de veículos

✏️ Edição de veículos

🗑️ Exclusão de veículos

➕ Cadastro de Ordens de Serviço

✏️ Edição de Ordens de Serviço

🗑️ Exclusão de Ordens de Serviço

🔗 Ordens de Serviço vinculadas aos veículos

📩 Formulário de contatos com armazenamento no banco

🔐 Autenticação de usuários

⚙️ Django Admin personalizado

🌐 Página de veículos integrada com API

📱 Interface responsiva para desktop e mobile

🛠️ Tecnologias

Tecnologia

Versão

Utilização

🐍 Python

3.13.13

Linguagem principal

🌐 Django

6.1.1

Framework web

🗄️ SQLite

—

Banco de dados

🎨 Bootstrap

5.3.3

Interface responsiva

🔹 Bootstrap Icons

1.11.3

Ícones

🔀 Git

—

Controle de versão

☁️ GitHub

—

Repositório e colaboração

🎨 Identidade Visual

Cores principais

Cor

Hexadecimal

Utilização

🔴 Primária

#8A2A22

Botões, navbar e destaques

🟥 Primária escura

#6B1E18

Hover e gradientes

🟡 Dourado

#BE770D

Destaques secundários

🟤 Texto

#2E1B12

Textos principais

🟫 Texto suave

#6B5544

Textos secundários

🟨 Fundo

#FBF1E0

Fundo da página

⚪ Fundo Card

#FFFFFF

Cards e formulários

❌ Danger

#A5342A

Exclusões e erros

✅ Success

#3E7A44

Confirmações

ℹ️ Info

#2E6F73

Informações

⚠️ Warning

#C98A1B

Avisos

Layout

Bordas arredondadas com border-radius: 0.75rem

Cards com sombra e efeito hover

Botões com elevação suave

Navbar e footer com gradiente vermelho-escuro

Layout responsivo utilizando Bootstrap

Tabelas no desktop e adaptação para telas menores

🗄️ Modelos do Banco de Dados

🚗 Veiculo

O modelo Veiculo armazena as informações dos veículos cadastrados.

Campo

Tipo

Descrição

tipo

Choices

Carro, moto ou caminhão

marca

CharField

Marca do veículo

modelo

CharField

Modelo do veículo

placa

Unique

Identificação única

ano

IntegerField

Ano do veículo

cor

CharField

Cor do veículo

combustivel

Choices

Gasolina, etanol, diesel, flex, elétrico, híbrido etc.

quilometragem

IntegerField

Quilometragem atual

observacoes

TextField

Observações adicionais

imagem

ImageField

Foto do veículo

data_cadastro

DateTimeField

Data/hora registrada automaticamente

🛠️ OrdemServico

O modelo OrdemServico representa os serviços realizados nos veículos.

Existe um relacionamento 1 (um para muitos):

Veiculo
   │
   ├── OrdemServico
   ├── OrdemServico
   └── OrdemServico

Isso significa que:

Um veículo pode possuir várias Ordens de Serviço.

Cada Ordem de Serviço fica vinculada a um veículo através do relacionamento definido no modelo.

📩 Contato

O modelo Contato armazena as mensagens enviadas pelo formulário de contato.

Campo

Tipo

Finalidade

nome

CharField

Nome do remetente

email

EmailField

E-mail

telefone

CharField

Telefone opcional

assunto

CharField

Assunto da mensagem

mensagem

TextField

Mensagem enviada

data_envio

DateTimeField

Data/hora automática

🔄 Rotas do Sistema

As rotas abaixo representam as principais funcionalidades do FleetCard.

🚗 CRUD de Veículos

Operação

Método

Rota

Função

➕ Create

POST

/veiculos/cadastrar/

Cadastrar veículo

📋 Read

GET

/veiculos/

Listar veículos

✏️ Update

GET/POST

/veiculos/editar/<id>/

Editar veículo

🗑️ Delete

GET/POST

/veiculos/excluir/<id>/

Excluir veículo

Fluxo do CRUD de Veículos

Cadastrar
   ↓
/veiculos/cadastrar/
   ↓
Veiculo.objects.create()
   ↓
Banco SQLite
   ↓
/veiculos/
   ↓
Listagem

Para edição:

/veiculos/
   ↓
Editar
   ↓
/veiculos/editar/<id>/
   ↓
Veiculo.objects.get()
   ↓
Atualização
   ↓
Banco SQLite

Para exclusão:

/veiculos/
   ↓
Excluir
   ↓
/veiculos/excluir/<id>/
   ↓
Confirmação
   ↓
Veiculo.delete()
   ↓
Banco SQLite

🛠️ CRUD de Ordens de Serviço

As Ordens de Serviço são vinculadas a um veículo.

Operação

Método

Rota

Função

➕ Create

GET/POST

/ordens-servico/cadastrar/<veiculo_id>/

Cadastrar OS para um veículo

📋 Read

GET

/ordens-servico/

Listar todas as OS

📋 Read

GET

/veiculos/<veiculo_id>/ordens-servico/

Listar OS de um veículo

✏️ Update

GET/POST

/ordens-servico/editar/<id>/

Editar OS

🗑️ Delete

GET/POST

/ordens-servico/excluir/<id>/

Excluir OS

Fluxo da Ordem de Serviço

Veículos
   ↓
Selecionar veículo
   ↓
/ordens-servico/cadastrar/<veiculo_id>/
   ↓
Cadastrar serviço
   ↓
OrdemServico
   ↓
Relacionamento com Veiculo
   ↓
Banco SQLite

Consulta das OS de um veículo

/veiculos/<veiculo_id>/ordens-servico/

Essa rota permite visualizar somente as Ordens de Serviço relacionadas ao veículo selecionado.

🌐 Rotas Gerais

Rota

Função

/

🏠 Página inicial

/sobre/

ℹ️ Sobre o projeto

/contatos/

📩 Formulário de contatos

/pagina_veiculos/

🚗 Página de veículos integrada com API

/deslogar/

🔐 Encerrar sessão

/admin/

⚙️ Área administrativa

🔐 Autenticação e Controle de Acesso

O sistema utiliza o sistema de autenticação do Django.

Existem diferentes níveis de acesso às funcionalidades:

Usuário não autenticado
        ↓
Acesso às páginas públicas
        ↓
Login
        ↓
Usuário autenticado
        ↓
Funcionalidades protegidas
        ↓
Django Admin

As funcionalidades administrativas são controladas pelo sistema de autenticação e permissões do Django.

⚙️ Django Admin

O projeto utiliza o Django Admin para administração dos dados.

O administrador pode consultar e gerenciar:

🚗 Veículos

🛠️ Ordens de Serviço

📩 Contatos

O Admin possui personalização visual própria do FleetCard, mantendo uma identidade diferente da área pública do site.

🗂️ Estrutura do Projeto

cadastro_de_veiculos/
│
├── FleetCard/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── forms.py
│   ├── veiculos_api.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── includes/
│   │   │   ├── navbar.html
│   │   │   └── footer.html
│   │   │
│   │   ├── home.html
│   │   ├── sobre.html
│   │   ├── contatos.html
│   │   ├── cadastrar_veiculo.html
│   │   ├── lista_veiculos.html
│   │   ├── editar_veiculo.html
│   │   ├── pagina_veiculos.html
│   │   ├── cadastrar_ordem_servico.html
│   │   ├── lista_ordens_servico.html
│   │   ├── editar_ordem_servico.html
│   │   ├── excluir_ordem_servico.html
│   │   └── ordens_servico_veiculo.html
│   │
│   └── static/
│       └── css/
│
├── config/
│
├── manage.py
├── db.sqlite3
└── requirements.txt

🔗 Arquitetura das Rotas

O funcionamento básico do Django segue o fluxo:

🌐 Navegador
      ↓
🔗 URL
      ↓
👁️ View
      ↓
🧩 Model / ORM
      ↓
🗄️ SQLite
      ↓
📄 Template
      ↓
🌐 Navegador

No CRUD:

Usuário
  ↓
URL
  ↓
View
  ↓
ORM do Django
  ↓
Banco de Dados
  ↓
Template
  ↓
Resultado na tela

🚀 Como Executar o Projeto

1. Clonar o repositório

git clone https://github.com/chavierwebmidia2026-glitch/cadastro_de_veiculos.git

2. Entrar na pasta

cd cadastro_de_veiculos

3. Criar o ambiente virtual

python -m venv venv

4. Ativar o ambiente virtual — Windows

venv\Scripts\activate

5. Instalar as dependências

pip install -r requirements.txt

6. Executar as migrations

python manage.py migrate

7. Criar superusuário

Opcional:

python manage.py createsuperuser

8. Executar o servidor

python manage.py runserver

9. Acessar o sistema

http://127.0.0.1:8000/

Área administrativa:

http://127.0.0.1:8000/admin/

🧪 Principais Operações do Sistema

🚗 Veículos

CREATE → cadastrar
READ   → listar
UPDATE → editar
DELETE → excluir

🛠️ Ordens de Serviço

CREATE → cadastrar OS
READ   → listar OS
UPDATE → editar OS
DELETE → excluir OS

📩 Contatos

Formulário
    ↓
POST
    ↓
View contatos()
    ↓
Contato.objects.create()
    ↓
SQLite
    ↓
Mensagem de sucesso

📱 Responsividade

A interface foi desenvolvida utilizando Bootstrap 5.3.3, permitindo adaptação para diferentes tamanhos de tela.

O projeto considera:

🖥️ Desktop

💻 Notebook

📱 Smartphone

📲 Tablet

Os componentes de navegação, cards, formulários, tabelas e botões foram estruturados para manter a usabilidade em diferentes dispositivos.

🔀 Git e GitHub

O projeto utiliza Git para controle de versão e GitHub para armazenamento e colaboração.

Fluxo utilizado:

feature/*
    ↓
desenvolvimento
    ↓
commit
    ↓
push
    ↓
GitHub
    ↓
develop
    ↓
master

Exemplo de commit:

git add .
git commit -m "feat: implementa CRUD de veículos"
git push

📊 Situação Atual do Projeto

O FleetCard possui atualmente:

✅ Cadastro de veículos

✅ Listagem de veículos

✅ Edição de veículos

✅ Exclusão de veículos

✅ Cadastro de Ordens de Serviço

✅ Listagem de Ordens de Serviço

✅ Edição de Ordens de Serviço

✅ Exclusão de Ordens de Serviço

✅ Relacionamento Veiculo × OrdemServico

✅ Formulário de contatos

✅ Persistência dos contatos no banco

✅ Autenticação

✅ Django Admin personalizado

✅ Integração com API

✅ Interface responsiva

✅ Controle de versão com Git/GitHub

📚 Objetivo Educacional

O projeto foi desenvolvido para aplicar, na prática, conhecimentos de:

Python

Django

Django ORM

SQLite

CRUD

Templates

Views

URLs

Autenticação

Django Admin

Bootstrap

Banco de dados relacional

Git e GitHub

Desenvolvimento web responsivo

📄 Licença

Este projeto foi desenvolvido para fins educacionais, como parte da Atividade Avaliativa Prática do curso Programador Back-End Python, na Unidade Curricular Desenvolvimento Web com Django.

👥 Grupo 3

Raphael Farias • Kayke Cansanção • Letícia • Fabiano

🚗 FleetCard — Sistema de Gestão e Cadastro de Veículos