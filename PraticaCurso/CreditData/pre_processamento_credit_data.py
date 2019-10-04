# -*- coding: utf-8 -*-
"""
Created on Thurs Out 3 22:49 2019

@author: Nicolas Gabriel Teixeira
"""
# Importa a biblioteca panda
import pandas as pd

# Importa a base de dados
base = pd.read_csv('creditData.csv')

# Traz algumas metricas da variavel (Nesse caso da base de dados)
base.describe()

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