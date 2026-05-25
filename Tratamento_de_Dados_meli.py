import pandas as pd

import numpy as np



# Substitua pelo ID da sua planilha integrada

# Linha 5: Guarde o ID como um texto (String) usando aspas

SEU_SHEET_ID = "1d2FDl84KxzV6M_RQi9Wu4uiCSUSteadEP1Oxkmc6sD4"



# Linha 6: Agora sim a f-string vai ler a variável perfeitamente

url_integracao = f"https://docs.google.com/spreadsheets/d/{SEU_SHEET_ID}/export?format=csv"



# Carregando os dados brutos

df_cajamar = pd.read_csv(url_integracao)



# =========================================================================

# MÓDULO DE AUDITORIA: ALERTA DE DADOS SUJOS

# =========================================================================



print("=" * 60)

print("🚨 ALERTA DE QUALIDADE DE DADOS: OPERAÇÃO CAJAMAR 🚨")

print("=" * 60)

print(f"📊 Total de linhas brutas importadas: {len(df_cajamar):,}")

print("-" * 60)



# 1. Contagem de Linhas Duplicadas (Bips repetidos no mesmo segundo)

total_duplicados = df_cajamar.duplicated().sum()



# 2. Contagem de Valores Nulos (Falta de registro no scanner)

nulos_por_coluna = df_cajamar.isnull().sum()

total_nulos = nulos_por_coluna.sum()



# 3. Inconsistências de Texto no Setor (letras minúsculas ou espaços em branco)

# Consideramos padrão correto apenas "DV" e "RESSUBIDO" estritos

setores_fora_padrao = df_cajamar[~df_cajamar['Setor'].isin(['DV', 'RESSUBIDO'])].shape[0]



# 4. Erros Críticos de Contagem (O temido '99999' ou peças negativas)

contagens_bizzaras = df_cajamar[(df_cajamar['Pecas_Processadas'] == 99999) | (df_cajamar['Pecas_Processadas'] < 0)].shape[0]



# 5. Erros de Cronômetro (Tempo zerado ou negativo)

tempo_invalido = df_cajamar[df_cajamar['Tempo_Segundos'] <= 0].shape[0]





# --- EXIBIÇÃO DO DIAGNÓSTICO ---

print(f"👥 Linhas 100% duplicadas encontradas: {total_duplicados:,}")

print(f"🕳️ Total de campos vazios (NaN): {total_nulos:,}")

for coluna, qtd in nulos_por_coluna.items():

    if qtd > 0:

        print(f"   ↳ Coluna '{coluna}': {qtd:,} nulos")



print(f"🔤 Setores com erro de digitação/caixa: {setores_fora_padrao:,}")

print(f"📦 Bips com quantidades impossíveis (<0 ou 99999): {contagens_bizzaras:,}")

print(f"⏱️ Registros com tempo inválido (<= 0s): {tempo_invalido:,}")



print("=" * 60)

if total_duplicados > 0 or total_nulos > 0 or contagens_bizzaras > 0:

    print("⚠️ STATUS: BASE INADEQUADA PARA DASHBOARD! Inicializando limpeza...")

else:

    print("✅ STATUS: BASE LIMPA! Pronta para processamento.")

print("=" * 60)

# ==============================================================================

# MÓDULO DE TRATAMENTO: GERANDO A BASE LIMPA

# ==============================================================================

print("\n🧹 Iniciando o tratamento dos dados...")



# 1. Removendo linhas 100% duplicadas

df_limpo = df_cajamar.drop_duplicates()



# 2. Eliminando qualquer valor nulo (NaN) nas colunas críticas

df_limpo = df_limpo.dropna(subset=['ID_Colaborador', 'Pecas_Processadas', 'Tempo_Segundos'])



# 3. Padronizando a coluna 'Setor' para Maiúsculas e corrigindo erros de digitação

df_limpo['Setor'] = df_limpo['Setor'].str.upper().str.strip()

# Corrigindo quem digitou "RESUBIDO" com um 'S' só para "RESSUBIDO"

df_limpo['Setor'] = df_limpo['Setor'].replace('RESUBIDO', 'RESSUBIDO')



# 4. Filtrando apenas os setores que estão dentro do padrão da operação (DV e RESSUBIDO)

df_limpo = df_limpo[df_limpo['Setor'].isin(['DV', 'RESSUBIDO'])]



# 5. Eliminando contagens bizarras (peças negativas ou o temido '99999')

df_limpo = df_limpo[(df_limpo['Pecas_Processadas'] >= 0) & (df_limpo['Pecas_Processadas'] != 99999)]



# 6. Eliminando registros com tempo inválido (menor ou igual a zero segundos)

df_limpo = df_limpo[df_limpo['Tempo_Segundos'] > 0]



# ==============================================================================

# EXPORTAÇÃO DA NOVA PLANILHA (CRIANDO UM NOVO ARQUIVO)

# ==============================================================================

# Define o nome do novo arquivo tratado

nome_arquivo_limpo = "dados_limpos_meli.csv"



# Exporta o DataFrame limpo para CSV (index=False evita que o pandas crie uma coluna de números inúteis)

df_limpo.to_csv(nome_arquivo_limpo, index=False, encoding='utf-8')



print("=" * 60)

print(f"✅ SUCESSO! Nova base criada com o nome: {nome_arquivo_limpo}")

print(f"📊 Linhas da base bruta: {len(df_cajamar):,}")

print(f"✨ Linhas da base limpa e pronta para uso: {len(df_limpo):,}")

print("=" * 60)# ==============================================================================

# MÓDULO DE TRATAMENTO: GERANDO A BASE LIMPA

# ==============================================================================

print("\n🧹 Iniciando o tratamento dos dados...")



# 1. Removendo linhas 100% duplicadas

df_limpo = df_cajamar.drop_duplicates()



# 2. Eliminando qualquer valor nulo (NaN) nas colunas críticas

df_limpo = df_limpo.dropna(subset=['ID_Colaborador', 'Pecas_Processadas', 'Tempo_Segundos'])



# 3. Padronizando a coluna 'Setor' para Maiúsculas e corrigindo erros de digitação

df_limpo['Setor'] = df_limpo['Setor'].str.upper().str.strip()

# Corrigindo quem digitou "RESUBIDO" com um 'S' só para "RESSUBIDO"

df_limpo['Setor'] = df_limpo['Setor'].replace('RESUBIDO', 'RESSUBIDO')



# 4. Filtrando apenas os setores que estão dentro do padrão da operação (DV e RESSUBIDO)

df_limpo = df_limpo[df_limpo['Setor'].isin(['DV', 'RESSUBIDO'])]



# 5. Eliminando contagens bizarras (peças negativas ou o temido '99999')

df_limpo = df_limpo[(df_limpo['Pecas_Processadas'] >= 0) & (df_limpo['Pecas_Processadas'] != 99999)]



# 6. Eliminando registros com tempo inválido (menor ou igual a zero segundos)

df_limpo = df_limpo[df_limpo['Tempo_Segundos'] > 0]



# ==============================================================================

# EXPORTAÇÃO DA NOVA PLANILHA (CRIANDO UM NOVO ARQUIVO)

# ==============================================================================

# Define o nome do novo arquivo tratado

nome_arquivo_limpo = "dados_limpos_meli.csv"



# Exporta o DataFrame limpo para CSV (index=False evita que o pandas crie uma coluna de números inúteis)

df_limpo.to_csv(nome_arquivo_limpo, index=False, encoding='utf-8')



print("=" * 60)

print(f"✅ SUCESSO! Nova base criada com o nome: {nome_arquivo_limpo}")

print(f"📊 Linhas da base bruta: {len(df_cajamar):,}")

print(f"✨ Linhas da base limpa e pronta para uso: {len(df_limpo):,}")

print("=" * 60) 

