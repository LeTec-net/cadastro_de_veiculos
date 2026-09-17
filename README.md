# 🚗 FLEETCARD — Sistema de Gestão e Cadastro de Veículos

**Gist Completo do Projeto**

---

## 📋 Ficha do Projeto

| Campo | Valor |
|---|---|
| 📛 Nome | FleetCard |
| 🎓 Tipo | Atividade Avaliativa Prática — Grupo 3 |
| 📚 Curso | Programador Back-End Python |
| 🧩 Unidade Curricular | Desenvolvimento Web com Django |
| 🗓️ Turma | 2026.2 |
| 🔗 GitHub | `chavierwebmidia2026-glitch/cadastro_de_veiculos` |

---

## 👥 Equipe — Grupo 3

| Integrante | Função |
|---|---|
| Raphael Farias | Desenvolvedor |
| Kayke Cansanção | Desenvolvedor |
| Letícia | Desenvolvedora |
| Fabiano | Desenvolvedor |

---

## 📌 Sobre o Projeto

O FleetCard é uma aplicação web em **Django** para cadastro e gerenciamento de veículos, com CRUD completo para **Veículos** e **Ordens de Serviço**, mantendo o relacionamento entre cada ordem e seu veículo.

Também inclui: formulário de contatos com persistência no banco, autenticação de usuários, Django Admin personalizado, integração com API própria e interface responsiva.

---

## ✨ Funcionalidades

- 🚗 CRUD completo de veículos
- 🛠️ CRUD completo de Ordens de Serviço
- 🔎 Listagem e consulta de veículos
- ✏️ Edição de veículos
- 🗑️ Exclusão de veículos
- ➕ Cadastro de Ordens de Serviço
- ✏️ Edição de Ordens de Serviço
- 🗑️ Exclusão de Ordens de Serviço
- 🔗 Ordens de Serviço vinculadas aos veículos
- 📩 Formulário de contatos com armazenamento no banco
- 🔐 Autenticação de usuários
- ⚙️ Django Admin personalizado
- 🌐 Página de veículos integrada com API
- 📱 Interface responsiva para desktop e mobile

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Utilização |
|---|---|---|
| 🐍 Python | 3.13.13 | Linguagem principal |
| 🌐 Django | 6.1.1 | Framework web |
| 🗄️ SQLite | — | Banco de dados |
| 🎨 Bootstrap | 5.3.3 | Interface responsiva |
| 🔹 Bootstrap Icons | 1.11.3 | Ícones |
| 🖌️ CSS personalizado | `static/css/` | Estilização própria sobre o Bootstrap (cores, cards, hover, navbar/footer) |
| 🔀 Git | — | Controle de versão |
| ☁️ GitHub | — | Repositório e colaboração |

---

## 🎨 Identidade Visual

### Cores principais

| Cor | Hex | Utilização |
|---|---|---|
| 🔴 Primária | `#8A2A22` | Botões, navbar e destaques |
| 🟥 Primária escura | `#6B1E18` | Hover e gradientes |
| 🟡 Dourado | `#BE770D` | Destaques secundários |
| 🟤 Texto | `#2E1B12` | Textos principais |
| 🟫 Texto suave | `#6B5544` | Textos secundários |
| 🟨 Fundo | `#FBF1E0` | Fundo da página |
| ⚪ Fundo Card | `#FFFFFF` | Cards e formulários |
| ❌ Danger | `#A5342A` | Exclusões e erros |
| ✅ Success | `#3E7A44` | Confirmações |
| ℹ️ Info | `#2E6F73` | Informações |
| ⚠️ Warning | `#C98A1B` | Avisos |

### Layout
- Bordas arredondadas: `border-radius: 0.75rem`
- Cards com sombra e efeito hover
- Botões com elevação suave
- Navbar e footer com gradiente vermelho-escuro
- 🔐 Tela de login estilizada com as cores da identidade visual (`login.css`)
- Layout responsivo com Bootstrap
- Tabelas no desktop, adaptadas em telas menores

---

## 🗄️ Modelos do Banco de Dados

### 🚗 Veiculo

| Campo | Tipo | Descrição |
|---|---|---|
| tipo | Choices | Carro, moto ou caminhão |
| marca | CharField | Marca do veículo |
| modelo | CharField | Modelo do veículo |
| placa | Unique | Identificação única |
| ano | IntegerField | Ano do veículo |
| cor | CharField | Cor do veículo |
| combustivel | Choices | Gasolina, etanol, diesel, flex, elétrico, híbrido etc. |
| quilometragem | IntegerField | Quilometragem atual |
| observacoes | TextField | Observações adicionais |
| imagem | ImageField | Foto do veículo |
| data_cadastro | DateTimeField | Registrada automaticamente |

### 🛠️ OrdemServico

Relacionamento **1 para muitos** com Veiculo:

```
Veiculo
   │
   ├── OrdemServico
   ├── OrdemServico
   └── OrdemServico
```

- Um veículo pode ter várias Ordens de Serviço
- Cada OS fica vinculada a um veículo via FK

### 📩 Contato

| Campo | Tipo | Finalidade |
|---|---|---|
| nome | CharField | Nome do remetente |
| email | EmailField | E-mail |
| telefone | CharField | Telefone (opcional) |
| assunto | CharField | Assunto da mensagem |
| mensagem | TextField | Mensagem enviada |
| data_envio | DateTimeField | Registrada automaticamente |

---

## 🔄 Rotas do Sistema

### 🚗 CRUD de Veículos

| Operação | Método | Rota | Função |
|---|---|---|---|
| ➕ Create | POST | `/veiculos/cadastrar/` | Cadastrar veículo |
| 📋 Read | GET | `/veiculos/` | Listar veículos |
| ✏️ Update | GET/POST | `/veiculos/editar/<id>/` | Editar veículo |
| 🗑️ Delete | GET/POST | `/veiculos/excluir/<id>/` | Excluir veículo |

**Fluxo cadastro:**
```
Cadastrar → /veiculos/cadastrar/ → Veiculo.objects.create() → SQLite → /veiculos/ → Listagem
```

**Fluxo edição:**
```
/veiculos/ → Editar → /veiculos/editar/<id>/ → Veiculo.objects.get() → Atualização → SQLite
```

**Fluxo exclusão:**
```
/veiculos/ → Excluir → /veiculos/excluir/<id>/ → Confirmação → Veiculo.delete() → SQLite
```

### 🛠️ CRUD de Ordens de Serviço

| Operação | Método | Rota | Função |
|---|---|---|---|
| ➕ Create | GET/POST | `/ordens-servico/cadastrar/<veiculo_id>/` | Cadastrar OS para um veículo |
| 📋 Read | GET | `/ordens-servico/` | Listar todas as OS |
| 📋 Read | GET | `/veiculos/<veiculo_id>/ordens-servico/` | Listar OS de um veículo |
| ✏️ Update | GET/POST | `/ordens-servico/editar/<id>/` | Editar OS |
| 🗑️ Delete | GET/POST | `/ordens-servico/excluir/<id>/` | Excluir OS |

**Fluxo:**
```
Veículos → Selecionar veículo → /ordens-servico/cadastrar/<veiculo_id>/
→ Cadastrar serviço → OrdemServico → Relacionamento com Veiculo → SQLite
```

### 🌐 Rotas Gerais

| Rota | Função |
|---|---|
| `/` | 🏠 Página inicial |
| `/sobre/` | ℹ️ Sobre o projeto |
| `/contatos/` | 📩 Formulário de contatos |
| `/pagina_veiculos/` | 🚗 Página de veículos integrada com API |
| `/deslogar/` | 🔐 Encerrar sessão |
| `/admin/` | ⚙️ Área administrativa |

---

## 🔐 Autenticação e Controle de Acesso

Usa o sistema de autenticação do Django:

```
Usuário não autenticado → Acesso às páginas públicas → Login
→ Usuário autenticado → Funcionalidades protegidas → Django Admin
```

---

## ⚙️ Django Admin

Gerencia: 🚗 Veículos · 🛠️ Ordens de Serviço · 📩 Contatos

Possui personalização visual própria, diferente da área pública.

---

## 🗂️ Estrutura do Projeto

```
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
│           ├── login.css        # Estilização da tela de login (cores da identidade)
│           ├── style.css        # Estilos globais do projeto
│           ├── veiculos.css     # Estilos das páginas de veículos
│           └── ver_detalhes.css # Estilos da página de detalhes do veículo
│
├── config/
├── manage.py
├── db.sqlite3
└── requirements.txt
```

### 🎨 Estrutura da pasta `static/css/`

```
static/
└── css/
    ├── login.css
    ├── style.css
    ├── veiculos.css
    └── ver_detalhes.css
```

| Arquivo | Onde é usado | Responsabilidade |
|---|---|---|
| 🔐 `login.css` | Tela de login | Estilização da tela de autenticação com as cores da identidade visual do FleetCard |
| 🎨 `style.css` | Base do projeto (`base.html`) | Estilos globais: navbar, footer, tipografia e elementos compartilhados por todas as páginas |
| 🚗 `veiculos.css` | Páginas de veículos (listagem, cadastro, edição) | Estilização de cards, tabelas e formulários relacionados aos veículos |
| 🔎 `ver_detalhes.css` | Página de detalhes do veículo | Estilização específica da visualização detalhada de um veículo |

---

## 🔗 Arquitetura das Rotas

```
🌐 Navegador → 🔗 URL → 👁️ View → 🧩 Model/ORM → 🗄️ SQLite → 📄 Template → 🌐 Navegador
```

No CRUD:

```
Usuário → URL → View → ORM do Django → Banco de Dados → Template → Resultado na tela
```

---

## 🚀 Como Executar o Projeto

1. **Clonar o repositório**
   ```bash
   git clone https://github.com/chavierwebmidia2026-glitch/cadastro_de_veiculos.git
   ```
2. **Entrar na pasta**
   ```bash
   cd cadastro_de_veiculos
   ```
3. **Criar o ambiente virtual**
   ```bash
   python -m venv venv
   ```
4. **Ativar o ambiente virtual (Windows)**
   ```bash
   venv\Scripts\activate
   ```
5. **Instalar as dependências**
   ```bash
   pip install -r requirements.txt
   ```
6. **Executar as migrations**
   ```bash
   python manage.py migrate
   ```
7. **Criar superusuário** (opcional)
   ```bash
   python manage.py createsuperuser
   ```
8. **Executar o servidor**
   ```bash
   python manage.py runserver
   ```
9. **Acessar o sistema**
   - App: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`

---

## 🧪 Principais Operações do Sistema

**🚗 Veículos:** CREATE → cadastrar | READ → listar | UPDATE → editar | DELETE → excluir

**🛠️ Ordens de Serviço:** CREATE → cadastrar OS | READ → listar OS | UPDATE → editar OS | DELETE → excluir OS

**📩 Contatos:**
```
Formulário → POST → View contatos() → Contato.objects.create() → SQLite → Mensagem de sucesso
```

---

## 📱 Responsividade

Desenvolvida com Bootstrap 5.3.3, cobrindo: 🖥️ Desktop · 💻 Notebook · 📱 Smartphone · 📲 Tablet

Navegação, cards, formulários, tabelas e botões estruturados para usabilidade em qualquer dispositivo.

---

## 🔀 Git e GitHub

**Fluxo:**
```
feature/* → desenvolvimento → commit → push → GitHub → develop → master
```

**Exemplo de commit:**
```bash
git add .
git commit -m "feat: implementa CRUD de veículos"
git push
```

---

## 📊 Situação Atual do Projeto

- ✅ Cadastro de veículos
- ✅ Listagem de veículos
- ✅ Edição de veículos
- ✅ Exclusão de veículos
- ✅ Cadastro de Ordens de Serviço
- ✅ Listagem de Ordens de Serviço
- ✅ Edição de Ordens de Serviço
- ✅ Exclusão de Ordens de Serviço
- ✅ Relacionamento Veiculo × OrdemServico
- ✅ Formulário de contatos
- ✅ Persistência dos contatos no banco
- ✅ Autenticação
- ✅ Django Admin personalizado
- ✅ Integração com API
- ✅ Interface responsiva
- ✅ Controle de versão com Git/GitHub

**Status: projeto concluído 🎉**

---

## 📚 Objetivo Educacional

Aplicar na prática: Python · Django · Django ORM · SQLite · CRUD · Templates · Views · URLs · Autenticação · Django Admin · Bootstrap · Banco de dados relacional · Git e GitHub · Desenvolvimento web responsivo

---

## 📄 Licença

Projeto desenvolvido para fins educacionais, como parte da Atividade Avaliativa Prática do curso Programador Back-End Python, na Unidade Curricular Desenvolvimento Web com Django.

---

**🚗 FleetCard — Sistema de Gestão e Cadastro de Veículos**