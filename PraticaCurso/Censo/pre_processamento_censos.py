#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 5 10:52:51 2019

@author: nicolas
"""

import pandas as pd
base = pd.read_csv('census.csv')

base.describe

# Agora vamos transforma os dados classificados como CATEGORICOS para numericos
# Pois, os algoritimos são baseados em funções matemáticas, então para utilziar todo o potencial dessas funções é preciso dar NUMERO a elas

# Primeiro é dividir quais são atributos Previsores e Classe

x = base.iloc[:,0:14].values # Atributos Previsor
y = base.iloc[:, 14].values # Atributos Classe

