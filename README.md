# 💡 DSA AI SQL Query Generator - Text-to-SQL

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-blue?logo=streamlit)  
![Python](https://img.shields.io/badge/Python-3.10+-green?logo=python)  
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue?logo=postgresql)  
![Hosted](https://img.shields.io/badge/Hosted%20on-Streamlit%20Cloud-orange?logo=streamlit)

> Projeto Final - Curso de Analista de Dados da [Data Science Academy](https://www.datascienceacademy.com.br)  
> Desenvolvido por **Alex Felipe Barbosa** — 02/07/2025  
> Acesse o projeto online:  
> 🔗 [https://alexfelipebarbosa-gerartemplatesql.streamlit.app/](https://alexfelipebarbosa-gerartemplatesql.streamlit.app/)

---

## 🧠 Visão Geral

Este projeto é uma aplicação **Text-to-SQL** que utiliza **Inteligência Artificial** (modelo Gemini da Google) para transformar uma descrição em linguagem natural em um template de **consulta SQL**.

Além da query, a aplicação gera:

- ✅ Um exemplo de saída esperada  
- ✅ Uma explicação detalhada da sintaxe SQL  
- ✅ Opção para download do conteúdo gerado  

---

## ⚙️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Google Generative AI - Gemini 2](https://ai.google.dev/)
- [PostgreSQL](https://www.postgresql.org/) (hospedado no [Neon](https://neon.tech/))
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- Hospedagem: [Streamlit Cloud](https://streamlit.io/cloud)

---

## 🧪 Como Funciona

1. O usuário digita uma **descrição da consulta** desejada.
2. O modelo Gemini transforma essa descrição em **query SQL**.
3. O sistema gera também um **exemplo da saída esperada** e uma **explicação** da consulta.
4. A descrição (prompt) é armazenada no banco de dados PostgreSQL para controle e análise futura.
5. Tudo é apresentado em abas e com opção de **download** no formato `.sql`.

---

## 📁 Estrutura dos Arquivos

📦 dsa-sql-generator/
│
├── streamlit_app.py # Aplicação principal com interface Streamlit
├── db_utils.py # Módulo de persistência dos prompts no banco
├── .env # Variáveis de ambiente (NÃO subir ao GitHub)
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo :)


---

## 🔒 Segurança

As **credenciais do banco de dados** e **API Key da Gemini** são armazenadas em um arquivo `.env` (não incluso no repositório público).  
O acesso a essas informações é feito via `os.getenv()`.

### Exemplo de `.env` (não compartilhar publicamente):

```env
GOOGLE_API_KEY=your_google_api_key
DB_USER=your_user
DB_PASS=your_password
DB_HOST=your_host
DB_PORT=5432
DB_NAME=your_db


🚀 Executando Localmente
Clone este repositório:
git clone https://github.com/seuusuario/dsa-sql-generator.git
cd dsa-sql-generator

💾 Banco de Dados
Os prompts inseridos são armazenados na tabela prompts com o timestamp do acesso.

A conexão é feita via SQLAlchemy com autenticação segura (SSL).

O banco utilizado está hospedado no Neon, uma solução moderna e escalável para PostgreSQL na nuvem.

📬 Contato
Desenvolvido por Alex Felipe Barbosa
🔗 LinkedIn

