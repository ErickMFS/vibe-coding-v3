"""
Script para criar o modelo mock usado no curso.
Execute: python setup_modelo.py
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

def criar_modelo_mock():
    """Cria um modelo de regressão simples para demonstração."""
    
    print("🌾 Criando modelo mock para o curso...")
    
    # Carregar dados
    df = pd.read_csv("data/safras.csv")
    
    # Preparar features e target
    # O modelo usa: area, temperatura, precipitacao para prever producao
    X = df[["area_hectares", "temperatura_media", "precipitacao_mm"]].values
    y = df["producao_toneladas"].values
    
    # Dividir dados
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Treinar modelo
    modelo = RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    modelo.fit(X_train, y_train)
    
    # Avaliar
    score_train = modelo.score(X_train, y_train)
    score_test = modelo.score(X_test, y_test)
    
    print(f"   R² treino: {score_train:.4f}")
    print(f"   R² teste:  {score_test:.4f}")
    
    # Criar pasta se não existir
    os.makedirs("models", exist_ok=True)
    
    # Salvar modelo
    caminho = "models/modelo_mock.pkl"
    joblib.dump(modelo, caminho)
    
    print(f"✅ Modelo salvo em: {caminho}")
    
    # Testar predição
    exemplo = [[10000000, 25.0, 1400]]  # 10M ha, 25°C, 1400mm
    pred = modelo.predict(exemplo)[0]
    print(f"   Teste: {exemplo[0]} → {pred:,.0f} toneladas")
    
    return modelo


def verificar_modelo():
    """Verifica se o modelo existe e funciona."""
    
    caminho = "models/modelo_mock.pkl"
    
    if not os.path.exists(caminho):
        print(f"❌ Modelo não encontrado em {caminho}")
        return False
    
    try:
        modelo = joblib.load(caminho)
        pred = modelo.predict([[10000000, 25.0, 1400]])[0]
        print(f"✅ Modelo OK: predição teste = {pred:,.0f} ton")
        return True
    except Exception as e:
        print(f"❌ Erro ao carregar modelo: {e}")
        return False


if __name__ == "__main__":
    print("=" * 50)
    print("Setup do Modelo Mock - Curso Vibe Coding v3")
    print("=" * 50)
    print()
    
    # Verificar se dados existem
    if not os.path.exists("data/safras.csv"):
        print("❌ Arquivo data/safras.csv não encontrado!")
        print("   Certifique-se de estar na pasta correta do projeto.")
        exit(1)
    
    # Criar modelo
    criar_modelo_mock()
    
    print()
    print("=" * 50)
    print("Verificação final:")
    verificar_modelo()
    print("=" * 50)