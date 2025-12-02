import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib
from datetime import datetime

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Dashboard de Safras",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# FUNÇÕES DE CARREGAMENTO (COM CACHE)
# ============================================================

@st.cache_data
def carregar_dados():
    """Carrega e retorna os dados de safras."""
    return pd.read_csv("data/safras.csv")


@st.cache_resource
def carregar_modelo():
    """Carrega o modelo de ML."""
    try:
        return joblib.load("models/modelo_mock.pkl")
    except FileNotFoundError:
        return None


# ============================================================
# CARREGAR DADOS E MODELO
# ============================================================

df = carregar_dados()
modelo = carregar_modelo()

# ============================================================
# SIDEBAR - FILTROS E STATUS
# ============================================================

st.sidebar.image("https://via.placeholder.com/150x50/276749/ffffff?text=MAPA", width=150)
st.sidebar.title("🌾 Dashboard de Safras")
st.sidebar.markdown("---")

# Filtros
st.sidebar.header("🔍 Filtros")

# Lista de opções únicas
culturas = ["Todas"] + sorted(df["cultura"].unique().tolist())
estados = ["Todos"] + sorted(df["estado"].unique().tolist())
anos = ["Todos"] + sorted(df["ano"].unique().tolist(), reverse=True)

# Widgets de filtro
cultura_selecionada = st.sidebar.selectbox("Cultura", culturas)
estado_selecionado = st.sidebar.selectbox("Estado", estados)
ano_selecionado = st.sidebar.selectbox("Ano", anos)

# Aplicar filtros
df_filtrado = df.copy()

if cultura_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["cultura"] == cultura_selecionada]

if estado_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["estado"] == estado_selecionado]

if ano_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["ano"] == ano_selecionado]

# Indicador de filtros ativos
filtros_ativos = []
if cultura_selecionada != "Todas":
    filtros_ativos.append(f"Cultura: {cultura_selecionada}")
if estado_selecionado != "Todos":
    filtros_ativos.append(f"Estado: {estado_selecionado}")
if ano_selecionado != "Todos":
    filtros_ativos.append(f"Ano: {ano_selecionado}")

if filtros_ativos:
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Filtros ativos:**")
    for filtro in filtros_ativos:
        st.sidebar.markdown(f"• {filtro}")
    
    if st.sidebar.button("🗑️ Limpar Filtros"):
        st.rerun()

# Status do modelo
st.sidebar.markdown("---")
st.sidebar.header("🤖 Modelo ML")

if modelo is not None:
    st.sidebar.success("✅ Modelo carregado")
    st.sidebar.caption("RandomForest - modelo_mock.pkl")
else:
    st.sidebar.error("❌ Modelo não disponível")
    st.sidebar.caption("Execute: python setup_modelo.py")

# ============================================================
# CONTEÚDO PRINCIPAL
# ============================================================

# Título
st.title("🌾 Dashboard de Previsão de Safras")
st.markdown("Visualização e previsão de produtividade agrícola brasileira")

# ============================================================
# MÉTRICAS RESUMO
# ============================================================

st.header("📊 Resumo")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label="Total de Registros",
        value=f"{len(df_filtrado):,}"
    )

with col2:
    st.metric(
        label="Culturas",
        value=df_filtrado["cultura"].nunique()
    )

with col3:
    st.metric(
        label="Estados",
        value=df_filtrado["estado"].nunique()
    )

with col4:
    producao_total = df_filtrado["producao_toneladas"].sum()
    if producao_total >= 1e9:
        producao_fmt = f"{producao_total/1e9:.1f}B ton"
    else:
        producao_fmt = f"{producao_total/1e6:.1f}M ton"
    st.metric(
        label="Produção Total",
        value=producao_fmt
    )

with col5:
    area_total = df_filtrado["area_hectares"].sum()
    st.metric(
        label="Área Total",
        value=f"{area_total/1e6:.1f}M ha"
    )

# ============================================================
# DADOS E GRÁFICOS
# ============================================================

st.header("📈 Dados e Visualizações")

tab1, tab2, tab3 = st.tabs(["📋 Tabela", "📊 Por Estado", "📈 Evolução"])

with tab1:
    # Tabela de dados
    st.subheader("Dados Detalhados")
    
    # Formatar colunas numéricas
    df_display = df_filtrado.copy()
    df_display["area_hectares"] = df_display["area_hectares"].apply(lambda x: f"{x:,.0f}")
    df_display["producao_toneladas"] = df_display["producao_toneladas"].apply(lambda x: f"{x:,.0f}")
    df_display["produtividade"] = df_display["produtividade"].apply(lambda x: f"{x:,.0f}")
    
    st.dataframe(
        df_display,
        use_container_width=True,
        height=400,
        column_config={
            "id": st.column_config.NumberColumn("ID", width="small"),
            "cultura": st.column_config.TextColumn("Cultura", width="medium"),
            "estado": st.column_config.TextColumn("UF", width="small"),
            "ano": st.column_config.NumberColumn("Ano", width="small"),
            "area_hectares": st.column_config.TextColumn("Área (ha)", width="medium"),
            "producao_toneladas": st.column_config.TextColumn("Produção (ton)", width="medium"),
            "produtividade": st.column_config.TextColumn("Produtiv. (kg/ha)", width="medium"),
            "temperatura_media": st.column_config.NumberColumn("Temp (°C)", width="small"),
            "precipitacao_mm": st.column_config.NumberColumn("Chuva (mm)", width="small"),
        }
    )

with tab2:
    # Gráfico por estado
    st.subheader("Produção por Estado")
    
    col_g1, col_g2 = st.columns(2)
    
    with col_g1:
        # Barras horizontais
        df_estado = df_filtrado.groupby("estado")["producao_toneladas"].sum().reset_index()
        df_estado = df_estado.sort_values("producao_toneladas", ascending=True)
        
        fig_bar = px.bar(
            df_estado,
            x="producao_toneladas",
            y="estado",
            orientation="h",
            color="estado",
            labels={
                "producao_toneladas": "Produção (toneladas)",
                "estado": "Estado"
            },
            title="Produção Total por Estado"
        )
        fig_bar.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col_g2:
        # Pizza
        fig_pie = px.pie(
            df_estado,
            values="producao_toneladas",
            names="estado",
            title="Distribuição da Produção"
        )
        fig_pie.update_layout(height=400)
        st.plotly_chart(fig_pie, use_container_width=True)

with tab3:
    # Evolução temporal
    st.subheader("Evolução Temporal")
    
    df_temporal = df_filtrado.groupby(["ano", "cultura"])["producao_toneladas"].sum().reset_index()
    
    fig_linha = px.line(
        df_temporal,
        x="ano",
        y="producao_toneladas",
        color="cultura",
        markers=True,
        labels={
            "producao_toneladas": "Produção (toneladas)",
            "ano": "Ano",
            "cultura": "Cultura"
        },
        title="Evolução da Produção por Cultura"
    )
    fig_linha.update_layout(height=400)
    st.plotly_chart(fig_linha, use_container_width=True)

# ============================================================
# PREVISÃO COM ML
# ============================================================

st.header("🔮 Previsão de Produção")

if modelo is None:
    st.warning("""
    ⚠️ Modelo de Machine Learning não disponível.
    
    Para usar a previsão, execute no terminal:
    ```
    python setup_modelo.py
    ```
    """)
else:
    st.markdown("""
    Insira os parâmetros abaixo para obter uma previsão de produção 
    baseada no modelo de Machine Learning.
    """)
    
    # Formulário de entrada
    col_input1, col_input2, col_input3 = st.columns(3)
    
    with col_input1:
        cultura_pred = st.selectbox(
            "Cultura",
            ["Soja", "Milho", "Café", "Algodão", "Cana"],
            key="pred_cultura",
            help="Selecione a cultura para previsão"
        )
        
        area_pred = st.number_input(
            "Área plantada (hectares)",
            min_value=100,
            max_value=15000000,
            value=1000000,
            step=100000,
            help="Área total de plantio"
        )
    
    with col_input2:
        estado_pred = st.selectbox(
            "Estado",
            ["MT", "PR", "GO", "MS", "MG", "SP", "BA", "RS", "SC", "ES"],
            key="pred_estado",
            help="Estado de produção"
        )
        
        temperatura_pred = st.slider(
            "Temperatura média (°C)",
            min_value=15.0,
            max_value=35.0,
            value=25.0,
            step=0.5,
            help="Temperatura média anual esperada"
        )
    
    with col_input3:
        ano_pred = st.number_input(
            "Ano da safra",
            min_value=2024,
            max_value=2030,
            value=2025,
            help="Ano de referência"
        )
        
        precipitacao_pred = st.slider(
            "Precipitação anual (mm)",
            min_value=500,
            max_value=2500,
            value=1400,
            step=50,
            help="Precipitação anual esperada"
        )
    
    # Botão de previsão
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    
    with col_btn2:
        btn_prever = st.button(
            "🚀 Calcular Previsão",
            type="primary",
            use_container_width=True
        )
    
    # Executar previsão
    if btn_prever:
        with st.spinner("Calculando previsão..."):
            try:
                # Preparar entrada (features que o modelo espera)
                X = [[area_pred, temperatura_pred, precipitacao_pred]]
                
                # Fazer previsão
                predicao = modelo.predict(X)[0]
                
                # Calcular produtividade
                produtividade = predicao / area_pred if area_pred > 0 else 0
                
                # Exibir resultado
                st.markdown("---")
                
                col_res1, col_res2, col_res3 = st.columns(3)
                
                with col_res1:
                    st.metric(
                        label="🎯 Produção Estimada",
                        value=f"{predicao:,.0f} ton"
                    )
                
                with col_res2:
                    st.metric(
                        label="📊 Produtividade",
                        value=f"{produtividade:,.0f} kg/ha"
                    )
                
                with col_res3:
                    # Comparar com média histórica da cultura
                    media_hist = df[df["cultura"] == cultura_pred]["produtividade"].mean()
                    delta = ((produtividade - media_hist) / media_hist * 100) if media_hist > 0 else 0
                    st.metric(
                        label="📈 vs. Média Histórica",
                        value=f"{produtividade:,.0f}",
                        delta=f"{delta:+.1f}%"
                    )
                
                # Mensagem de sucesso
                st.success(f"""
                **Previsão realizada com sucesso!**
                
                Para {cultura_pred} em {estado_pred} ({ano_pred}):
                - Área: {area_pred:,} hectares
                - Produção estimada: **{predicao:,.0f} toneladas**
                - Produtividade: {produtividade:,.0f} kg/ha
                """)
                
                # Balões de celebração
                st.balloons()
                
            except Exception as e:
                st.error(f"Erro na previsão: {str(e)}")

# ============================================================
# RODAPÉ
# ============================================================

st.markdown("---")

col_footer1, col_footer2, col_footer3 = st.columns(3)

with col_footer1:
    st.markdown("**🌾 Dashboard de Safras v3.0**")
    st.caption("Curso Vibe Coding Estruturado")

with col_footer2:
    st.markdown("**📊 Dados**")
    st.caption("Fonte: Dados simulados para fins educacionais")

with col_footer3:
    st.markdown("**🕐 Atualizado**")
    st.caption(datetime.now().strftime("%d/%m/%Y %H:%M"))