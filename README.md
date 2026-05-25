# data-quality-pipeline-logistics
Pipeline em Python (Pandas/Numpy) para auditoria de qualidade de dados (Data Quality) e processo de ETL focado em performance operacional e People Analytics na logística.
# 🚨 Data Quality Audit & ETL Pipeline: Operação Cajamar

Este projeto simula um pipeline de engenharia e análise de dados focado em **People Analytics e Performance Logística**. O objetivo é extrair dados volumosos diretamente da nuvem, auditar a qualidade das informações antes do processamento e gerar uma base limpa e padronizada para ferramentas de Business Intelligence (BI).

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Pandas** (Tratamento, limpeza e filtragem de dados)
* **Numpy** (Manipulação matemática e tratamento de nulos)
* **Google Sheets API** (Integração direta com repositórios na nuvem)

## 📊 Estrutura do Pipeline
1. **Data Quality Audit (Pre-flight Check):** Antes de iniciar qualquer higienização, o script mapeia a volumetria bruta, identifica registros duplicados, campos nulos (`NaN`), anomalias de digitação em setores e contagens impossíveis.
2. **Tratamento e ETL:** * Remoção de bips duplicados e registros sem identificação.
   * Padronização de strings (limpeza de espaços e caixa alta).
   * Filtragem de outliers e valores discrepantes (ex: quantidades negativas ou logs corrompidos).
3. **Exportação:** Geração de um arquivo higienizado (`dados_limpos_meli.csv`) otimizado para modelagem SQL e Dashboards no Looker Studio.
