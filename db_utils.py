## Alex Felipe Barbosa - 02/07/2025
## Projeto do Curso de Analista de Dados da Data Science Academy
## SQL Para Análise de Dados e Data Science
## Projeto Especial - DSA AI SQL Query Generator Text-to-SQL

## Conexão com Banco de Dados 

import os
from sqlalchemy import create_engine, Table, Column, String, MetaData
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env 
load_dotenv()

# Configura conexão com o banco via variáveis de ambiente
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

if not all([DB_USER, DB_PASS, DB_HOST, DB_NAME]):
    raise Exception("Por favor, configure as variáveis de ambiente: DB_USER, DB_PASS, DB_HOST e DB_NAME")


DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require&channel_binding=require"


engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Define tabela para armazenar prompts
AcessosUsuarios = Table(
    "prompts", metadata,
    Column("prompt", String, nullable=False),
    Column("data_hora", String, nullable=False),
)

metadata.create_all(engine)

def salvar_prompt(prompt: str):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with engine.connect() as conn:
            ins = AcessosUsuarios.insert().values(prompt=prompt, data_hora=data_hora)
            result = conn.execute(ins)
            conn.commit()  # Garante commit da transação
        print(f"Registro inserido com sucesso: prompt='{prompt}' às {data_hora}")
    except SQLAlchemyError as e:
        print(f"Erro ao inserir registro no banco de dados: {e}")

