# -*- coding: utf-8 -*-
"""
Created on Thurs Out 3 22:49 2019

@author: Nicolas Gabriel Teixeira
"""
# Importa a biblioteca panda
import pandas as pd
import numpy as np
# Importa a base de dados
base = pd.read_csv('creditData.csv')

# Traz algumas metricas da variavel (Nesse caso da base de dados)
base.describe()


# TRATAR DADOS INCONSISTENTES

# Depois de descoberto uma inconsistencia (Negative Age). Vamos achar esses caras

#funcao para encontrar coisas
base.loc[base['age'] < 0]

# Tecnicas Para Correcao Dessas Inconsistencias

# 1. Apagar a coluna [NAO RECOMENDADO]
#
# Como o nome diz, vai eliminar o mal pela raiz
base.drop('age', 1, inplace=True)

# 2. Apagar Somente os Registros com Problema [NAO RECOMENDADO]
# base[base.age < 0].index --> So vai deletar os dados da condicao e o "index" quer dizer que vai excluir todo o index
base.drop(base[base.age < 0].index, inplace=True)

# 3. Preencher manualmente os valores corretamente [MAIS EFICIENTE, POREM DIFICIL DE EXECUTAR]

# 4. Preencher os valores com a média [MAIS RECOMENDADO, CASO O 3 FALHE]
base.mean() # Traz a media de todas as colunas
base['age'].mean() # Traz a media da coluna especifica
base['age'][base.age > 0].mean() # Traz a media da coluna especifica de acordo com a condicao

base.loc[base.age < 0, 'age'] = 40.92

# TRATAR DADOS FALTANTES

pd.isnull(base['age'])
base.loc[pd.isnull(base['age'])]

previsores = base.iloc[:, 1:4].values # Armazenando os valores Previsores em uma variavel
classe = base.iloc[:, 4].values # Armazenando os valores Metas em uma variavel
    
# Tratando os valores Nulls da base de dados
from sklearn.impute import SimpleImputer

SimpleImputer = SimpleImputer(missing_values=np.nan, strategy='mean')  # Pega todos os valores NUlls e substitui pela média  
SimpleImputer = SimpleImputer.fit(previsores[:, 0:3])
previsores[:, 0:3] = SimpleImputer.transform(previsores[:, 0:3])

#ESCALONAMENTO DE ATRIBUTOS

#Vamos usar a estrategia de Standardisation(Padronização) para tratar a diferença de escala entre os dados

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)