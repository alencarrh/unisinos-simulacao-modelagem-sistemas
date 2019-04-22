# -*- coding: utf-8 -*-


def print_lugares(lugares, tab=""):
    linha_0 = tab + "     Lugar:"
    linha_1 = tab + "  Marcação:"
    for id_lugar in lugares:
        linha_0 += "  {0: <5}  ".format(id_lugar)
        linha_1 += "  {0: <5}  ".format(str(lugares[id_lugar].marcas))

    print(linha_0)
    print(linha_1)


def print_transicoes(transicoes, tab=""):
    linha_0 = tab + "Transições:"
    linha_1 = tab + "Habilitada:"
    for id_transicao in transicoes:
        linha_0 += "  {0: <5}  ".format(id_transicao)
        linha_1 += "  {0: <5}  ".format(str(transicoes[id_transicao].habilitada))

    print(linha_0)
    print(linha_1)
