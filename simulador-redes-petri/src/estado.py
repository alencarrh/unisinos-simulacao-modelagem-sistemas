# -*- coding: utf-8 -*-


def atualizar(transicoes):
    transicoes = transacoes_habilitadas(transicoes)

    for transicao in transicoes:
        if transicao.habilitada:
            transicao.executar()


def transacoes_habilitadas(todas_transicoes):
    transicoes = []
    for transicao_id in todas_transicoes:
        transicao = todas_transicoes[transicao_id]
        if transicao.habilitada:
            transicoes.append(todas_transicoes[transicao_id])

    return transicoes


def lugares_iniciais(lugares):
    lugares_inicias = {}
    for id_lugar in lugares:
        lugar = lugares[id_lugar]
        if lugar.is_inicial:
            lugares_inicias[id_lugar] = lugar

    return lugares_inicias
