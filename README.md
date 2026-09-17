# 🚗 FLEETCARD
### Sistema de Gestão e Cadastro de Veículos
**Documentação Completa do Projeto — Grupo 3**

---

## 📋 Ficha do Projeto

| Campo | Valor |
|---|---|
| 🎓 Atividade | Atividade Avaliativa Prática — Projeto: Cadastro de Veículos |
| 📚 Curso | Programador Back-End Python |
| 🧩 Unidade Curricular | Desenvolvimento Web com Django |
| 🗓️ Turma | 2026.2 |
| 👥 Grupo | Grupo 3 |
| 🙋 Integrantes | Raphael Farias • Kayke Cansanção • Letícia • Fabiano |
| 🔗 GitHub | `chavierwebmidia2026-glitch/cadastro_de_veiculos` |

> 📌 **Projeto Integrador — Grupo 3**
> Documentação do sistema FleetCard, desenvolvido com Python, Django, SQLite e Bootstrap.

---

## 1️⃣ Situação de Aprendizagem

O projeto FleetCard foi desenvolvido para **centralizar o cadastro e o gerenciamento de veículos** em uma aplicação web. O sistema organiza as informações dos veículos e permite realizar operações de **cadastro, consulta, atualização e exclusão**.

Durante o desenvolvimento, o projeto foi ampliado para incluir:
- 🛠️ Ordens de Serviço relacionadas aos veículos
- 📩 Formulário de Contatos com armazenamento no banco de dados
- 🔐 Autenticação de usuários
- ⚙️ Área administrativa personalizada
- 🌐 Integração da página de veículos com uma API

> ✅ **Implementação no FleetCard:** A situação foi adaptada ao FleetCard, substituindo o cenário de *Controle de Produtos* do exemplo pelo problema de cadastro e gerenciamento de veículos que é tratado pelo projeto.

---

## 2️⃣ Desafio

> Desenvolver um sistema web denominado **FleetCard**, permitindo o cadastro, consulta, atualização e exclusão de veículos de forma organizada.

A aplicação utiliza **Django Admin** para gerenciamento administrativo e **Bootstrap 5** para construção da interface web.

> ✅ **Implementação no FleetCard:** O desafio é atendido pelo CRUD de veículos e pelas demais funcionalidades implementadas no projeto.

---

## 3️⃣ Competências Desenvolvidas

- ⚙️ Configurar um projeto Django
- 🧩 Criar aplicação utilizando Django
- 🗄️ Modelar banco de dados utilizando ORM
- 💾 Utilizar SQLite
- 🔄 Desenvolver operações CRUD
- 🛠️ Utilizar Django Admin
- 📄 Criar Templates reutilizáveis
- 🔗 Organizar URLs e Views
- 🎨 Aplicar Bootstrap
- 🔐 Utilizar autenticação do Django
- 🔁 Criar relacionamento entre modelos
- 📩 Persistir dados de formulário
- 🌐 Integrar uma página com API
- 🔀 Utilizar Git e GitHub

---

## 4️⃣ Recursos Disponíveis

| Recurso | Detalhe |
|---|---|
| 🐍 Python | 3.13.13 |
| 🌐 Django | 6.1.1 |
| 🗄️ SQLite | Banco de dados |
| 💻 Visual Studio Code | Editor |
| 🎨 Bootstrap | 5.3.3 |
| 🔹 Bootstrap Icons | 1.11.3 |
| 🔀 Git e GitHub | Controle de versão |
| 🌍 Navegador Web | Execução/teste |

---

## 5️⃣ Entregáveis

- ✅ Projeto Django funcionando
- ✅ Código-fonte organizado
- ✅ Banco SQLite
- ✅ Interface funcional e responsiva
- ✅ CRUD de veículos
- ✅ CRUD de Ordens de Serviço
- ✅ Formulário de Contatos com persistência
- ✅ Django Admin personalizado
- ✅ Autenticação
- ✅ Página de veículos integrada com API

---

## 6️⃣ Requisitos Funcionais

### 🔹 RF01 — Criar o projeto Django
> Criar um projeto Django chamado: `cadastro_de_veiculos`

✅ **Implementação:** O projeto Django utilizado no desenvolvimento está organizado no projeto `cadastro_de_veiculos`, tendo a aplicação **FleetCard** como aplicação principal.

### 🔹 RF02 — Criar o aplicativo
> Criar um aplicativo chamado: `FleetCard`

✅ **Implementação:** Foi criada a aplicação Django **FleetCard**, responsável pelas funcionalidades de veículos, Ordens de Serviço, Contatos e demais recursos do sistema.

### 🔹 RF03 — Modelo Veiculo
> Criar o modelo `Veiculo` contendo os campos utilizados no projeto.

| Campo | Tipo / característica | Como é utilizado |
|---|---|---|
| `tipo` | Choices | Carro, moto ou caminhão |
| `marca` | CharField | Marca do veículo |
| `modelo` | CharField | Modelo do veículo |
| `placa` | Campo único | Identificação única do veículo |
| `ano` | Campo numérico | Ano do veículo |
| `cor` | CharField | Cor do veículo |
| `combustivel` | Choices | Gasolina, etanol, diesel, flex, elétrico ou híbrido |
| `quilometragem` | Campo numérico | Quilometragem do veículo |
| `observacoes` | TextField | Observações adicionais |
| `imagem` | ImageField | Imagem do veículo |
| `data_cadastro` | DateTimeField | Data registrada automaticamente |

✅ **Implementação:** O modelo `Veiculo` é utilizado pelo cadastro, listagem, edição e exclusão dos veículos.

### 🔹 RF04 — Registrar no Django Admin
> O Admin deverá possuir pesquisa, filtros e ordenação para facilitar o gerenciamento.

- 🔎 Pesquisa por marca
- 🔎 Pesquisa por modelo
- 🔎 Pesquisa por placa
- 🧰 Filtro por tipo
- 🧰 Filtro por combustível
- 🧰 Filtro por ano
- 🔃 Ordenação pela data de cadastro

✅ **Implementação:** O `VeiculoAdmin` foi configurado com `list_display`, `search_fields`, `list_filter` e `ordering`.

### 🔹 RF05 — Criar as páginas
- 🏠 Home
- 📋 Lista de Veículos
- ➕ Cadastrar Veículo
- ✏️ Editar Veículo
- 🗑️ Excluir Veículo
- 🚗 Página de Veículos
- 📩 Contatos
- ℹ️ Sobre

✅ **Implementação:** Essas páginas fazem parte da estrutura atual do FleetCard.

### 🔹 RF06 — Template Base
> Criar um Template Base. Todas as páginas deverão utilizar herança de templates.

✅ **Implementação:** O projeto utiliza `base.html` como template base. As páginas utilizam herança com `{% extends 'base.html' %}`, mantendo uma estrutura comum.

### 🔹 RF07 — Menu de navegação
> Criar um menu contendo as principais áreas do sistema:

- 🏠 Home
- 🚗 Veículos
- ➕ Cadastrar Veículo
- 📋 Listar Veículos
- 📩 Contatos
- ℹ️ Sobre

✅ **Implementação:** O menu do FleetCard utiliza navbar e menu lateral/offcanvas para organizar a navegação.

### 🔹 RF08 — Tela de listagem
> A tela de listagem deverá apresentar os dados dos veículos e as ações disponíveis:

**Tipo · Marca · Modelo · Placa · Ano · Cor · Combustível · Quilometragem · Ações**

✅ **Implementação:** A página `lista_veiculos.html` apresenta os veículos cadastrados e as opções de gerenciamento.

### 🔹 RF09 — Ações disponíveis
As ações deverão permitir:
- 👁️ Visualizar/consultar
- ✏️ Editar
- 🗑️ Excluir

✅ **Implementação:** O CRUD de veículos possui ações de edição e exclusão, além da consulta/listagem dos registros.

### 🔹 RF10 — Página de detalhes/cadastro
> Na página de detalhes/cadastro deverão aparecer as informações do veículo.

✅ **Implementação:** O formulário de veículo trabalha com os campos definidos no modelo `Veiculo`, permitindo cadastrar e editar as informações.

---

## 7️⃣ Rotas do CRUD — Veículos e Ordens de Serviço

O FleetCard organiza as operações de cadastro, consulta, edição e exclusão por meio das URLs do Django. As rotas são conectadas às Views e aos templates correspondentes. As funcionalidades de gerenciamento do site são disponibilizadas ao usuário autenticado.

### 🚗 7.1 CRUD de Veículos

| Operação | Rota de acesso | Finalidade |
|---|---|---|
| ➕ Create | `/veiculos/cadastrar/` | Abre o cadastro de um novo veículo |
| 📋 Read | `/veiculos/` | Lista os veículos cadastrados |
| 👁️ Read — detalhes | `/pagina_veiculos/detalhes/<tipo>/<marca>/<modelo>/` | Exibe os detalhes de um veículo |
| ✏️ Update | `/veiculos/editar/<id>/` | Edita os dados do veículo identificado pelo ID |
| 🗑️ Delete | `/veiculos/excluir/<id>/` | Solicita confirmação e exclui o veículo |

### 🛠️ 7.2 CRUD de Ordens de Serviço

| Operação | Rota de acesso | Finalidade |
|---|---|---|
| ➕ Create | `/ordens-servico/cadastrar/<veiculo_id>/` | Cadastra uma OS vinculada a um veículo |
| 📋 Read | `/ordens-servico/` | Lista as Ordens de Serviço |
| 👁️ Read — veículo | `/veiculos/<veiculo_id>/ordens-servico/` | Consulta as ordens vinculadas a um veículo |
| ✏️ Update | `/ordens-servico/editar/<id>/` | Edita a OS identificada pelo ID |
| 🗑️ Delete | `/ordens-servico/excluir/<id>/` | Solicita confirmação e exclui a OS |

### 🌐 7.3 Rotas gerais relacionadas ao sistema

| Rota | Nome / função |
|---|---|
| `/` | 🏠 Home — página inicial |
| `/sobre/` | ℹ️ Sobre — apresentação do projeto |
| `/contatos/` | 📩 Contatos — formulário e persistência das mensagens |
| `/pagina_veiculos/` | 🚗 Página de veículos integrada à API |
| `/deslogar/` | 🔐 Encerramento da sessão |
| `/admin/` | ⚙️ Área administrativa do Django |

**🔄 Fluxo do CRUD:**
```
Navegador → URL → View → Django ORM → SQLite → Template
```

> ⚠️ **Observação:** Os parâmetros entre `<>` são valores dinâmicos, como o ID do registro ou o identificador do veículo. O Django Admin também mantém as rotas administrativas próprias para gerenciamento dos modelos.

---

## 8️⃣ Funcionalidades Desenvolvidas Além do Exemplo

### 🔹 RF11 — Ordens de Serviço
> Criar o modelo `OrdemServico` relacionado ao veículo.

✅ **Implementação:** O FleetCard possui o modelo `OrdemServico` relacionado ao `Veiculo`. Um veículo pode possuir várias ordens de serviço.

- ➕ Cadastrar Ordem de Serviço
- 📋 Listar Ordens de Serviço
- ✏️ Editar Ordem de Serviço
- 🗑️ Excluir Ordem de Serviço
- 🔎 Consultar ordens vinculadas a um veículo

### 🔹 RF12 — Contatos
> Criar o modelo `Contato` para armazenar mensagens enviadas pelo formulário.

| Campo | Tipo | Finalidade |
|---|---|---|
| `nome` | CharField | Nome do remetente |
| `email` | EmailField | E-mail |
| `telefone` | CharField | Telefone, opcional |
| `assunto` | CharField | Assunto |
| `mensagem` | TextField | Mensagem enviada |
| `data_envio` | DateTimeField | Data/hora automática |

✅ **Implementação:** O formulário salva os dados no banco e apresenta mensagem de confirmação após o envio.

### 🔹 RF13 — Autenticação
✅ **Implementação:** O sistema utiliza a autenticação do Django para controlar funcionalidades adicionais conforme o usuário esteja autenticado. O Django Admin utiliza login e permissões administrativas.

### 🔹 RF14 — API
✅ **Implementação:** A página de veículos possui integração com API pública para consulta de modelos, organizando resultados por carros, motocicletas e caminhões.

### 🔹 RF15 — Responsividade
✅ **Implementação:** A interface utiliza Bootstrap 5 e componentes responsivos, incluindo menu lateral/offcanvas, cards e formulários adaptáveis. Botões ficam sempre em linha. Listagens de Ordens de Serviço exibem tabela no desktop e cards no celular para melhor usabilidade.

---

## 9️⃣ Requisitos Técnicos

- 🌐 Django
- 🧩 ORM
- 🗄️ SQLite
- 📄 Templates
- 🎨 Bootstrap 5
- 🔹 Bootstrap Icons
- ⚙️ Django Admin
- 🐍 Python
- 🔀 Git e GitHub

✅ **Implementação:** Todos os itens acima fazem parte da estrutura e desenvolvimento do FleetCard.

---

## 🔟 Regras de Negócio

| Regra | Aplicação no FleetCard |
|---|---|
| RN01 | A placa do veículo é única |
| RN02 | O tipo do veículo utiliza as opções definidas no modelo |
| RN03 | O combustível utiliza as opções definidas no modelo |
| RN04 | Uma Ordem de Serviço pertence a um veículo |
| RN05 | Um veículo pode possuir várias Ordens de Serviço |
| RN06 | Os dados do formulário de Contatos são armazenados no banco |
| RN07 | A data do contato é registrada automaticamente |
| RN08 | Após o envio do contato é exibida uma confirmação |
| RN09 | O redirecionamento após POST evita reenvio ao atualizar a página |
| RN10 | Funcionalidades administrativas respeitam autenticação e permissões |

---

## 1️⃣1️⃣ Banco de Dados

O FleetCard utiliza **SQLite** e possui os principais modelos abaixo:

| Modelo | Função | Relacionamento |
|---|---|---|
| 🚗 `Veiculo` | Cadastro de veículos | 1:N com `OrdemServico` |
| 🛠️ `OrdemServico` | Serviços vinculados aos veículos | N:1 com `Veiculo` |
| 📩 `Contato` | Mensagens recebidas pelo formulário | Independente |

---

## 1️⃣2️⃣ Templates e Estrutura do Projeto

| Arquivo / pasta | Função |
|---|---|
| `base.html` | Template base (herança de todas as páginas) |
| `includes/navbar.html` | Navbar e navegação (menu lateral/offcanvas) |
| `includes/footer.html` | Rodapé |
| `home.html` | Página inicial |
| `sobre.html` | Página sobre o projeto |
| `contatos.html` | Formulário de contatos com persistência |
| `cadastrar_veiculo.html` | Cadastro de novo veículo |
| `lista_veiculos.html` | Listagem de veículos cadastrados |
| `editar_veiculo.html` | Edição de veículo existente |
| `pagina_veiculos.html` | Página de veículos integrada com API |
| `cadastrar_ordem_servico.html` | Cadastro de Ordem de Serviço |
| `lista_ordens_servico.html` | Listagem geral de Ordens de Serviço |
| `editar_ordem_servico.html` | Edição de Ordem de Serviço |
| `excluir_ordem_servico.html` | Confirmação de exclusão de OS |
| `ordens_servico_veiculo.html` | Ordens de Serviço de um veículo específico |

---

## 1️⃣3️⃣ Processo de Execução

1. ⚙️ Configuração do ambiente Python/Django
2. 🧩 Criação do projeto e aplicação
3. 🗄️ Configuração do SQLite e migrations
4. 🏗️ Criação dos modelos
5. 📄 Criação do template base
6. 🚗 Implementação do CRUD de veículos
7. 🛠️ Implementação das Ordens de Serviço
8. 🌐 Integração da API de veículos
9. 📩 Criação do modelo e formulário de Contatos
10. 💾 Persistência dos contatos no banco
11. 🎨 Personalização do Django Admin
12. 🔐 Configuração da autenticação
13. 📱 Ajustes de responsividade (botões em linha, tabelas → cards no mobile)
14. 🧪 Testes e correções
15. 🔀 Versionamento com Git/GitHub

---

## 1️⃣4️⃣ Git e GitHub

O projeto utiliza **Git** para controle de versões e **GitHub** para armazenamento remoto. Foram utilizadas *branches* de funcionalidades durante o desenvolvimento, permitindo separar alterações e integrar as funcionalidades posteriormente.

---

## 1️⃣5️⃣ Situação Atual

- ✅ CRUD de veículos funcionando
- ✅ CRUD de Ordens de Serviço funcionando
- ✅ Relacionamento entre `Veiculo` e `OrdemServico` funcionando
- ✅ Formulário de Contatos funcionando
- ✅ Contatos salvos no banco
- ✅ Autenticação funcionando
- ✅ Django Admin personalizado
- ✅ API de veículos integrada
- ✅ Interface responsiva (desktop + mobile)

---

## 1️⃣6️⃣ Conclusão

O **FleetCard** atende à proposta de desenvolver uma aplicação web utilizando Django para gerenciamento de veículos. A implementação contempla os requisitos do documento-exemplo adaptados ao contexto real do projeto.

Além dos requisitos básicos apresentados no exemplo, o FleetCard possui funcionalidades adicionais, como:
- 🛠️ Ordens de Serviço
- 📩 Contatos com persistência
- 🔐 Autenticação
- 🌐 Integração com API
- ⚙️ Personalização do Django Admin

A documentação mantém a organização do modelo fornecido pelo professor, mas apresenta as respostas e implementações correspondentes ao projeto FleetCard desenvolvido pelo Grupo 3.

---

<div align="center">

**🚗 FleetCard — Sistema de Gestão e Cadastro de Veículos**

*Grupo 3 — Raphael Farias • Kayke Cansanção • Letícia • Fabiano*
*Turma 2026.2 | Desenvolvimento Web com Django*

</div>