---
marp: true
theme: default
paginate: true
backgroundColor: #ffffff
color: #1a202c
style: |
  /* ===== CONFIGURAÇÃO GLOBAL COM MARGENS SEGURAS ===== */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=Fira+Code:wght@400;500&display=swap');
  
  :root {
    --color-primary: #1a365d;
    --color-primary-light: #2c5282;
    --color-secondary: #276749;
    --color-secondary-light: #38a169;
    --color-accent: #ed8936;
    --color-text: #1a202c;
    --color-text-light: #4a5568;
    --color-bg-light: #f7fafc;
    --color-bg-code: #0d1117;
  }
  
  section {
    font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
    padding: 50px 70px;
    font-size: 22px;
    line-height: 1.4;
  }
  
  h1 {
    color: var(--color-primary);
    font-weight: 900;
    font-size: 1.9em;
    margin-bottom: 0.4em;
    margin-top: 0;
  }
  
  h2 {
    color: var(--color-primary-light);
    font-weight: 700;
    font-size: 1.4em;
    margin-top: 0.3em;
  }
  
  h3 {
    color: var(--color-secondary);
    font-weight: 600;
    font-size: 1.1em;
    margin-bottom: 0.3em;
  }
  
  p, li {
    font-size: 0.95em;
    margin: 0.3em 0;
  }
  
  ul, ol {
    margin: 0.4em 0;
    padding-left: 1.5em;
  }
  
  code {
    font-family: 'Fira Code', 'Consolas', monospace;
    background: #1e293b;
    color: #22d3ee;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.85em;
  }
  
  pre {
    background: var(--color-bg-code);
    border-radius: 8px;
    padding: 14px 18px;
    margin: 0.5em 0;
    overflow-x: auto;
    border: 1px solid #30363d;
  }
  
  pre code {
    background: transparent;
    color: #e6edf3;
    font-size: 0.72em;
    line-height: 1.5;
    padding: 0;
  }
  
  /* ===== SYNTAX HIGHLIGHTING - ALTO CONTRASTE ===== */
  
  pre .comment { color: #8b949e; font-style: italic; }
  pre .keyword { color: #ff7b72; font-weight: 600; }
  pre .string { color: #a5d6ff; }
  pre .number { color: #79c0ff; }
  pre .function { color: #d2a8ff; }
  pre .variable { color: #ffa657; }
  pre .operator { color: #ff7b72; }
  pre .builtin { color: #7ee787; }
  pre .decorator { color: #7ee787; }
  
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.5em 0;
    font-size: 0.85em;
  }
  
  th {
    background: var(--color-primary);
    color: white;
    padding: 8px 12px;
    text-align: left;
    font-weight: 600;
  }
  
  td {
    padding: 6px 12px;
    border-bottom: 1px solid #e2e8f0;
  }
  
  tr:nth-child(even) {
    background: var(--color-bg-light);
  }
  
  blockquote {
    border-left: 4px solid var(--color-accent);
    margin: 0.5em 0;
    padding: 0.5em 1em;
    background: #fffaf0;
    font-style: italic;
    font-size: 0.95em;
  }
  
  blockquote p {
    margin: 0;
  }
  
  /* ===== CLASSES UTILITÁRIAS ===== */
  
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    align-items: start;
  }
  
  .columns-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 15px;
  }
  
  .box {
    background: var(--color-bg-light);
    border-radius: 8px;
    padding: 12px 16px;
    border-left: 4px solid var(--color-primary);
    font-size: 0.9em;
  }
  
  .box-success {
    background: #f0fff4;
    border-left-color: var(--color-secondary-light);
  }
  
  .box-warning {
    background: #fffaf0;
    border-left-color: var(--color-accent);
  }
  
  .box-danger {
    background: #fff5f5;
    border-left-color: #c53030;
  }
  
  .box-code {
    background: #0d1117;
    border-left-color: #7ee787;
    color: #e6edf3;
  }
  
  .prompt-box {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    border: 2px solid #7ee787;
    border-radius: 12px;
    padding: 16px 20px;
    color: #e6edf3;
    font-family: 'Fira Code', monospace;
    font-size: 0.85em;
  }
  
  .prompt-box strong {
    color: #7ee787;
  }
  
  .small {
    font-size: 0.8em;
    color: var(--color-text-light);
  }
  
  .center {
    text-align: center;
  }
  
  .big-number {
    font-size: 3em;
    font-weight: 900;
    color: var(--color-primary);
    line-height: 1;
  }
  
  .timer {
    background: var(--color-accent);
    color: white;
    padding: 4px 12px;
    border-radius: 15px;
    font-weight: 700;
    font-size: 0.85em;
  }
  
  .checkpoint {
    background: linear-gradient(135deg, #276749 0%, #38a169 100%);
    color: white;
    padding: 6px 16px;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.9em;
  }
  
  .claude-prompt {
    background: #1a1b26;
    border: 1px solid #7ee787;
    border-radius: 8px;
    padding: 12px 16px;
    font-family: 'Fira Code', monospace;
    font-size: 0.8em;
    color: #7ee787;
  }
  
  /* ===== SLIDES ESPECIAIS ===== */
  
  section.lead {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    padding: 60px 80px;
  }
  
  section.lead h1 {
    font-size: 2.4em;
    color: white;
    margin-bottom: 0.3em;
  }
  
  section.lead h2 {
    color: rgba(255,255,255,0.9);
    font-weight: 400;
    font-size: 1.3em;
  }
  
  section.invert {
    background: var(--color-primary);
    color: white;
  }
  
  section.invert h1,
  section.invert h2,
  section.invert h3 {
    color: white;
  }

---

<!-- _class: lead -->
<!-- _backgroundColor: #1a365d -->

# 🚀 Vibe Coding Estruturado

## De ideia a protótipo funcional na web em 3 horas

**Ministério da Agricultura, Pecuária e Abastecimento**

---

<!-- _class: lead -->
<!-- _backgroundColor: #276749 -->

# Ao final de hoje:

## Uma interface web funcionando
## publicada na internet
## para o seu modelo de Machine Learning

---

# O que vamos construir

<div class="center">

Um **Dashboard de Previsão de Safras** completo:

</div>

<div class="columns">

<div class="box">

### Funcionalidades
- 📊 Visualizar dados históricos
- 🔍 Filtrar por cultura/estado
- 📈 Gráficos interativos
- 🤖 Previsões com seu modelo ML

</div>

<div class="box box-success">

### Resultado
- Gerado pelo Claude Code
- Publicado na web gratuitamente
- Interface profissional
- Seu modelo integrado

</div>

</div>

---

# A diferença desta aula

<div class="columns">

<div class="box box-danger">

### ❌ Abordagem tradicional

- Copiar código dos slides
- Colar no editor
- Não dominar o que está fazendo
- Travar quando precisar modificar

</div>

<div class="box box-success">

### ✅ Nossa abordagem

- Dialogar com Claude Code
- Especificar o que deseja
- LLM gera documentação e código
- Você entende e ajusta
- Pede explicações para o LLM

</div>

</div>

<br>

> **Você aprende a pescar (com LLMs), não recebe o peixe.**

---

# Jornada de hoje

| Bloco | Conteúdo | Tempo |
|-------|----------|-------|
| **1** | Conceitos + Demo | 25 min |
| **2** | Setup | 20 min |
| **3** | Construção via Claude Code | 55 min |
| — | *Pausa* | 10 min |
| **4** | Integração ML via Claude Code | 30 min |
| **5** | Seu projeto (Spec + Deploy) | 30 min |
| **6** | Fechamento | 10 min |

---

<!-- _class: lead -->
<!-- _backgroundColor: #c05621 -->

# BLOCO 1
## Conceitos Essenciais

<span class="timer">25 minutos</span>

---

# 🎬 Primeiro: ver funcionando

<div class="center">

### Próximos 5 minutos:

Demonstração de uma aplicação completa

<br>

**Observem:**
- A simplicidade da interface
- Como os dados aparecem
- Como a previsão funciona

</div>

---

# O problema: "Vibe Coding" tradicional

> **"Não importa quão rápido você consegue criar algo se for inútil."**
> — Bechtel

<div class="box box-danger">

### O ciclo frustrante:

```
Você: "Cria um dashboard pra mim"
IA:   [300 linhas de código confuso]
Você: "Não era isso..."
IA:   [mais código, diferente]
Você: "Agora deu erro..."

⏱️ 2 horas depois: frustração
```

</div>

---

# Por que isso acontece?

<div class="box box-warning">

### O LLM não lê mentes

Quando você diz "cria um dashboard":

- Qual framework? *(React? Flask? Streamlit?)*
- Quais dados? *(CSV? Banco? API?)*
- Quais gráficos? *(Barras? Linhas? Pizza?)*
- Qual layout? *(Simples? Complexo?)*

**A IA adivinha. E adivinha errado.**

</div>

<br>

> **"Dê à IA uma especificação clara, e você terá uma saída clara; dê um 'vibe' (sensação), e receberá um 'vibe' de volta."**

---

# A solução: Especificação Vibrante (Vibe Specs)

<div class="box box-success">

### O padrão que funciona:

1. **Você dialoga** com o LLM sobre o que quer
2. **LLM sintetiza** em uma especificação
3. **Você aprova** com "VAI!"
4. **LLM implementa** baseado na especificação

</div>

<br>

### Evidências:
- **60% de redução** no tempo de desenvolvimento
- Usado por OpenAI, Shopify, desenvolvedores de elite
- Pesquisa acadêmica valida a abordagem

---

# Engenharia de Contexto

> **"Engenharia de contexto é a arte e ciência delicada de preencher a janela de contexto com exatamente a informação certa para o próximo passo."**
> — Andrej Karpathy

<br>

<div class="columns">

<div class="box">

### Pouco contexto
LLM adivinha e erra

</div>

<div class="box">

### Contexto demais
LLM se perde e fica caro

</div>

</div>

<br>

<div class="box box-success">

### Contexto certo (Especificação)
LLM entrega exatamente o que você precisa

</div>

---

# O "Caminho Dourado"

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   💬 DIÁLOGO  →  📝 SPEC  →  ✅ "VAI!"  →  💻 CÓDIGO      │
│                                                             │
│ (LLM pergunta) (LLM escreve) (você aprova) (LLM programa)   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### A diferença crucial:
- **Você não escreve** código
- **Você dialoga** com o LLM
- O LLM **sintetiza e implementa** com base no documento de especificação que você aprova!

---

# 7 problemas que a Especificação resolve

| Problema | Com Especificação |
|----------|-------------------|
| Conversa confusa (deriva) | Documento estável |
| Trabalho isolado | Comunicação fácil com colegas e demandante|
| Sem controle de versão | Rastreado no Git |
| Escopo inflado | Escopo definido |
| Contexto perdido | Retomada instantânea |
| Página em branco | LLM estrutura o pensamento |
| Tokens desperdiçados | Contexto denso e eficiente |

---

# O fluxo em 3 fases

<div class="columns-3">

<div class="box">

### Fase 1
**Diálogo**

LLM faz perguntas
Você responde
Refinam juntos

</div>

<div class="box">

### Fase 2
**Especificação**

LLM sintetiza
Você revisa
Ajustam se preciso

</div>

<div class="box box-success">

### Fase 3
**"VAI!"**

Você aprova
LLM implementa
Código correto

</div>

</div>

<br>

> **"Devagar é suave, e suave é rápido."**

---

<!-- _class: lead -->
<!-- _backgroundColor: #276749 -->

# ✅ Conceitos-chave:

## 1. Especificação antes de código
## 2. LLM ajuda a criar a Especificação
## 3. "VAI!" só após aprovação humana

---

<!-- _class: lead -->
<!-- _backgroundColor: #c05621 -->

# BLOCO 2
## Preparação do Ambiente

<span class="timer">20 minutos (com buffer)</span>

---

# Passo 1: Clonar repositório

<div class="prompt-box">

**Terminal:**

git clone https://github.com/ErickMFS/vibe-coding-v3.git
cd vibe-coding-v3

</div>

### Estrutura:

```
vibe-coding-v3/
├── app_referencia.py    ← Código de referência (consulta)
├── prompts/             ← Prompts para usar com Claude
├── data/safras.csv
├── models/modelo_mock.pkl
└── docs/                ← Templates de especificação
```

---

# Passo 2: Ambiente virtual

<div class="columns">

<div class="box">

### Linux / Mac

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

</div>

<div class="box">

### Windows

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

</div>

</div>

---

# Passo 3: Testar Streamlit

<div class="prompt-box">

**Terminal:**

streamlit hello

</div>

### Deve aparecer:

```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```

<div class="box box-success">

✅ **Se abriu no navegador, está funcionando!**

Pressione `Ctrl+C` para parar.

</div>

---

# Passo 4: Iniciar Claude Code

<div class="prompt-box">

**Terminal:**

claude

</div>

### Claude Code deve iniciar:

```
╭─────────────────────────────────────────╮
│ Claude Code                             │
│ Versão X.X.X                            │
╰─────────────────────────────────────────╯

>
```

<div class="box box-success">

✅ **Se viu o prompt, Claude Code está pronto!**

</div>

---

# 🆘 Resolução de Problemas Rápida

| Erro | Solução |
|------|---------|
| `command not found: streamlit` | `pip install streamlit` |
| `command not found: claude` | `npm install -g @anthropic-ai/claude-code` |
| Porta em uso | `streamlit run app.py --server.port 8502` |
| Permissão negada (Windows) | `Set-ExecutionPolicy RemoteSigned` |

---

<!-- _class: lead -->
<!-- _backgroundColor: #276749 -->

# ✅ Verificação: Preparação

## 🙋 Quem conseguiu:
### - `streamlit hello` funcionou?
### - `claude` iniciou?

---

<!-- _class: lead -->
<!-- _backgroundColor: #c05621 -->

# BLOCO 3
## Construção via Claude Code

<span class="timer">55 minutos</span>

*3 pontos de verificação — ninguém fica para trás*

---

# A nova abordagem

<div class="columns">

<div class="box box-danger">

### ❌ O que NÃO faremos

- Copiar código dos slides
- Colar sem entender
- Depender de código pronto

</div>

<div class="box box-success">

### ✅ O que faremos

- Usar prompts com Claude Code
- Gerar código via diálogo
- Entender o que foi criado

</div>

</div>

<br>

<div class="box box-warning">

**Código de referência existe** na pasta `app_checkpoints/` — use apenas se travar!

</div>

---

# Metas dos próximos 55 min

<div class="columns-3">

<div class="box box-success">

### PV 1
**Dados**

Carregar CSV
Mostrar tabela

*~18 min*

</div>

<div class="box box-success">

### PV 2
**Filtros**

Barras laterais
Filtrar dados

*~18 min*

</div>

<div class="box box-success">

### PV 3
**Gráfico**

Visualização
Interativo

*~18 min*

</div>

</div>

<br>

<div class="center small">

**Regra:** Ninguém avança até todos chegarem no ponto de verificação

</div>

---

<!-- _class: lead -->
<!-- _backgroundColor: #38a169 -->

# 🎯 PONTO DE VERIFICAÇÃO 1
## Carregar e Exibir Dados

<span class="timer">~18 min</span>

---

# PV1: O que queremos

<div class="box">

### Objetivo:
Uma aplicação Streamlit que:
- Carrega dados de `data/safras.csv`
- Mostra título e descrição
- Exibe métricas resumo (total, culturas, estados, produção)
- Mostra tabela com todos os dados

</div>

---

# PV1: Use este prompt com Claude Code

<div class="prompt-box">

**Cole no Claude Code:**

Crie uma aplicação Streamlit básica com estas características:

1. Configure a página com título "Dashboard de Safras", ícone 🌾, layout amplo
2. Adicione título "Dashboard de Safras" e subtítulo descritivo
3. Carregue dados do arquivo data/safras.csv usando cache
4. Mostre 4 métricas em colunas: total de registros, número de culturas únicas, número de estados, produção total em milhões de toneladas
5. Exiba a tabela completa de dados

Salve como app.py

</div>

---

# PV1: O que Claude deve gerar

<div class="box box-success">

### Claude Code vai:

1. Criar o arquivo `app.py`
2. Importar streamlit e pandas
3. Configurar a página
4. Criar função com cache para carregar dados
5. Exibir métricas e tabela

</div>

### Teste:

<div class="prompt-box">

**Terminal (nova janela):**

streamlit run app.py

</div>

---

# PV1: Verifique o resultado

<div class="box box-success">

### ✅ Critérios de sucesso:

- [ ] Página abre no navegador
- [ ] Título aparece
- [ ] 4 métricas estão visíveis
- [ ] Tabela mostra dados do CSV

</div>

<br>

<div class="box box-warning">

### 🆘 Travou? 

Copie o código de referência:
`cp app_checkpoints/pv1_dados.py app.py`

</div>

---

<!-- _class: lead -->
<!-- _backgroundColor: #276749 -->

# ✅ Ponto de Verificação 1 Completo!

### 🙋 Quem conseguiu gerar via Claude Code?
### 🙋 Quem precisou do código de referência?

---

<!-- _class: lead -->
<!-- _backgroundColor: #38a169 -->

# 🎯 PONTO DE VERIFICAÇÃO 2
## Adicionar Filtros

<span class="timer">~18 min</span>

---

# PV2: O que queremos

<div class="box">

### Objetivo:
Adicionar à aplicação:
- Barra lateral com filtros
- Filtro por cultura (com opção "Todas")
- Filtro por estado (com opção "Todos")
- Métricas e tabela atualizam conforme filtros

</div>

---

# PV2: Use este prompt com Claude Code

<div class="prompt-box">

**Cole no Claude Code:**

Modifique app.py para adicionar filtros:

1. Crie uma barra lateral (sidebar) com título "Filtros"
2. Adicione um seletor de cultura com opções: "Todas" + culturas únicas do CSV
3. Adicione um seletor de estado com opções: "Todos" + estados únicos do CSV
4. Aplique os filtros aos dados: se cultura != "Todas", filtre; se estado != "Todos", filtre
5. As métricas e tabela devem usar os dados filtrados
6. Mostre indicador de filtros ativos na barra lateral

</div>

---

# PV2: Verifique o resultado

<div class="box box-success">

### ✅ Critérios de sucesso:

- [ ] Barra lateral aparece
- [ ] Seletores de cultura e estado funcionam
- [ ] Ao filtrar, métricas mudam
- [ ] Ao filtrar, tabela mostra menos linhas

</div>

<br>

<div class="box box-warning">

### 🆘 Travou? 

`cp app_checkpoints/pv2_filtros.py app.py`

</div>

---

<!-- _class: lead -->
<!-- _backgroundColor: #276749 -->

# ✅ Ponto de Verificação 2 Completo!

### ✓ Barra lateral funcionando
### ✓ Filtros aplicando corretamente

---

<!-- _class: lead -->
<!-- _backgroundColor: #38a169 -->

# 🎯 PONTO DE VERIFICAÇÃO 3
## Adicionar Visualização

<span class="timer">~18 min</span>

---

# PV3: O que queremos

<div class="box">

### Objetivo:
Adicionar gráficos à aplicação:
- Gráfico de barras horizontais por estado
- Gráfico de linhas mostrando evolução temporal
- Layout em colunas: tabela ao lado do gráfico

</div>

---

# PV3: Use este prompt com Claude Code

<div class="prompt-box">

**Cole no Claude Code:**

Modifique app.py para adicionar visualizações com Plotly:

1. Importe plotly.express
2. Crie seção "Dados e Visualização"
3. Use duas colunas lado a lado
4. Na coluna esquerda: tabela de dados (altura 400)
5. Na coluna direita: gráfico de barras horizontais mostrando produção total por estado, colorido por estado, sem legenda
6. Abaixo, adicione gráfico de linhas mostrando evolução da produção por ano, com linhas separadas por cultura

Use os dados filtrados para todos os gráficos.

</div>

---

# PV3: Verifique o resultado

<div class="box box-success">

### ✅ Critérios de sucesso:

- [ ] Tabela e gráfico de barras lado a lado
- [ ] Gráfico de barras mostra estados
- [ ] Gráfico de linhas mostra evolução
- [ ] Filtros afetam todos os gráficos

</div>

<br>

<div class="box box-warning">

### 🆘 Travou? 

`cp app_checkpoints/pv3_grafico.py app.py`

</div>

---

<!-- _class: lead -->
<!-- _backgroundColor: #276749 -->

# ✅ Ponto de Verificação 3 Completo!

### ✓ Gráfico de barras
### ✓ Gráfico de linhas
### ✓ Layout profissional

---

<!-- _class: lead -->
<!-- _backgroundColor: #ed8936 -->

# ☕ PAUSA

## 10 minutos

### Aproveitem para resolver pendências

---

<!-- _class: lead -->
<!-- _backgroundColor: #c05621 -->

# BLOCO 4
## Integração com Aprendizado de Máquina

<span class="timer">30 minutos</span>

---

# O objetivo principal

<div class="box box-success">

### Conectar interface web + modelo de AM

O que vocês treinaram nas aulas anteriores
agora terá uma interface para usar!

</div>

### Dois pontos de verificação:
1. **PV4**: Carregar modelo
2. **PV5**: Interface de previsão

---

<!-- _class: lead -->
<!-- _backgroundColor: #38a169 -->

# 🎯 PONTO DE VERIFICAÇÃO 4
## Carregar Modelo de AM

<span class="timer">~12 min</span>

---

# PV4: O que queremos

<div class="box">

### Objetivo:
- Carregar modelo de `models/modelo_mock.pkl`
- Usar cache especial para modelos
- Mostrar status na barra lateral
- Tratar erro se modelo não existir

</div>

---

# PV4: Use este prompt com Claude Code

<div class="prompt-box">

**Cole no Claude Code:**

Modifique app.py para carregar o modelo de AM:

1. Importe joblib
2. Crie função carregar_modelo() com cache de recurso (@st.cache_resource)
3. Carregue models/modelo_mock.pkl
4. Trate FileNotFoundError retornando None
5. Na barra lateral, adicione seção "Modelo AM" com:
   - Se modelo carregado: mensagem de sucesso verde
   - Se não carregado: mensagem de erro vermelha

</div>

---

# PV4: Verifique o resultado

<div class="box box-success">

### ✅ Critérios de sucesso:

- [ ] Barra lateral mostra status do modelo
- [ ] Aparece "✅ Carregado" em verde
- [ ] Sem erros no terminal

</div>

<br>

<div class="box box-warning">

### Se modelo não existe:

`python setup_modelo.py`

</div>

---

<!-- _class: lead -->
<!-- _backgroundColor: #38a169 -->

# 🎯 PONTO DE VERIFICAÇÃO 5
## Interface de Previsão

<span class="timer">~18 min</span>

---

# PV5: O que queremos

<div class="box">

### Objetivo:
Formulário completo de previsão:
- Campos de entrada (área, temperatura, precipitação)
- Botão para calcular
- Exibição do resultado
- Comparação com média histórica

</div>

---

# PV5: Use este prompt com Claude Code

<div class="prompt-box">

**Cole no Claude Code:**

Modifique app.py para adicionar interface de previsão:

1. Crie seção "Fazer Previsão"
2. Se modelo não disponível, mostre aviso
3. Se disponível, crie 3 colunas com:
   - Coluna 1: seletor de cultura, campo numérico para área (100 a 15M, padrão 1M)
   - Coluna 2: seletor de estado, controle deslizante de temperatura (15 a 35, padrão 25)
   - Coluna 3: campo para ano (2024-2030), controle deslizante de precipitação (500-2500, padrão 1400)
4. Botão "Calcular Previsão" centralizado
5. Ao clicar: use modelo.predict com [area, temp, chuva]
6. Mostre resultado em 3 métricas: produção, produtividade, comparação com média
7. Adicione efeito de balões ao final

</div>

---

# PV5: Verifique o resultado

<div class="box box-success">

### ✅ Critérios de sucesso:

- [ ] Formulário aparece com todos os campos
- [ ] Botão funciona
- [ ] Previsão aparece em métricas
- [ ] Balões aparecem! 🎈

</div>

<br>

<div class="box box-warning">

### 🆘 Travou? 

`cp app_checkpoints/pv5_previsao.py app.py`

</div>

---

<!-- _class: lead -->
<!-- _backgroundColor: #276749 -->

# 🎉 PARABÉNS!

## Vocês construíram uma aplicação web
## com Aprendizado de Máquina integrado
## usando Claude Code!

---

# 🔄 Do modelo de exemplo para o SEU modelo

<div class="box box-warning">

### O modelo de exemplo usa:

```
X = [[area, temperatura, precipitacao]]  # 3 características numéricas
```

### Seu modelo provavelmente usa características diferentes!

</div>

---

# Adaptando para seu modelo: Prompt

<div class="prompt-box">

**Pergunte ao Claude Code:**

Meu modelo de AM usa as seguintes características:
- [lista suas características aqui]
- Exemplo: area_ha, umidade_percent, ph_solo, tipo_solo (categorico)

O tipo_solo é categórico com valores: argiloso, arenoso, misto

Modifique o formulário de previsão para usar essas características.
Se houver variável categórica, use seletor e faça encoding manual.

</div>

---

# Claude vai adaptar automaticamente

<div class="box box-success">

### Exemplo do que Claude geraria:

Para característica categórica:

```
tipo_solo = st.selectbox("Tipo de Solo", ["argiloso", "arenoso", "misto"])
mapa_solo = {"argiloso": 0, "arenoso": 1, "misto": 2}
solo_codificado = mapa_solo[tipo_solo]

X = [[area, umidade, ph, solo_codificado]]
pred = modelo.predict(X)[0]
```

</div>

---

# Como descobrir as características do seu modelo

<div class="prompt-box">

**No caderno (notebook) onde você treinou:**

```
# Ver características usadas:
print(X_treino.columns.tolist())

# Ver tipos:
print(X_treino.dtypes)

# Se o modelo tiver o atributo:
print(modelo.feature_names_in_)
```

</div>

### Anote essas informações para usar no prompt!

---

<!-- _class: lead -->
<!-- _backgroundColor: #c05621 -->

# BLOCO 5
## Seu Projeto: Especificação + Publicação

<span class="timer">30 minutos</span>

---

# Duas metas para este bloco

<div class="columns">

<div class="box box-success">

### Meta 1: Especificação
Criar especificação para **seu** projeto

*15 min*

</div>

<div class="box box-success">

### Meta 2: Publicação
Colocar aplicação **na internet**

*15 min*

</div>

</div>

---

# Exercício: Diálogo para Especificação

<div class="prompt-box">

**Inicie o Claude Code e cole:**

Você é um assistente de especificação. Vou criar uma interface web para meu modelo de Aprendizado de Máquina.

Faça-me perguntas para entender:
1. O que meu modelo prevê?
2. Quais características/entradas ele usa?
3. Que dados históricos tenho?
4. Como quero visualizar os resultados?

Após entender, sintetize em uma Especificação Enxuta de 1 página.
Ao final, pergunte se posso dizer "VAI!" para implementar.

</div>

---

# Exemplo de diálogo

```
Claude: O que seu modelo de AM prevê?

Você:   Produtividade de lavouras de soja em kg/hectare

Claude: Quais entradas/características o modelo usa?

Você:   Área plantada, precipitação média, temperatura média, 
        tipo de solo (argiloso, arenoso, misto)

Claude: Que dados históricos você tem?

Você:   Um CSV com dados de safras dos últimos 5 anos

Claude: Entendi! Aqui está a Especificação Enxuta:
        [... sintetiza em documento ...]
        
        Isso captura sua intenção? Posso dizer "VAI!" para implementar?
```

---

# Após o "VAI!"

<div class="box box-success">

### Claude vai:

1. Gerar código baseado na Especificação
2. Ajustar as entradas para suas características
3. Configurar visualizações adequadas

### Você vai:

1. Salvar como `app.py`
2. Testar com `streamlit run app.py`
3. Ajustar o que precisar

</div>

---

<!-- _class: lead -->
<!-- _backgroundColor: #2c5282 -->

# 🌐 PUBLICAÇÃO NA WEB

## Streamlit Cloud — Gratuito!

---

# Por que publicar na web?

<div class="box box-success">

### Benefícios:

- 🌍 **Acesso de qualquer lugar** — sem instalar nada
- 👥 **Compartilhar com colegas** — basta enviar o link
- 📱 **Funciona no celular** — interface responsiva
- 🆓 **Gratuito** — para projetos públicos

</div>

---

# Passo 1: Preparar repositório no GitHub

<div class="box">

### Seu repositório precisa ter:

```
meu-projeto/
├── app.py              ← Sua aplicação
├── requirements.txt    ← Dependências
├── data/
│   └── safras.csv      ← Seus dados
└── models/
    └── modelo.pkl      ← Seu modelo (se < 100MB)
```

</div>

<br>

### Comandos:

```
git add .
git commit -m "Aplicação pronta para publicação"
git push origin main
```

---

# Passo 2: Criar conta no Streamlit Cloud

<div class="box box-success">

### Acesse: **share.streamlit.io**

1. Clique em **"Sign up"** (Cadastrar)
2. Conecte com sua conta **GitHub**
3. Autorize o Streamlit a acessar seus repositórios
4. Preencha nome e e-mail se solicitado

</div>

---

# Passo 3: Publicar aplicação

<div class="box">

### No painel do Streamlit Cloud:

1. Clique em **"New app"** (Nova aplicação)
2. Selecione seu **repositório** do GitHub
3. Escolha o **branch** (geralmente `main`)
4. Informe o **arquivo principal** (ex: `app.py`)
5. Clique em **"Deploy!"** (Publicar)

</div>

<br>

⏱️ **Aguarde 2-5 minutos** para a publicação completar

---

# Passo 4: Acessar sua aplicação

<div class="box box-success">

### Sua URL será algo como:

**https://seu-usuario-nome-do-app.streamlit.app**

</div>

<br>

### Compartilhe com qualquer pessoa!
- Colegas de trabalho
- Gestores
- Qualquer um com o link

---

# Resolução de Problemas na Publicação

| Problema | Solução |
|----------|---------|
| Erro de dependência | Verifique `requirements.txt` |
| Arquivo não encontrado | Confira caminhos relativos |
| Modelo muito grande | Use Git LFS ou hospede externamente |
| Demora para carregar | Adicione cache com `@st.cache_data` |

---

# ⏱️ Mãos à obra: 15 minutos

<div class="center">

### Façam agora:

1. Gerem a especificação do projeto
2. Deixem Claude gerar o código
3. Preparem repositório no GitHub
4. Publiquem no Streamlit Cloud

</div>

---

<!-- _class: lead -->
<!-- _backgroundColor: #276749 -->

# ✅ Tempo!

## 🙋 Quem conseguiu publicar?
## 🙋 Quem precisa de ajuda?

---

<!-- _class: lead -->
<!-- _backgroundColor: #c05621 -->

# BLOCO 6
## Fechamento

<span class="timer">10 minutos</span>

---

# O que vocês aprenderam

<div class="columns-3">

<div class="box">

### Conceitos

- Especificação Vibrante
- Engenharia de Contexto
- Caminho Dourado
- Spec → Código

</div>

<div class="box">

### Ferramentas

- Streamlit
- Claude Code
- Plotly
- Streamlit Cloud

</div>

<div class="box">

### Prática

- Dialogar com IA
- Gerar código via prompts
- Integrar modelos AM
- Publicar na web

</div>

</div>

---

# Projeto da semana

<div class="box box-success">

### Sua missão:

1. Finalizar interface para seu modelo
2. Usar o fluxo: **Diálogo → Spec → VAI! → Código**
3. Publicar no Streamlit Cloud
4. Compartilhar o link na próxima aula

### Prazo: [DATA]

</div>

---

# Recursos

<div class="columns">

<div>

### Documentação

- [Documentação Streamlit](https://docs.streamlit.io)
- [Plotly Python](https://plotly.com/python/)
- [Especificação Vibrante](https://lukebechtel.com/blog/vibe-speccing)

</div>

<div>

### Repositório

```
https://github.com/ErickMFS/vibe-coding-v3
```

- Prompts para cada ponto de verificação
- Código de referência
- Modelo de especificação

</div>

</div>

---

# Conclusões finais

> **"A mágica não está em evitar o LLM até ter os requisitos. A mágica está em usar o LLM para ajudá-lo a descobrir quais são seus requisitos de verdade."**

<br>

> **"Na era do desenvolvimento assistido por IA, todo desenvolvedor se tornará seu próprio gerente de produto."**

<br>

<div class="center">

**LLM → Especificação → Código. Este é o caminho.**

</div>

---

<!-- _class: lead -->
<!-- _backgroundColor: #1a365d -->

# 🚀 Bom trabalho!

## Nos vemos na apresentação

**Material**: https://github.com/ErickMFS/vibe-coding-v3

---

<!-- _class: invert -->

# 📎 ANEXOS

## Material de referência

---

# Anexo A: Modelo de Especificação Enxuta

```
# [Nome do Projeto]

## O que é? (1 frase)
_______________________________________

## Para quem?
_______________________________________

## Características do modelo de AM
| Característica | Tipo    | Faixa/Valores |
|----------------|---------|---------------|
|                |         |               |

## O que o modelo prevê?
_______________________________________

## Visualizações desejadas
- [ ] Tabela de dados
- [ ] Gráfico de barras
- [ ] Gráfico de linhas

## Critérios de sucesso
- [ ] ________________________________
- [ ] ________________________________
```

---

# Anexo B: Prompt para Diálogo de Especificação

<div class="prompt-box" style="font-size: 0.7em;">

Você é um assistente especializado em criar especificações para interfaces web com Aprendizado de Máquina.

Seu objetivo é me ajudar a definir claramente o que quero construir.

**Processo:**

1. Pergunte uma coisa de cada vez:
   - Qual o objetivo da interface?
   - O que o modelo prevê?
   - Quais entradas o modelo precisa?
   - Que dados históricos existem?
   - Quais visualizações quer?

2. Após coletar respostas, sintetize em Especificação Enxuta

3. Pergunte: "Isso captura sua intenção? Digite VAI! para implementar"

4. Só gere código após "VAI!"

</div>

---

# Anexo C: Prompts dos Pontos de Verificação

### PV1 - Dados

```
Crie aplicação Streamlit básica:
- Título "Dashboard de Safras"
- Carregue data/safras.csv com cache
- Mostre 4 métricas: registros, culturas, estados, produção
- Exiba tabela completa
```

### PV2 - Filtros

```
Adicione filtros:
- Barra lateral com seletores de cultura e estado
- Opções "Todas/Todos" + valores únicos
- Métricas e tabela usam dados filtrados
```

---

# Anexo C: Prompts (continuação)

### PV3 - Gráficos

```
Adicione visualizações Plotly:
- Duas colunas: tabela | gráfico de barras por estado
- Gráfico de linhas: evolução por ano e cultura
- Use dados filtrados
```

### PV4 - Modelo

```
Carregue modelo de AM:
- Importe joblib
- Função com cache de recurso
- Carregue models/modelo_mock.pkl
- Mostre status na barra lateral
```

---

# Anexo C: Prompts (continuação)

### PV5 - Previsão

```
Adicione interface de previsão:
- 3 colunas com: cultura, estado, ano, área, temperatura, precipitação
- Botão "Calcular Previsão"
- Use modelo.predict([[area, temp, chuva]])
- Mostre resultado em métricas
- Adicione efeito de balões
```

---

# Anexo D: Resolução de Problemas

| Sintoma | Causa Provável | Solução |
|---------|----------------|---------|
| `ModuleNotFoundError` | Pacote não instalado | `pip install X` |
| `FileNotFoundError` | Caminho errado | Verificar com `ls` |
| `KeyError` | Coluna não existe | `st.write(df.columns)` |
| Gráfico vazio | Dados filtrados = 0 | Limpar filtros |
| Modelo não carrega | Arquivo errado | Verificar caminho |

---

# Anexo E: Publicação no Streamlit Cloud

### Passo a passo:

1. **Repositório GitHub** com: `app.py`, `requirements.txt`, dados
2. **Acesse** share.streamlit.io
3. **Conecte** conta GitHub
4. **Clique** "New app"
5. **Selecione** repositório, branch, arquivo
6. **Clique** "Deploy!"
7. **Aguarde** 2-5 minutos
8. **Acesse** sua URL pública!

---

# Anexo F: Estrutura Final do Projeto

```
meu-projeto/
├── app.py                 ← Aplicação principal
├── requirements.txt       ← Dependências
├── data/
│   └── safras.csv         ← Dados
├── models/
│   └── modelo.pkl         ← Modelo AM
├── docs/
│   └── especificacao.md   ← Sua especificação
├── prompts/
│   └── pv1_dados.txt      ← Prompts usados
└── README.md              ← Documentação
```

---

<!-- _class: lead -->
<!-- _backgroundColor: #1a365d -->

# FIM DA AULA

## Vibe Coding Estruturado v4.0

**Dezembro 2025**