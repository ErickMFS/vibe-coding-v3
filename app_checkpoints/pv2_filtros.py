import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎛️ Checkpoint 2: Filtros de Dados")

st.markdown("""
### Objetivo
Adicionar filtros interativos para analisar os dados.
""")

# Carregar dados
try:
    df = pd.read_csv('../data/safras.csv')
    
    # Filtros na sidebar
    st.sidebar.header("🎛️ Filtros")
    
    # Filtro de área
    area_min, area_max = st.sidebar.slider(
        "Área (hectares):",
        float(df['area_hectares'].min()),
        float(df['area_hectares'].max()),
        (float(df['area_hectares'].min()), float(df['area_hectares'].max()))
    )
    
    # Filtro de precipitação
    precip_min, precip_max = st.sidebar.slider(
        "Precipitação (mm):",
        float(df['precipitacao_mm'].min()),
        float(df['precipitacao_mm'].max()),
        (float(df['precipitacao_mm'].min()), float(df['precipitacao_mm'].max()))
    )
    
    # Filtro de tipo de solo
    tipos_solo = st.sidebar.multiselect(
        "Tipo de Solo:",
        df['tipo_solo'].unique(),
        df['tipo_solo'].unique()
    )
    
    # Aplicar filtros
    df_filtrado = df[
        (df['area_hectares'] >= area_min) &
        (df['area_hectares'] <= area_max) &
        (df['precipitacao_mm'] >= precip_min) &
        (df['precipitacao_mm'] <= precip_max) &
        (df['tipo_solo'].isin(tipos_solo))
    ]
    
    # Exibir resultados
    st.subheader(f"📋 Dados Filtrados ({len(df_filtrado)} registros)")
    
    if len(df_filtrado) > 0:
        # Métricas
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Produção Média", f"{df_filtrado['producao_toneladas'].mean():.1f} t")
        
        with col2:
            st.metric("Área Média", f"{df_filtrado['area_hectares'].mean():.1f} ha")
        
        with col3:
            prod_media = df_filtrado['producao_toneladas'].mean() / df_filtrado['area_hectares'].mean()
            st.metric("Produtividade Média", f"{prod_media:.2f} t/ha")
        
        # Tabela filtrada
        st.subheader("📊 Tabela de Dados Filtrados")
        st.dataframe(df_filtrado)
        
        # Gráfico simples
        st.subheader("📈 Produção vs Área (Filtrado)")
        fig = px.scatter(df_filtrado, x='area_hectares', y='producao_toneladas', 
                        color='tipo_solo', title="Produção vs Área")
        st.plotly_chart(fig, use_container_width=True)
        
    else:
        st.warning("Nenhum dado encontrado com os filtros selecionados.")
    
except FileNotFoundError:
    st.error("❌ Arquivo 'safras.csv' não encontrado")
    st.info("Execute 'python setup_modelo.py' para gerar os dados.")