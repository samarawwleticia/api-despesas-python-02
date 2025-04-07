# 💸 Projeto de Controle de Despesas Pessoais

Este é um projeto simples de controle de despesas pessoais, desenvolvido com **Python**, usando o framework **Flask**, com suporte a autenticação de usuários via **Flask-Login** e persistência de dados com **SQLAlchemy**.

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-Login](https://flask-login.readthedocs.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- SQLite

## 📋 Funcionalidades

- Cadastro e login de usuários
- Autenticação de sessões com Flask-Login
- CRUD de despesas:
  - Adicionar nova despesa
  - Listar despesas
  - Editar e remover despesas
- Categorização das despesas (ex: alimentação, transporte, lazer)
- Filtro por data ou categoria 

## 🔧 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Programmer-Girls/api-despesas-python-02.git
cd projeto-despesas
````

### 2. Crie e ative um ambiente virtual
````bash
python -m venv venv
source venv/bin/activate (linux e Mac) | venv\Scripts\activate (windows)
````

### 3. Instale as dependências
````bash
pip install -r requirements.txt
````

### 4. Rode a aplicação

````bash
flask run
````

A aplicação estará disponível em **http://127.0.0.1:5000.**

## 🗃️ Estrutura

```plaintext
📁 projeto-despesas/
│
├── app.py               # Arquivo principal da aplicação Flask
├── models.py            # Modelos SQLAlchemy
├── forms.py             # Formulários com WTForms
├── templates/           # Templates HTML
├── static/              # Arquivos estáticos (CSS, JS, imagens)
├── requirements.txt     # Dependências do projeto
└── README.md
````

## ✨ Créditos

Projeto desenvolvido por Karolline Falcão, Letycia Locha, Samara Letícia, Isabela e Beatriz Cardoso durante a dinâmica de back-end da ProGirls. 💜
