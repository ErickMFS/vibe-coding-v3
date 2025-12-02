# 📦 Modelos de Machine Learning

Esta pasta contém os modelos usados na aplicação.

## Modelo Mock (modelo_mock.pkl)

Modelo RandomForest para demonstração no curso.

### Features esperadas:
| Feature | Tipo | Descrição | Range típico |
|---------|------|-----------|--------------|
| `area_hectares` | float | Área plantada em hectares | 100 - 15.000.000 |
| `temperatura_media` | float | Temperatura média em °C | 15 - 35 |
| `precipitacao_mm` | float | Precipitação anual em mm | 500 - 2500 |

### Output:
- `producao_toneladas`: Produção estimada em toneladas

### Exemplo de uso:
```python
import joblib

modelo = joblib.load("models/modelo_mock.pkl")

# Entrada: [area, temperatura, precipitação]
X = [[10000000, 25.0, 1400]]

# Predição
producao = modelo.predict(X)[0]
print(f"Produção estimada: {producao:,.0f} toneladas")
```