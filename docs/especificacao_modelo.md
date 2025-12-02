# Modelo de Especificação Enxuta

Use este modelo para documentar os requisitos do seu projeto antes de implementar.

---

## Especificação Enxuta: [Nome do Projeto]

### 1. O que é? (1 frase)

_________________________________________________________________________

### 2. Para quem?

_________________________________________________________________________

### 3. Características do modelo de AM

| Característica | Tipo | Faixa de Valores | Obrigatório |
|----------------|------|------------------|-------------|
|                |      |                  | [ ] Sim [ ] Não |
|                |      |                  | [ ] Sim [ ] Não |
|                |      |                  | [ ] Sim [ ] Não |
|                |      |                  | [ ] Sim [ ] Não |
|                |      |                  | [ ] Sim [ ] Não |

### 4. O que o modelo prevê?

**Saída:** _________________________________________________________________

**Unidade:** _______________________________________________________________

### 5. Dados históricos disponíveis

- **Arquivo:** _______________________________________________
- **Formato:** [ ] CSV  [ ] Excel  [ ] Banco  [ ] Outro: ______
- **Colunas principais:** ____________________________________
- **Quantidade aproximada de registros:** ____________________

### 6. Visualizações desejadas

- [ ] Tabela de dados com busca/ordenação
- [ ] Gráfico de barras (por: _________________________)
- [ ] Gráfico de linhas (evolução por: ________________)
- [ ] Gráfico de pizza (distribuição de: _______________)
- [ ] Mapa geográfico
- [ ] Outro: _______________________________________________

### 7. Filtros necessários

- [ ] Por categoria/tipo: __________________________________
- [ ] Por região/estado: ___________________________________
- [ ] Por período/ano: _____________________________________
- [ ] Outro: _______________________________________________

### 8. Critérios de sucesso

Como você vai testar se a aplicação está funcionando corretamente?

1. [ ] ______________________________________________________
2. [ ] ______________________________________________________
3. [ ] ______________________________________________________
4. [ ] ______________________________________________________
5. [ ] ______________________________________________________

### 9. Fora do escopo (NÃO fazer neste protótipo)

- _________________________________________________________
- _________________________________________________________
- _________________________________________________________

---

### Metadados

- **Data de criação:** _______________
- **Autor:** _________________________
- **Versão:** ________________________
- **Status:** [ ] Rascunho  [ ] Em revisão  [ ] Aprovado

---

## Exemplo Preenchido

### Especificação Enxuta: Dashboard de Previsão de Safras

### 1. O que é?
Interface web para visualizar dados históricos de safras e prever 
produtividade agrícola usando modelo de Aprendizado de Máquina.

### 2. Para quem?
Analistas e gestores do departamento de planejamento agrícola do MAPA.

### 3. Características do modelo de AM

| Característica | Tipo | Faixa | Obrigatório |
|----------------|------|-------|-------------|
| area_hectares | numérico | 100 - 15.000.000 | [x] Sim |
| temperatura_media | numérico | 15 - 35 °C | [x] Sim |
| precipitacao_mm | numérico | 500 - 2500 mm | [x] Sim |

### 4. O que o modelo prevê?
**Saída:** Produção estimada
**Unidade:** Toneladas

### 5. Dados históricos
- **Arquivo:** data/safras.csv
- **Formato:** [x] CSV
- **Colunas:** cultura, estado, ano, area, producao, temperatura, precipitacao
- **Registros:** ~75 (2020-2024)

### 6. Visualizações
- [x] Tabela de dados com busca/ordenação
- [x] Gráfico de barras (por: estado)
- [x] Gráfico de linhas (evolução por: ano e cultura)
- [ ] Gráfico de pizza
- [ ] Mapa geográfico

### 7. Filtros
- [x] Por categoria/tipo: Cultura
- [x] Por região/estado: Estado (UF)
- [x] Por período/ano: Ano

### 8. Critérios de sucesso
1. [x] Tabela carrega e exibe todos os dados
2. [x] Filtros funcionam e atualizam visualizações
3. [x] Gráficos são interativos (hover, zoom)
4. [x] Formulário aceita inputs e não dá erro
5. [x] Previsão retorna valor numérico válido

### 9. Fora do escopo
- Autenticação de usuários
- Salvar histórico de previsões
- Exportação para PDF
- Versão mobile nativa

---

**Data:** Dezembro 2025  
**Status:** [x] Aprovado