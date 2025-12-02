import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title("📊 Checkpoint 3: Visualização de Dados")

st.markdown("""
### Objetivo
Criar gráficos interativos para explorar os dados.
""")

# Carregar dados
try:
    df = pd.read_csv('../data/safras.csv')
    
    # Opções de visualização
    st.sidebar.header("📊 Opções de Visualização")
    tipo_grafico = st.sidebar.selectbox(
        "Escolha o tipo de gráfico:",
        ["Distribuição", "Dispersão", "Box Plot", "Correlação"]
    )
    
    if tipo_grafico == "Distribuição":
        st.subheader("📈 Distribuição da Produção")
        fig = px.histogram(df, x='producao_toneladas', nbins=20,
                          title="Distribuição da Produção (toneladas)")
        fig.add_vline(x=df['producao_toneladas'].mean(), line_dash="dash", 
                     annotation_text=f"Média: {df['producao_toneladas'].mean():.1f}")
        st.plotly_chart(fig, use_container_width=True)
        
        # Distribuição da área
        fig_area = px.histogram(df, x='area_hectares', nbins=20,
                               title="Distribuição da Área (hectares)")
        st.plotly_chart(fig_area, use_container_width=True)
        
    elif tipo_grafico == "Dispersão":
        st.subheader("📊 Gráficos de Dispersão")
        
        # Selecionar variáveis
        col_x = st.selectbox("Variável X:", df.select_dtypes(include=['number']).columns)
        col_y = st.selectbox("Variável Y:", df.select_dtypes(include=['number']).columns, 
                           index=1)
        
        fig = px.scatter(df, x=col_x, y=col_y, color='tipo_solo',
                        title=f"{col_y} vs {col_x}")
        st.plotly_chart(fig, use_container_width=True)
        
    elif tipo_grafico == "Box Plot":
        st.subheader("📦 Box Plots")
        
        # Box plot por tipo de solo
        fig_solo = px.box(df, x='tipo_solo', y='producao_toneladas',
                         title="Produção por Tipo de Solo")
        st.plotly_chart(fig_solo, use_container_width=True)
        
        # Box plot de variáveis numéricas
        variavel_num = st.selectbox("Variável para análise:", 
                                   df.select_dtypes(include=['number']).columns)
        fig_num = px.box(df, y=variavel_num, title=f"Distribuição de {variavel_num}")
        st.plotly_chart(fig_num, use_container_width=True)
        
    elif tipo_grafico == "Correlação":
        st.subheader("🔗 Análise de Correlação")
        
        # Matriz de correlação
        corr_matrix = df.corr(numeric_only=True)
        
        fig_corr = px.imshow(corr_matrix, text_auto=True, aspect="auto",
                            title="Matriz de Correlação")
        st.plotly_chart(fig_corr, use_container_width=True)
        
        # Heatmap detalhado
        st.subheader("📈 Correlações com Produção")
        corr_producao = corr_matrix['producao_toneladas'].sort_values(ascending=False)
        
        fig_corr_prod = px.bar(x=corr_producao.index, y=corr_producao.values,
                              title="Correlação com Produção")
        fig_corr_prod.update_xaxes(title="Variável")
        fig_corr_prod.update_yaxes(title="Correlação")
        st.plotly_chart(fig_corr_prod, use_container_width=True)
    
    # Estatísticas gerais
    st.sidebar.markdown("---")
    st.sidebar.subheader("📈 Estatísticas Gerais")
    
    for col in df.select_dtypes(include=['number']).columns:
        st.sidebar.write(f"**{col}:**")
        st.sidebar.write(f"- Média: {df[col].mean():.2f}")
        st.sidebar.write(f"- Mediana: {df[col].median():.2f}")
        st.sidebar.write(f"- Desvio: {df[col].std():.2f}")
        st.sidebar.write("")
    
except FileNotFoundError:
    st.error("❌ Arquivo 'safras.csv' não encontrado")
    st.info("Execute 'python setup_modelo.py' para gerar os dados.")