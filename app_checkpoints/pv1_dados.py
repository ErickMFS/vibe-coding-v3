import streamlit as st
import pandas as pd

st.title("🌾 Checkpoint 1: Carregamento de Dados")

st.markdown("""
### Objetivo
Carregar e exibir os dados da safra agrícola.
""")

# Carregar dados
try:
    df = pd.read_csv('../data/safras.csv')
    st.success("✅ Dados carregados com sucesso!")
    
    # Exibir informações básicas
    st.subheader("📋 Informações do Dataset")
    st.write(f"Total de registros: {len(df)}")
    st.write(f"Colunas: {', '.join(df.columns.tolist())}")
    
    # Exibir tabela
    st.subheader("📊 Primeiros Registros")
    st.dataframe(df.head())
    
    # Estatísticas básicas
    st.subheader("📈 Estatísticas Descritivas")
    st.dataframe(df.describe())
    
except FileNotFoundError:
    st.error("❌ Arquivo 'safras.csv' não encontrado na pasta 'data/'")
    st.info("Execute 'python setup_modelo.py' para gerar os dados.")