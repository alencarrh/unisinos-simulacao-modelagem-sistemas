# -*- coding: utf-8 -*-

import estado
import teclado
import tela
from leitor_arquivo import ler_arquivo

arquivo = ler_arquivo("./temp.json")

lugares = arquivo["lugares"]
transicoes = arquivo["transicoes"]

iteracao = 1
continuar = True
tab = "   "
while (continuar):
    print("Iteração:", iteracao)
    tela.print_lugares(lugares, tab=tab)
    tela.print_transicoes(transicoes, tab=tab)

    estado.atualizar(transicoes)

    iteracao += 1
    result = teclado.query_yes_no("Mostrar próximo estado?")
    if not result:
        break
