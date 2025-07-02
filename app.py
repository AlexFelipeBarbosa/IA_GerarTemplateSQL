## Alex Felipe Barbosa - 02/07/2025
## Projeto do Curso de Analista de Dados da Data Science Academy
## SQL Para Análise de Dados e Data Science
## Projeto Especial - DSA AI SQL Query Generator Text-to-SQL

# Imports
import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Importa função para salvar no banco
from db_utils import salvar_prompt

# Carrega o arquivo de variáveis de ambiente
load_dotenv()   

# Carrega a variável de ambiente da API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configura a chamada ao modelo via API
genai.configure(api_key=GOOGLE_API_KEY)

# Cria instância do modelo de IA
modelo_ai = genai.GenerativeModel('gemini-2.0-flash')

# Função para gerar a resposta do modelo de IA
def gera_resposta_modelo(prompt):

    # Tenta executar o bloco abaixo e capturar possíveis erros
    try:
        # Envia o prompt ao modelo de IA para gerar conteúdo
        response = modelo_ai.generate_content(prompt)

        # Retorna o texto da resposta, removendo espaços e blocos markdown com ```sql
        return response.text.strip().lstrip("```sql").rstrip("```")

    # Captura qualquer exceção que ocorrer durante a geração do conteúdo
    except Exception as e:

        # Exibe uma mensagem de erro ao usuário com detalhes da exceção capturada
        st.error(f"Erro ao gerar resposta: {str(e)}")

        # Retorna None indicando que houve falha na geração da resposta
        return None

# Função para download do resultado do modelo
def download_resultado(sql_query, e_output, explicacao):
    
    # Formata o conteúdo a ser baixado, incluindo consulta SQL, saída esperada e explicação
    conteudo = f"Consulta SQL:\n{sql_query}\n\nSaída Esperada:\n{e_output}\n\nExplicação:\n{explicacao}"
    
    # Cria e exibe um botão que permite ao usuário baixar o conteúdo formatado como arquivo .sql
    st.download_button("Baixar Resultado", conteudo, file_name = "resultado_query.sql", mime = "text/plain")

# Função principal
def main():

    # Configuração da página
    st.set_page_config(page_title="Alex Felipe Barbosa - Gerador de Modelo SQL", page_icon=":desktop_computer:", layout="wide")

    # Sidebar com instruções
    with st.sidebar:
        st.markdown(
            "<h1 style='color:darkblue;'>👋 Alex Felipe Barbosa</h1>",
            unsafe_allow_html=True
        )
        st.header("📊 Projeto do Curso de Analista de Dados")
        st.header("📋 Instruções")
        st.markdown("""
        - 📝 Digite uma **descrição clara** da query SQL desejada.
        - 🔍 Clique no botão **\"Gerar Query SQL\"**.
        - 🤖 A IA vai gerar:
        - 📄 O template da consulta SQL.
        - 🖥️ Um exemplo da saída esperada.
        - 📚 Uma explicação da sintaxe da query.
        - 💡 Quanto melhor o contexto, melhor a saída.
        - ⚠️ IA pode cometer erros. **Sempre** verifique os resultados com seu conhecimento.
        """)
        st.markdown(
            "[🔗 Meu LinkedIn](https://www.linkedin.com/in/seu-usuario/)",
            unsafe_allow_html=True
        )

        if st.button("✉️ Contato"):
            st.write("🔗 LinkedIn: https://www.linkedin.com/in/alexfelipebarbosa/")


    # Título principal
    st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: darkblue;">🚀 Gerador de Template de Query SQL</h1>
        <h2>💬 Text-to-SQL</h2>
        <hr style="margin:20px 0;">
        <h3 style="color: darkblue;">🤖 Sou um Assistente de Inteligência Artificial criado para facilitar sua vida com SQL!</h3>
        <h5>✨ Gere automaticamente <strong>templates de queries SQL</strong> sob medida para sua necessidade.</h5>
        <h5>📖 Além disso, receba <em>explicações claras</em> sobre a sintaxe utilizada e baixe o arquivo <code>.sql</code> pronto para uso.</h5>
        <h5>⚡ Tudo de forma rápida, prática e inteligente.</h5>
        <hr style="margin:20px 0;">
    </div>
    """,
    unsafe_allow_html=True,
)

    # Input do usuário
    text_input = st.text_area("Descreva, em português, a query SQL que deseja:")

    # Botão de envio
    submit = st.button(label='Gerar Query SQL')

    if submit:
        if len(text_input.strip()) < 15:
            st.warning("Por favor, forneça uma descrição mais detalhada.")
            return

        # Processamento com spinner
        with st.spinner("A IA está gerando o resultado. Aguarde..."):

            # Gera a resposta do modelo
            sql_query = gera_resposta_modelo(f"Crie de forma clara, objetiva e profissional, uma consulta SQL baseada neste texto: {text_input}")

            # Salva prompt no banco
            try:
                salvar_prompt(text_input)
            except Exception as e:
                st.warning(f"Erro ao salvar prompt no banco: {e}")

            # Se a primeira resposta foi gerada, seguimos usando IA para gerar as demais saídas 
            if sql_query:

                # Exemplo de saída da query
                e_output = gera_resposta_modelo(f"Mostre um exemplo da saída esperada para: {sql_query}")

                # Explicação
                explicacao = gera_resposta_modelo(f"Avalie e detalhe a explicação da sintaxe desta consulta SQL, descrevendo cada cláusula e função utilizada: {sql_query}")

                # Criar abas para exibir os resultados
                tab1, tab2, tab3 = st.tabs(["Consulta SQL", "Saída Esperada", "Explicação"])

                with tab1:
                    st.code(sql_query, language="sql")

                with tab2:
                    st.markdown(e_output)

                with tab3:
                    st.markdown(explicacao)

                # Opção de download
                download_resultado(sql_query, e_output, explicacao)

# Executa a aplicação
main()