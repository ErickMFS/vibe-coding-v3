# 🚀 Guia Completo de Publicação no Streamlit Cloud

Este guia explica como publicar sua aplicação Streamlit gratuitamente na internet
usando o Streamlit Cloud.

---

## Índice

1. [Pré-requisitos](#1-pré-requisitos)
2. [Preparar o Repositório](#2-preparar-o-repositório)
3. [Criar Conta no Streamlit Cloud](#3-criar-conta-no-streamlit-cloud)
4. [Publicar a Aplicação](#4-publicar-a-aplicação)
5. [Configurações Avançadas](#5-configurações-avançadas)
6. [Resolução de Problemas](#6-resolução-de-problemas)
7. [Manutenção](#7-manutenção)

---

## 1. Pré-requisitos

Antes de começar, você precisa ter:

- [ ] Conta no **GitHub** (gratuita)
- [ ] Aplicação Streamlit funcionando localmente
- [ ] Arquivo `requirements.txt` com as dependências

### Verificar se a aplicação funciona localmente:

```bash
streamlit run app.py
```

Se abrir no navegador sem erros, está pronto para publicar!

---

## 2. Preparar o Repositório

### 2.1 Estrutura necessária

Seu repositório deve ter **no mínimo**:

```
meu-projeto/
├── app.py              ← Arquivo principal (obrigatório)
├── requirements.txt    ← Dependências (obrigatório)
└── ...                 ← Outros arquivos
```

### 2.2 Criar requirements.txt

Se ainda não tem, crie o arquivo com as dependências:

```bash
# Opção 1: Gerar automaticamente (pode incluir pacotes extras)
pip freeze > requirements.txt

# Opção 2: Criar manualmente (recomendado)
```

**Conteúdo recomendado do requirements.txt:**

```
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.18.0
scikit-learn>=1.3.0
joblib>=1.3.0
```

### 2.3 Verificar arquivos de dados

Se sua aplicação usa arquivos de dados:

```
meu-projeto/
├── app.py
├── requirements.txt
├── data/
│   └── safras.csv      ← Dados incluídos no repo
└── models/
    └── modelo.pkl      ← Modelo incluído no repo
```

**⚠️ Atenção com tamanho de arquivos:**
- GitHub tem limite de 100MB por arquivo
- Para arquivos maiores, use Git LFS ou hospede externamente

### 2.4 Enviar para o GitHub

```bash
# Se ainda não inicializou o Git
git init
git add .
git commit -m "Preparar para publicação"

# Criar repositório no GitHub (via site) e conectar
git remote add origin https://github.com/seu-usuario/seu-projeto.git
git branch -M main
git push -u origin main
```

---

## 3. Criar Conta no Streamlit Cloud

### 3.1 Acessar o site

1. Acesse: **https://share.streamlit.io**
2. Clique em **"Sign up"** ou **"Get started"**

### 3.2 Conectar com GitHub

1. Clique em **"Continue with GitHub"**
2. Autorize o Streamlit a acessar sua conta
3. Selecione quais repositórios o Streamlit pode acessar:
   - **Todos os repositórios** (mais fácil)
   - **Apenas repositórios selecionados** (mais seguro)

### 3.3 Completar cadastro

1. Preencha seu nome
2. Preencha seu e-mail
3. Aceite os termos de uso
4. Clique em **"Continue"**

---

## 4. Publicar a Aplicação

### 4.1 Iniciar nova publicação

1. No painel do Streamlit Cloud, clique em **"New app"**
2. Você verá um formulário com 3 campos principais

### 4.2 Preencher informações

| Campo | O que preencher |
|-------|-----------------|
| **Repository** | Selecione seu repositório da lista |
| **Branch** | Geralmente `main` ou `master` |
| **Main file path** | Nome do arquivo principal (ex: `app.py`) |

### 4.3 Configurações opcionais

Clique em **"Advanced settings"** para:

- **Python version**: Escolha a versão (recomendado: 3.10 ou 3.11)
- **Secrets**: Adicionar variáveis secretas (senhas, chaves de API)

### 4.4 Publicar

1. Clique em **"Deploy!"**
2. Aguarde o processo (2-5 minutos na primeira vez)
3. Acompanhe o log de instalação

### 4.5 Acessar sua aplicação

Quando a publicação terminar, você receberá uma URL como:

```
https://seu-usuario-nome-do-app.streamlit.app
```

**Esta URL é pública!** Qualquer pessoa com o link pode acessar.

---

## 5. Configurações Avançadas

### 5.1 Personalizar a URL

Você pode escolher um nome personalizado:
- Nas configurações do app, edite o campo **"App URL"**
- Escolha algo como: `dashboard-safras.streamlit.app`

### 5.2 Variáveis de Ambiente (Secrets)

Para informações sensíveis (senhas, chaves de API):

1. No painel do app, clique em **"Settings"**
2. Vá para **"Secrets"**
3. Adicione no formato TOML:

```toml
# Exemplo de secrets
[database]
host = "meu-servidor.com"
password = "senha-secreta"

[api]
key = "minha-chave-de-api"
```

4. No código Python, acesse com:

```python
import streamlit as st

db_password = st.secrets["database"]["password"]
api_key = st.secrets["api"]["key"]
```

### 5.3 Arquivo de configuração (.streamlit/config.toml)

Crie este arquivo para personalizar a aparência:

```toml
[theme]
primaryColor = "#276749"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#1a202c"
font = "sans serif"

[server]
headless = true
port = 8501
```

---

## 6. Resolução de Problemas

### ❌ Erro: "ModuleNotFoundError"

**Causa**: Pacote não está no requirements.txt

**Solução**: Adicione o pacote ao requirements.txt e faça push

```bash
echo "nome-do-pacote>=1.0.0" >> requirements.txt
git add requirements.txt
git commit -m "Adicionar dependência"
git push
```

### ❌ Erro: "FileNotFoundError"

**Causa**: Arquivo não existe ou caminho errado

**Soluções**:
1. Verifique se o arquivo está no repositório
2. Use caminhos relativos (não absolutos)
3. Lembre que Linux é case-sensitive (`Data/` ≠ `data/`)

### ❌ Erro: "No module named 'sklearn'"

**Causa**: Nome do pacote diferente

**Solução**: Use `scikit-learn` no requirements.txt (não `sklearn`)

### ❌ Aplicação demora muito para carregar

**Causas e soluções**:
1. **Modelo muito grande**: Hospede o modelo externamente
2. **Dados muito grandes**: Use amostra menor ou banco de dados
3. **Sem cache**: Adicione `@st.cache_data` e `@st.cache_resource`

### ❌ Erro: "Your app has exceeded the resource limits"

**Causa**: Plano gratuito tem limites de memória

**Soluções**:
1. Otimize o código para usar menos memória
2. Carregue dados sob demanda
3. Considere upgrade para plano pago

### ❌ Aplicação não atualiza após push

**Soluções**:
1. Clique em **"Reboot app"** nas configurações
2. Verifique se o push foi para o branch correto
3. Aguarde alguns minutos (pode haver delay)

---

## 7. Manutenção

### 7.1 Atualizar a aplicação

Toda vez que você fizer push para o branch configurado, 
o Streamlit Cloud automaticamente atualiza a aplicação.

```bash
# Fazer alterações
git add .
git commit -m "Atualizar aplicação"
git push
```

Aguarde 1-2 minutos para a atualização completar.

### 7.2 Ver logs

1. No painel do Streamlit Cloud, clique na sua aplicação
2. Clique em **"Manage app"** (canto inferior direito)
3. Selecione **"Logs"**

### 7.3 Reiniciar a aplicação

Se a aplicação travar ou apresentar problemas:

1. Vá para **"Manage app"**
2. Clique em **"Reboot app"**

### 7.4 Excluir a aplicação

1. Vá para **"Settings"**
2. Role até o final
3. Clique em **"Delete app"**
4. Confirme a exclusão

---

## 8. Limites do Plano Gratuito

| Recurso | Limite Gratuito |
|---------|-----------------|
| Aplicações públicas | Ilimitadas |
| Aplicações privadas | 1 |
| Memória RAM | 1 GB |
| CPU | Compartilhada |
| Banda | Ilimitada |
| Inatividade | Dorme após 7 dias sem uso |

### Sobre a inatividade:

- Apps gratuitas "dormem" após 7 dias sem visitas
- Ao acessar novamente, demora ~30 segundos para "acordar"
- Para manter sempre ativa, configure um serviço de ping externo

---

## Checklist Final

Antes de compartilhar sua aplicação:

- [ ] Aplicação funciona localmente
- [ ] requirements.txt está atualizado
- [ ] Todos os arquivos estão no repositório
- [ ] Repositório está no GitHub
- [ ] Publicação no Streamlit Cloud completou sem erros
- [ ] URL funciona em janela anônima do navegador
- [ ] Testou todas as funcionalidades na versão publicada

---

## Recursos Adicionais

- [Documentação oficial do Streamlit Cloud](https://docs.streamlit.io/streamlit-community-cloud)
- [Fórum da comunidade Streamlit](https://discuss.streamlit.io/)
- [Galeria de aplicações](https://streamlit.io/gallery)

---

**🎉 Parabéns! Sua aplicação está na internet!**

Compartilhe a URL com colegas, gestores e qualquer pessoa que precise usar sua ferramenta.