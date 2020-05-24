# -*- coding: utf-8 -*-
"""
Arquivo de entrada
"""
import cnpj

cnpj_a_verificar = 'bbb' #'04.252.011/0001-10' 

if cnpj.valida(cnpj_a_verificar):
    print(f'{cnpj_a_verificar} eh valido!')
else:
    print(f'{cnpj_a_verificar} eh invalido!')


