# 🌾 Vibe Coding Estruturado v3

Material do curso de prototipagem rápida com Streamlit, Claude Code e 
Aprendizado de Máquina.

## 🎯 Sobre o Curso

Este curso ensina a criar interfaces web para modelos de ML usando 
**Especificação Vibrante (Vibe Specs)**: uma abordagem onde você 
dialoga com a IA para criar especificações antes de gerar código.

### Diferencial desta versão:

- ✅ **Você não copia código** — você usa prompts com Claude Code
- ✅ **Publicação na web** — aprenda a publicar gratuitamente
- ✅ **Código de referência** — disponível apenas como backup

---

## 🚀 Início Rápido

### 1. Clonar o repositório

```bash
git clone https://github.com/curso-mapa/vibe-coding-v4.git
cd vibe-coding-v4
```

### 2. Criar ambiente virtual

```bash
# Linux/Mac
python -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Gerar modelo de exemplo

```bash
python setup_modelo.py
```

### 5. Iniciar Claude Code

```bash
claude
```

---

## 📁 Estrutura do Projeto

```
vibe-coding-v4/
├── README.md               ← Você está aqui
├── requirements.txt        ← Dependências
├── setup_modelo.py         ← Script para criar modelo
├── app_referencia.py       ← Código completo (referência)
│
├── prompts/                ← Prompts para usar com Claude
│   ├── pv1_dados.txt
│   ├── pv2_filtros.txt
│   ├── pv3_grafico.txt
│   ├── pv4_modelo.txt
│   ├── pv5_previsao.txt
│   ├── dialogo_especificacao.txt
│   └── adaptar_modelo.txt
│
├── app_checkpoints/        ← Código de backup (se Claude falhar)
│   ├── pv1_dados.py
│   ├── pv2_filtros.py
│   ├── pv3_grafico.py
│   ├── pv4_modelo.py
│   └── pv5_previsao.py
│
├── data/
│   └── safras.csv          ← Dados de exemplo
│
├── models/
│   └── modelo_mock.pkl     ← Gerado pelo setup_modelo.py
│
├── docs/
│   ├── especificacao_modelo.md
│   └── guia_deploy.md      ← Como publicar na web
│
└── troubleshooting.md      ← Resolução de problemas
```

---

## 🎓 Como Usar Durante o Curso

### Abordagem Principal: Prompts

1. Abra o arquivo de prompt correspondente (ex: `prompts/pv1_dados.txt`)
2. Inicie o Claude Code: `claude`
3. Cole o prompt
4. Deixe o Claude gerar o código
5. Teste com `streamlit run app.py`

### Abordagem de Backup: Código de Referência

Se o Claude não conseguir gerar código funcional:

```bash
# Copie o código do checkpoint
cp app_checkpoints/pv1_dados.py app.py

# Continue de onde parou
```

---

## 🌐 Publicação na Web

Após completar o desenvolvimento, publique gratuitamente:

1. Suba o código para o GitHub
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte seu repositório
4. Clique em "Deploy"

Guia completo em: `docs/guia_deploy.md`

---

## 🔧 Adaptando para Seu Modelo

Para usar seu próprio modelo de ML:

1. Abra o prompt `prompts/adaptar_modelo.txt`
2. Preencha as informações do seu modelo
3. Cole no Claude Code
4. Teste o resultado

---

## 🆘 Problemas Comuns

| Problema | Solução |
|----------|---------|
| `streamlit: command not found` | `pip install streamlit` |
| `claude: command not found` | `npm install -g @anthropic-ai/claude-code` |
| Modelo não encontrado | `python setup_modelo.py` |
| Erro de importação | `pip install -r requirements.txt` |

Guia completo em: `troubleshooting.md`

---

## 📚 Recursos

- [Documentação Streamlit](https://docs.streamlit.io)
- [Plotly Python](https://plotly.com/python/)
- [Especificação Vibrante (Vibe Specs)](https://lukebechtel.com/blog/vibe-speccing)
- [Claude Code](https://docs.anthropic.com)

---

## 📝 Licença

Material educacional - Erick Muzart, com licença para o MAPA

Curso de Vibe Coding Estruturado v4 - Dezembro 2025