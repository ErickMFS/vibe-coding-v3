"""
🌾 Dashboard de Safras - Ponto de Partida

Este é o arquivo que você vai modificar durante o curso.
Siga os checkpoints para construir a aplicação completa.

Executar: streamlit run app.py
"""

import streamlit as st
import pandas as pd

# ============================================================
# CONFIGURAÇÃO INICIAL
# ============================================================

st.set_page_config(
    page_title="Dashboard de Safras",
    page_icon="🌾",
    layout="wide"
)

# ============================================================
# TÍTULO
# ============================================================

st.title("🌾 Meu Dashboard de Safras")
st.markdown("Vamos construir juntos!")

# ============================================================
# PRÓXIMOS PASSOS:
# 
# Checkpoint 1: Carregar e exibir dados
# Checkpoint 2: Adicionar filtros
# Checkpoint 3: Criar visualizações
# Checkpoint 4: Carregar modelo ML
# Checkpoint 5: Interface de previsão
#
# Se travar, copie o código do checkpoint:
# cp app_checkpoints/pv1_dados.py app.py
# ============================================================

st.info("""
👋 **Bem-vindo ao curso!**

Este é o ponto de partida. Durante o curso, vamos adicionar:

1. 📊 Carregamento de dados
2. 🔍 Filtros interativos
3. 📈 Gráficos e visualizações
4. 🤖 Integração com Machine Learning
5. 🔮 Interface de previsão

Siga as instruções do instrutor para começar!
""")