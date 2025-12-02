# Troubleshooting - Sistema de Previsão de Safras

## Problemas Comuns e Soluções

### 1. Arquivos Não Encontrados

**Erro:** `FileNotFoundError: [Errno 2] No such file or directory: 'data/safras.csv'`

**Solução:**
```bash
python setup_modelo.py
```

### 2. Dependências Faltando

**Erro:** `ModuleNotFoundError: No module named 'pandas'`

**Solução:**
```bash
pip install -r requirements.txt
```

**Alternativa (ambiente virtual):**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Streamlit Não Inicia

**Erro:** `streamlit: command not found`

**Solução:**
```bash
pip install streamlit
```

**Verificar instalação:**
```bash
streamlit --version
```

### 4. Modelo Não Carrega

**Erro:** `FileNotFoundError: [Errno 2] No such file or directory: 'models/modelo_mock.pkl'`

**Solução:**
```bash
# Garanta que o diretório models existe
mkdir -p models
python setup_modelo.py
```

### 5. Erro de Permissão

**Erro:** `PermissionError: [Errno 13] Permission denied`

**Solução:**
```bash
# Linux/Mac
chmod +x setup_modelo.py

# Ou use python3 em vez de python
python3 setup_modelo.py
```

### 6. Conflito de Versões

**Erro:** `ImportError: cannot import name '...' from '...'`

**Solução:**
```bash
# Atualize dependências
pip install --upgrade -r requirements.txt

# Ou reinstale tudo
pip uninstall -y -r requirements.txt
pip install -r requirements.txt
```

### 7. Porta Ocupada

**Erro:** `Port 8501 is already in use`

**Solução:**
```bash
# Mate processos usando a porta
lsof -ti:8501 | xargs kill -9

# Ou use outra porta
streamlit run app_referencia.py --server.port 8502
```

### 8. Problemas de Cache

**Sintoma:** Dados não atualizam mesmo após alterações

**Solução:**
- Limpe cache do navegador
- Reinicie o Streamlit: Ctrl+C e execute novamente
- Limpe cache do Streamlit: delete pasta `.streamlit`

### 9. Erros de Formato CSV

**Erro:** `pandas.errors.ParserError: Error tokenizing data`

**Solução:**
```bash
# Recrie o arquivo CSV
python setup_modelo.py

# Ou verifique manualmente o formato do arquivo
head data/safras.csv
```

### 10. Problemas de Display no Jupyter

**Sintoma:** Gráficos não aparecem ou cortados

**Solução:**
```python
# Adicione ao início do notebook
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
```

## Comandos Úteis

### Verificar Estrutura de Arquivos
```bash
find . -name "*.py" -o -name "*.csv" -o -name "*.pkl" | sort
```

### Verificar Dependências
```bash
pip list | grep -E "(streamlit|pandas|numpy|sklearn|plotly)"
```

### Executar Teste Rápido
```bash
python -c "import streamlit, pandas, sklearn, plotly; print('OK')"
```

### Monitorar Recursos
```bash
# Uso de CPU e memória
htop

# Uso de disco
df -h

# Processos Python
ps aux | grep python
```

## Verificação de Saúde do Sistema

Crie um script `health_check.py`:
```python
import pandas as pd
import streamlit as st
import sklearn
import plotly
import joblib
import os

def check_system():
    print("🔍 Verificação de Saúde do Sistema")
    print("=" * 40)
    
    # Verificar arquivos
    arquivos_necessarios = [
        'data/safras.csv',
        'requirements.txt',
        'app_referencia.py',
        'app.py'
    ]
    
    for arquivo in arquivos_necessarios:
        if os.path.exists(arquivo):
            print(f"✅ {arquivo}")
        else:
            print(f"❌ {arquivo}")
    
    # Verificar pacotes
    pacotes = {
        'pandas': pd,
        'streamlit': st,
        'sklearn': sklearn,
        'plotly': plotly,
        'joblib': joblib
    }
    
    print("\n📦 Pacotes:")
    for nome, pacote in pacotes.items():
        try:
            versao = getattr(pacote, '__version__', 'desconhecida')
            print(f"✅ {nome}: {versao}")
        except:
            print(f"❌ {nome}: não instalado")

if __name__ == "__main__":
    check_system()
```

## Ambiente de Desenvolvimento

### VS Code
- Instale extensão: Python
- Instale extensão: Streamlit
- Use interprete Python correto

### Jupyter Notebook
```bash
pip install jupyter
jupyter notebook
```

### Docker (Opcional)
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "app_referencia.py"]
```

## Performance

### Otimização de Memória
```python
# Para datasets grandes
import pandas as pd
dtype_options = {
    'area_hectares': 'float32',
    'precipitacao_mm': 'float32',
    'producao_toneladas': 'float32'
}
df = pd.read_csv('data/safras.csv', dtype=dtype_options)
```

### Cache do Streamlit
```python
# Para processamentos pesados
@st.cache_data(ttl=3600)  # Cache por 1 hora
def processamento_pesado(df):
    # ... processamento
    return resultado
```

## Suporte e Comunidade

- **Streamlit Docs:** https://docs.streamlit.io/
- **Scikit-learn Docs:** https://scikit-learn.org/
- **Plotly Docs:** https://plotly.com/python/
- **Pandas Docs:** https://pandas.pydata.org/docs/

## Log de Erros

Para habilitar logging detalhado:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

Ou execute Streamlit com debug:
```bash
streamlit run app_referencia.py --logger.level debug
```