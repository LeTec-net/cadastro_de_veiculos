blioteca
/
projeto integrador FleetCard
/
README_FleetCard_FORMATADO_COMPLETO.md


🚗 FleetCard
🚘 Sistema de Gestão e Cadastro de Veículos
Projeto Integrador — Programador Back-End Python

Unidade Curricular: Desenvolvimento Web com Django
Turma: 2026.2
Grupo: Grupo 3

👨‍💻 Integrantes
Raphael Farias

Kayke Cansanção

Letícia

Fabiano

🔗 Repositório
GitHub — cadastro_de_veiculos

📖 Sobre o Projeto
O FleetCard é um sistema web desenvolvido em Python e Django com o objetivo de realizar o cadastro, consulta e gerenciamento de veículos.

O sistema trabalha com diferentes tipos de veículos:

🚗 Carros

🏍️ Motocicletas

🚚 Caminhões

O projeto foi desenvolvido a partir do cenário da Oficina Mecânica AutoPrime, utilizado como situação de aprendizagem. Entretanto, o FleetCard foi estruturado como uma solução genérica para oficinas mecânicas, podendo ser adaptado a diferentes estabelecimentos.

A aplicação utiliza Django ORM, SQLite, Bootstrap 5, Bootstrap Icons e Django Admin.

📋 Situação de Aprendizagem
O gerenciamento de veículos pode envolver diversas informações, como tipo, marca, modelo, placa, ano, cor, combustível, quilometragem, observações e histórico de serviços.

Quando essas informações são armazenadas de maneira manual ou desorganizada, podem ocorrer dificuldades para localizar dados, atualizar registros e acompanhar os veículos.

Diante dessa necessidade, foi proposta uma aplicação web capaz de centralizar essas informações em um único sistema.

O FleetCard utiliza Python, Django e SQLite no desenvolvimento do sistema e Bootstrap 5 na construção da interface responsiva.

🎯 Desafio
Desenvolver um sistema web denominado FleetCard, permitindo realizar o cadastro, consulta, atualização e exclusão de veículos de forma organizada.

O sistema possui como objetivos:

📝 Cadastro de veículos;

🔎 Consulta de veículos;

📋 Listagem;

👁️ Visualização dos detalhes;

✏️ Edição;

🗑️ Exclusão;

🏷️ Classificação por tipo;

🔧 Controle de Ordens de Serviço;

🔐 Administração pelo Django Admin;

📱 Interface responsiva.

🛠️ Tecnologias
Tecnologia	Utilização
🐍 Python	Linguagem principal
🌐 Django	Framework web
🗄️ Django ORM	Comunicação com o banco
💾 SQLite	Banco de dados
🎨 Bootstrap 5	Interface responsiva
🔣 Bootstrap Icons	Ícones da interface
📄 Django Templates	Estrutura das páginas
🖥️ HTML5	Estrutura
🎨 CSS3	Personalização visual
⚡ JavaScript	Interações da interface
🌿 Git	Controle de versão
🐙 GitHub	Repositório
📦 Funcionalidades
🚘 Veículos
O sistema permite trabalhar com:

🚗 Carros;

🏍️ Motocicletas;

🚚 Caminhões.

O cadastro de veículos utiliza os seguintes campos:

Campo	Descrição
Tipo	Tipo do veículo
Marca	Marca do veículo
Modelo	Modelo
Placa	Identificação única
Ano	Ano do veículo
Cor	Cor
Combustível	Tipo de combustível
Quilometragem	Quilometragem atual
Observações	Informações adicionais
Imagem	Imagem opcional
Data de cadastro	Data e hora do cadastro
⛽ Combustíveis disponíveis
Gasolina

Etanol

Diesel

Flex

Elétrico

Híbrido

🔧 Ordens de Serviço
O FleetCard possui o modelo OrdemServico, relacionado diretamente ao veículo.

Um veículo pode possuir várias ordens de serviço.

Tipos de serviço
Troca de óleo

Revisão

Sistema de freios

Suspensão

Motor

Elétrica

Pneus

Outros

Status
Aguardando

Em andamento

Concluído

Cancelado

A data de conclusão é controlada automaticamente pelo sistema quando a Ordem de Serviço passa para o status Concluído.

🔐 Django Admin
O Django Admin é utilizado para o gerenciamento administrativo dos registros.

O cadastro de veículos permite:

Visualizar;

Cadastrar;

Editar;

Excluir;

Pesquisar;

Filtrar;

Ordenar registros.

🔎 Pesquisas
Marca;

Modelo;

Placa.

🔽 Filtros
Tipo;

Combustível;

Ano.

🔧 Ordens de Serviço
As Ordens de Serviço são exibidas dentro do cadastro do veículo por meio de Inline Admin.

Acesso
/admin/
Para criar um usuário administrador:

python manage.py createsuperuser
🧭 Páginas e URLs
Página	URL
🏠 Home	/
ℹ️ Sobre	/sobre/
📞 Contatos	/contatos/
🚗 Veículos	/pagina_veiculos/
📄 Detalhes	/pagina_veiculos/detalhes/<tipo>/<marca>/<modelo>/
📋 Lista de veículos	/veiculos/
🔐 Administração	/admin/
🚪 Deslogar	/deslogar/
O gerenciamento administrativo de criação, edição e exclusão dos veículos é realizado pelo Django Admin.

☰ Sidebar Responsiva
A navegação utiliza o componente Offcanvas do Bootstrap.

O menu foi desenvolvido para funcionar em:

💻 Computadores;

💻 Notebooks;

📱 Tablets;

📱 Smartphones.

A estrutura de navegação contempla as principais áreas do sistema, incluindo Home, Veículos, Cadastro, Lista, Contatos, Sobre e Administração.

🎨 Interface
A interface utiliza Bootstrap 5 e Bootstrap Icons, complementados pelo CSS próprio do FleetCard.

A identidade visual utiliza principalmente:

Elemento	Cor
Vermelho principal	#8A2A22
Vermelho escuro	#6B1E18
Dourado	#BE770D
Fundo principal	#FBF1E0
Fundo de seção	#F4E6CC
Texto principal	#2E1B12
A aplicação possui:

Navbar;

Logo FleetCard;

Menu hambúrguer;

Sidebar Offcanvas;

Footer;

Carrossel na Home;

Seção Hero;

Cards;

Layout responsivo;

Personalização visual própria.

🗄️ Banco de Dados
O projeto utiliza SQLite durante o desenvolvimento.

A comunicação entre os modelos e o banco é realizada pelo Django ORM.

Fluxo
Model
  ↓
Django ORM
  ↓
Migration
  ↓
SQLite
Comandos principais
python manage.py makemigrations
python manage.py migrate
🔄 CRUD
O sistema utiliza as operações fundamentais de CRUD:

CREATE
  ↓
READ
  ↓
UPDATE
  ↓
DELETE
Create
Cadastro de veículos.

Read
Listagem e visualização dos dados.

Update
Atualização das informações.

Delete
Exclusão dos registros.

No projeto atual, o gerenciamento administrativo do CRUD de veículos é realizado pelo Django Admin.

📁 Estrutura do Projeto
cadastro_de_veiculos/
│
├── FleetCard/
│   ├── migrations/
│   ├── static/
│   │   └── js/
│   │       └── script.js
│   ├── templates/
│   │   ├── admin/
│   │   │   ├── custom_login.html
│   │   │   └── meu_admin.html
│   │   ├── includes/
│   │   │   ├── footer.html
│   │   │   └── navbar.html
│   │   ├── base.html
│   │   ├── cadastrar_veiculo.html
│   │   ├── contatos.html
│   │   ├── home.html
│   │   ├── lista_veiculos.html
│   │   ├── pagina_veiculos.html
│   │   ├── sobre.html
│   │   ├── test_base.html
│   │   └── ver_detalhes.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
│   └── veiculos/
│
├── static/
├── db.sqlite3
├── manage.py
└── requirements.txt
🧩 Template Base
O projeto utiliza herança de templates.

O arquivo principal é:

FleetCard/templates/base.html
A estrutura compartilhada inclui:

Navbar;

Conteúdo principal;

Footer;

Bootstrap;

Bootstrap Icons;

CSS;

JavaScript.

As páginas utilizam o conceito de herança do Django Templates.

Exemplo
{% extends 'base.html' %}
🖼️ Imagens e Arquivos de Mídia
As imagens enviadas dos veículos são armazenadas no diretório:

media/veiculos/
A configuração utiliza:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
Durante o desenvolvimento, as URLs de mídia são disponibilizadas pelo config/urls.py.

🌐 Integração com API
A página de veículos utiliza dados obtidos por APIs externas para apresentar informações de veículos.

A implementação está organizada no arquivo:

FleetCard/veiculos_api.py
Os dados são organizados por:

🚗 Carros;

🏍️ Motocicletas;

🚚 Caminhões.

As informações são apresentadas na interface através de cards Bootstrap.

📚 Funcionalidades Complementares
A documentação do projeto prevê a evolução do FleetCard para recursos adicionais:

🏷️ Marcas;

🗂️ Categorias;

⛽ Combustíveis;

🎨 Cores;

🔧 Manutenção;

🔄 Revisões;

🛣️ Quilometragem;

📑 Documentação;

📊 Relatórios.

Esses recursos representam a evolução planejada do sistema e não devem ser considerados funcionalidades independentes já implementadas enquanto não houver sua implementação no código.

🧪 Regras de Negócio
A placa do veículo deve ser única.

O tipo do veículo utiliza opções previamente definidas.

A quilometragem possui valor padrão 0.

Observações são opcionais.

A imagem do veículo é opcional.

Um veículo pode possuir várias Ordens de Serviço.

Uma Ordem de Serviço pertence a um veículo.

Quando uma Ordem de Serviço é concluída, a data de conclusão é registrada automaticamente.

Quando o status deixa de ser concluído, a data de conclusão é removida.

🚀 Como Executar o Projeto
1. Clonar o repositório
git clone https://github.com/chavierwebmidia2026-glitch/cadastro_de_veiculos.git
2. Entrar na pasta
cd cadastro_de_veiculos
3. Criar ambiente virtual
No Windows:

python -m venv .venv
4. Ativar o ambiente virtual
Git Bash:

source .venv/Scripts/activate
PowerShell:

.venv\Scripts\Activate.ps1
5. Instalar as dependências
python -m pip install -r requirements.txt
6. Aplicar as migrations
python manage.py migrate
7. Criar superusuário
python manage.py createsuperuser
8. Executar o servidor
python manage.py runserver
9. Acessar no navegador
http://127.0.0.1:8000/

Para o Django Admin:

http://127.0.0.1:8000/admin/

🌿 Controle de Versão
O desenvolvimento utiliza Git e GitHub.

Estrutura utilizada no desenvolvimento:

master
  │
  ├── develop
  │
  ├── feature/sidebar
  ├── feature/carousel
  ├── feature/pagina_veiculos
  ├── feature/api-veiculos
  ├── feature/crud-veiculos
  └── feature/stylizar_css_admin_Django
As funcionalidades são desenvolvidas em branches específicas e posteriormente integradas ao fluxo principal do projeto.

📌 Status do Projeto
🟢 Implementado
Estrutura Django;

Aplicação FleetCard;

Templates;

base.html;

Navbar;

Footer;

Bootstrap 5;

Bootstrap Icons;

CSS personalizado;

Sidebar Offcanvas;

Menu hambúrguer;

Carrossel da Home;

Hero da Home;

Páginas Home, Sobre e Contatos;

Página de veículos;

Página de detalhes;

Modelo Veiculo;

Banco SQLite;

Django ORM;

Django Admin;

Filtros e pesquisas no Admin;

Modelo OrdemServico;

Ordens de Serviço relacionadas ao veículo;

Upload de imagens;

Integração com API de veículos;

Controle de acesso às opções administrativas.

🔄 Em evolução
Aprimoramento da interface;

Melhorias na apresentação dos veículos;

Melhorias no controle administrativo;

Refinamento da documentação;

Testes e ajustes finais.

📋 Planejado
Marcas;

Categorias;

Controle de documentação;

Controle de revisões;

Controle de quilometragem;

Relatórios;

Melhorias no Dashboard;

Novas funcionalidades de manutenção.

🎓 Projeto Integrador
O FleetCard tem como finalidade aplicar, de forma prática, os conhecimentos desenvolvidos durante a formação em programação Back-End com Python e Django.

O projeto utiliza conceitos de:

Desenvolvimento Web;

Django;

ORM;

Banco de dados;

CRUD;

Templates;

Bootstrap;

Django Admin;

APIs;

Git e GitHub.

A documentação acompanha a evolução do projeto, registrando sua estrutura, tecnologias, funcionalidades, requisitos e planejamento.

🏁 Conclusão
O FleetCard propõe uma solução web para centralizar o cadastro e gerenciamento de veículos.

A utilização de Python, Django, ORM, SQLite, Bootstrap e Django Admin proporciona uma estrutura organizada e responsiva.

O sistema trabalha com carros, motocicletas e caminhões e possui suporte ao gerenciamento de Ordens de Serviço.

A arquitetura permite que novas funcionalidades sejam adicionadas futuramente, incluindo manutenção, revisões, documentação, quilometragem e relatórios.

🚗 FleetCard
Organização, controle e gestão de veículos em um único sistema.

📌 Projeto
Informação	Detalhes
🚗 Projeto	FleetCard
📚 Tipo	Projeto Integrador
🎓 Curso	Programação em Back-end Python
📖 UC	Desenvolvimento Web com Django
💻 Área	Desenvolvimento Web
🐍 Backend	Python + Django
🗄️ Banco de Dados	SQLite
🎨 Frontend	HTML5 + CSS3 + Bootstrap 5
🔐 Administração	Django Admin
🌿 Controle de versão	Git + GitHub