import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib

st.title("🔮 Checkpoint 5: Sistema de Previsão")

st.markdown("""
### Objetivo
Criar interface completa para previsão de produção.
""")

# Carregar recursos
try:
    df = pd.read_csv('../data/safras.csv')
    modelo_info = joblib.load('../models/modelo_mock.pkl')
    modelo = modelo_info['modelo']
    features = modelo_info['features']
    
    st.success("✅ Sistema carregado com sucesso!")
    
    # Formulário de entrada
    st.subheader("📝 Insira os Dados para Previsão")
    
    col1, col2 = st.columns(2)
    
    with col1:
        area_input = st.number_input(
            "Área (hectares):", 
            min_value=1.0, 
            max_value=1000.0, 
            value=100.0, 
            step=10.0,
            help="Área total da plantação"
        )
        
        precipitacao_input = st.number_input(
            "Precipitação (mm):", 
            min_value=100.0, 
            max_value=3000.0, 
            value=1000.0, 
            step=50.0,
            help="Precipitação anual média"
        )
        
        temperatura_input = st.number_input(
            "Temperatura Média (°C):", 
            min_value=10.0, 
            max_value=40.0, 
            value=25.0, 
            step=0.5,
            help="Temperatura média anual"
        )
    
    with col2:
        fertilizante_input = st.number_input(
            "Fertilizante (kg):", 
            min_value=0.0, 
            max_value=500.0, 
            value=150.0, 
            step=10.0,
            help="Quantidade de fertilizante utilizada"
        )
        
        tipo_solo_input = st.selectbox(
            "Tipo de Solo:",
            ['arenoso', 'argiloso', 'humuso'],
            help="Selecione o tipo de solo predominante"
        )
        
        # Análise de similaridade
        st.write("**Análise Rápida:**")
        similares = df[
            (abs(df['area_hectares'] - area_input) < area_input * 0.3) &
            (df['tipo_solo'] == tipo_solo_input)
        ]
        st.write(f"Casos similares encontrados: {len(similares)}")
    
    # Botão de previsão
    if st.button("🔮 Fazer Previsão", type="primary"):
        # Preparar dados
        dados_previsao = pd.DataFrame({
            'area_hectares': [area_input],
            'precipitacao_mm': [precipitacao_input],
            'temperatura_media': [temperatura_input],
            'fertilizante_kg': [fertilizante_input],
            'tipo_solo': [tipo_solo_input]
        })
        
        # Codificar tipo_solo
        dados_previsao_encoded = pd.get_dummies(dados_previsao, columns=['tipo_solo'], drop_first=True)
        
        # Garantir todas as features
        for feature in features:
            if feature not in dados_previsao_encoded.columns:
                dados_previsao_encoded[feature] = 0
        
        dados_previsao_encoded = dados_previsao_encoded[features]
        
        # Fazer previsão
        previsao = modelo.predict(dados_previsao_encoded)[0]
        
        # Exibir resultados
        st.success(f"🎯 **Previsão de Produção: {previsao:.1f} toneladas**")
        
        # Métricas derivadas
        produtividade = previsao / area_input
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Produção Total", f"{previsao:.1f} t")
        
        with col2:
            st.metric("Produtividade", f"{produtividade:.2f} t/ha")
        
        with col3:
            st.metric("Preço Estimado*", f"R$ {previsao * 80:.0f}")
        
        st.info("*Considerando preço médio de R$ 80/tonelada")
        
        # Análise comparativa
        st.subheader("📊 Análise Comparativa")
        
        # Comparar com média histórica
        media_historica = df['producao_toneladas'].mean()
        diff_percentual = ((previsao - media_historica) / media_historica) * 100
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Média Histórica", 
                f"{media_historica:.1f} t",
                delta=f"{diff_percentual:.1f}%"
            )
        
        with col2:
            if previsao > media_historica:
                st.success("📈 Acima da média histórica")
            else:
                st.warning("📉 Abaixo da média histórica")
        
        # Gráfico comparativo
        fig = go.Figure()
        
        # Casos similares
        if len(similares) > 0:
            fig.add_trace(go.Scatter(
                x=similares['area_hectares'],
                y=similares['producao_toneladas'],
                mode='markers',
                name='Casos Similares',
                marker=dict(size=8, color='blue', opacity=0.6)
            ))
        
        # Previsão atual
        fig.add_trace(go.Scatter(
            x=[area_input],
            y=[previsao],
            mode='markers',
            name='Sua Previsão',
            marker=dict(size=15, color='red', symbol='star')
        ))
        
        # Média geral
        fig.add_hline(y=media_historica, line_dash="dash", 
                     annotation_text=f"Média: {media_historica:.1f}")
        
        fig.update_layout(
            title="Comparação da Previsão",
            xaxis_title="Área (hectares)",
            yaxis_title="Produção (toneladas)"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Recomendações
        st.subheader("💡 Recomendações")
        
        if produtividade < 2.0:
            st.warning("⚠️ Produtividade baixa. Considere:")
            st.write("- Aumentar a quantidade de fertilizante")
            st.write("- Verificar a qualidade do solo")
            st.write("- Avaliar técnicas de irrigação")
        
        elif produtividade > 5.0:
            st.success("✅ Produtividade excelente! Mantenha:")
            st.write("- As práticas atuais de cultivo")
            st.write("- O manejo adequado do solo")
            st.write("- O controle de pragas e doenças")
        
        else:
            st.info("📊 Produtividade dentro da faixa normal")
            st.write("- Continue monitorando as condições")
            st.write("- Considere otimizações graduais")

except FileNotFoundError as e:
    if 'safras.csv' in str(e):
        st.error("❌ Arquivo 'safras.csv' não encontrado")
        st.info("Execute 'python setup_modelo.py' para gerar os dados.")
    else:
        st.error("❌ Arquivo do modelo não encontrado")
        st.info("Execute 'python setup_modelo.py' para gerar o modelo.")

except Exception as e:
    st.error(f"❌ Erro ao carregar recursos: {str(e)}")
    st.info("Verifique se os arquivos de dados e modelo existem.")