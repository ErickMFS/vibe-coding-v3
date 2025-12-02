import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib

st.title("🤖 Checkpoint 4: Carregamento do Modelo")

st.markdown("""
### Objetivo
Carregar o modelo treinado e exibir informações sobre ele.
""")

# Carregar dados
try:
    df = pd.read_csv('../data/safras.csv')
    
    # Carregar modelo
    try:
        modelo_info = joblib.load('../models/modelo_mock.pkl')
        modelo = modelo_info['modelo']
        features = modelo_info['features']
        
        st.success("✅ Modelo carregado com sucesso!")
        
        # Informações do modelo
        st.subheader("🔧 Informações do Modelo")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Tipo de Modelo", type(modelo).__name__)
            st.metric("Número de Features", len(features))
            
        with col2:
            if hasattr(modelo, 'n_estimators'):
                st.metric("Número de Estimadores", modelo.n_estimators)
            if hasattr(modelo, 'max_depth'):
                st.metric("Profundidade Máxima", modelo.max_depth)
        
        # Features do modelo
        st.subheader("📋 Features Utilizadas")
        st.write(features)
        
        # Importância das features (se disponível)
        if hasattr(modelo, 'feature_importances_'):
            st.subheader("🎯 Importância das Features")
            
            feature_importance = pd.DataFrame({
                'feature': features,
                'importance': modelo.feature_importances_
            }).sort_values('importance', ascending=False)
            
            fig = px.bar(feature_importance.head(10), 
                        x='importance', y='feature',
                        title="Top 10 Features Mais Importantes",
                        orientation='h')
            st.plotly_chart(fig, use_container_width=True)
            
            # Tabela de importância
            st.dataframe(feature_importance, use_container_width=True)
        
        # Simulação de previsão
        st.subheader("🔮 Teste do Modelo")
        
        st.write("Selecione um registro para testar o modelo:")
        
        # Selecionar amostra
        amostra_index = st.selectbox(
            "Selecione um registro:",
            range(len(df)),
            format_func=lambda x: f"Registro {x+1}"
        )
        
        amostra = df.iloc[amostra_index:amostra_index+1]
        st.write("Dados selecionados:")
        st.dataframe(amostra)
        
        if st.button("🔮 Fazer Previsão"):
            # Preparar dados
            dados_previsao = amostra.copy()
            dados_previsao_encoded = pd.get_dummies(dados_previsao, columns=['tipo_solo'], drop_first=True)
            
            # Garantir todas as features
            for feature in features:
                if feature not in dados_previsao_encoded.columns:
                    dados_previsao_encoded[feature] = 0
            
            dados_previsao_encoded = dados_previsao_encoded[features]
            
            # Fazer previsão
            previsao = modelo.predict(dados_previsao_encoded)[0]
            valor_real = amostra['producao_toneladas'].iloc[0]
            erro = abs(previsao - valor_real)
            erro_percentual = (erro / valor_real) * 100
            
            # Exibir resultados
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Valor Real", f"{valor_real:.1f} t")
            
            with col2:
                st.metric("Previsto", f"{previsao:.1f} t")
            
            with col3:
                st.metric("Erro", f"{erro:.1f} t ({erro_percentual:.1f}%)")
            
            if erro_percentual < 10:
                st.success("✅ Previsão muito precisa!")
            elif erro_percentual < 20:
                st.info("⚠️ Previsão razoável")
            else:
                st.warning("❌ Previsão com erro elevado")
    
    except FileNotFoundError:
        st.error("❌ Arquivo do modelo não encontrado")
        st.info("Execute 'python setup_modelo.py' para gerar o modelo.")
    
except FileNotFoundError:
    st.error("❌ Arquivo 'safras.csv' não encontrado")
    st.info("Execute 'python setup_modelo.py' para gerar os dados.")