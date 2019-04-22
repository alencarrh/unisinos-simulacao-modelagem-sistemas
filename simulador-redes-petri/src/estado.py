# -*- coding: utf-8 -*-


def atualizar(lugares):
    transicoes = transacoes_habilitadas(lugares)

    for transicao in transicoes:
        transicao.executar()


def transacoes_habilitadas(lugares):
    transicoes = []
    for id_lugar in lugares:
        lugar = lugares[id_lugar]
        for transicao in [destino["destino"] for destino in lugar.destinos]:
            lugares_destino = {}
            for destino in transicao.destinos:
                lugares_destino[destino["destino"].id] = destino["destino"]

            if transicao.habilitada:
                transicoes.append(transicao)

            transicoes += transacoes_habilitadas(lugares_destino)

    return transicoes


def lugares_iniciais(lugares):
    lugares_inicias = {}
    for id_lugar in lugares:
        lugar = lugares[id_lugar]
        if lugar.is_inicial:
            lugares_inicias[id_lugar] = lugar

    return lugares_inicias
