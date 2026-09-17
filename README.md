

README.md
arquivos
🚗 FleetCard
Sistema de Gestão e Cadastro de Veículos








📋 Sobre o Projeto
O FleetCard é uma aplicação web desenvolvida para centralizar o cadastro e o gerenciamento de veículos. O sistema permite realizar operações de cadastro, consulta, atualização e exclusão, além de gerenciar Ordens de Serviço vinculadas a cada veículo.

✨ Funcionalidades
✅ CRUD completo de Veículos

✅ CRUD completo de Ordens de Serviço

✅ Formulário de Contatos com persistência no banco

✅ Autenticação de usuários

✅ Django Admin personalizado

✅ Página de veículos integrada com API

✅ Interface 100% responsiva (desktop + mobile)

🛠️ Tecnologias Utilizadas
Tecnologia

Versão

Descrição

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

✨ Bootstrap Icons

1.11.3

Ícones da interface

📦 Git / GitHub

—

Controle de versão

🎨 Cores e Layout
O FleetCard utiliza uma identidade visual própria, com tons terrosos e vermelho-escuro, transmitindo seriedade e modernidade.

🎨 Paleta de Cores
Nome

Hex

Uso principal

🟥 Primária

#8A2A22

Botões, navbar, destaques

🟥 Primária Escura

#6B1E18

Hover e gradientes

🟡 Dourado

#BE770D

Destaques secundários, indicadores

🟤 Texto

#2E1B12

Textos principais

🟤 Texto Suave

#6B5544

Textos secundários

beige Fundo

#FBF1E0

Fundo da página

⬜ Fundo Card

#FFFFFF

Cards e formulários

🔴 Danger

#A5342A

Ações de exclusão / erros

🟢 Success

#3E7A44

Confirmações e status positivos

🔵 Info

#2E6F73

Informações

🟠 Warning

#C98A1B

Avisos

✍️ Tipografia
Tipo

Fonte

Uso

🔤 Display

Poppins

Títulos (h1–h6)

📝 Corpo

Inter

Textos e formulários

📐 Layout
Border Radius: 0.75rem (arredondamento suave)

Sombra padrão: suave e elegante

Transições: 0.25s ease

Cards: efeito hover com elevação

Botões: elevação suave no hover

Navbar / Footer: gradiente vermelho-escuro

Formulários: inputs brancos com borda sutil e foco em vermelho

📱 Responsividade
Dispositivo

Comportamento

💻 Desktop / Tablet

Tabelas completas + layout em colunas

📱 Celular

Cards organizados + botões em linha + menu offcanvas

📁 Estrutura do Projeto
cadastro_de_veiculos/
│
├── 📂 FleetCard/                     # Aplicação principal
│   ├── 📄 models.py                  # Veiculo, OrdemServico, Contato
│   ├── 📄 views.py
│   ├── 📄 urls.py
│   ├── 📄 admin.py
│   ├── 📄 forms.py
│   │
│   └── 📂 templates/
│       ├── 📄 base.html
│       ├── 📂 includes/
│       │   ├── 📄 navbar.html
│       │   └── 📄 footer.html
│       ├── 📄 home.html
│       ├── 📄 sobre.html
│       ├── 📄 contatos.html
│       ├── 📄 cadastrar_veiculo.html
│       ├── 📄 lista_veiculos.html
│       ├── 📄 editar_veiculo.html
│       ├── 📄 pagina_veiculos.html
│       ├── 📄 cadastrar_ordem_servico.html
│       ├── 📄 lista_ordens_servico.html
│       ├── 📄 editar_ordem_servico.html
│       ├── 📄 excluir_ordem_servico.html
│       └── 📄 ordens_servico_veiculo.html
│
├── 📄 manage.py
├── 📄 db.sqlite3
└── 📄 requirements.txt
🗄️ Modelos do Banco de Dados
🚙 Veiculo
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

Gasolina, etanol, diesel, flex...

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

Registrada automaticamente

🛠️ OrdemServico
Relacionamento 1:N com Veiculo
→ Um veículo pode possuir várias ordens de serviço.

📩 Contato
Armazena as mensagens enviadas pelo formulário:

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

Telefone (opcional)

assunto

CharField

Assunto

mensagem

TextField

Mensagem enviada

data_envio

DateTimeField

Data/hora automática

🔗 Principais Rotas
🚗 Veículos
Operação

Rota

Descrição

➕ Create

/veiculos/cadastrar/

Cadastrar novo veículo

📋 Read

/veiculos/

Listar veículos

✏️ Update

/veiculos/editar/<id>/

Editar veículo

🗑️ Delete

/veiculos/excluir/<id>/

Excluir veículo

🛠️ Ordens de Serviço
Operação

Rota

Descrição

➕ Create

/ordens-servico/cadastrar/<veiculo_id>/

Cadastrar OS vinculada a um veículo

📋 Read

/ordens-servico/

Listar todas as OS

🔍 Read

/veiculos/<veiculo_id>/ordens-servico/

OS de um veículo específico

✏️ Update

/ordens-servico/editar/<id>/

Editar OS

🗑️ Delete

/ordens-servico/excluir/<id>/

Excluir OS

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

🔌 Página de veículos + API

/deslogar/

🚪 Encerrar sessão

/admin/

⚙️ Área administrativa Django

🚀 Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/chavierwebmidia2026-glitch/cadastro_de_veiculos.git
cd cadastro_de_veiculos
2️⃣ Crie e ative o ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
3️⃣ Instale as dependências
pip install -r requirements.txt
4️⃣ Aplique as migrations
python manage.py migrate
5️⃣ (Opcional) Crie um superusuário
python manage.py createsuperuser
6️⃣ Execute o servidor
python manage.py runserver
🌐 Acesse: http://127.0.0.1:8000

👥 Equipe — Grupo 3
Integrante

Função

👨‍💻 Raphael Farias

Desenvolvedor

👨‍💻 Kayke Cansanção

Desenvolvedor

👩‍💻 Letícia

Desenvolvedora

👨‍💻 Fabiano

Desenvolvedor

🎓 Turma: 2026.2
📚 Curso: Programador Back-End Python
📖 Unidade Curricular: Desenvolvimento Web com Django

📄 Licença
Este projeto foi desenvolvido para fins educacionais como parte da Atividade Avaliativa Prática do curso Programador Back-End Python.

FleetCard © 2026 — Grupo 3