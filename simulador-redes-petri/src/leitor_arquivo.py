# -*- coding: utf-8 -*-
import json

from lugar import Lugar
from transicao import Transicao


def ler_arquivo(arquivo: str):
    configuracoes = json.loads(
        open(file=arquivo, mode="r", encoding="UTF-8").read()
    )

    lugares = {}
    transicoes = {}

    for lugar_conf in configuracoes["lugares"]:
        lugar = Lugar(lugar_conf)
        lugares[lugar.id] = lugar

    for transacao_conf in configuracoes["transicoes"]:
        transicao = Transicao(transacao_conf)
        transicoes[transicao.id] = transicao

    for arco_conf in configuracoes["arcos"]:
        id_origem = arco_conf["origem"]
        id_destino = arco_conf["destino"]
        peso = arco_conf["peso"]

        if id_origem in lugares:
            origem = lugares[id_origem]
            destino = transicoes[id_destino]
        else:
            origem = transicoes[id_origem]
            destino = lugares[id_destino]

        origem.destinos.append({"peso": peso, "destino": destino})
        destino.origens.append({"peso": peso, "origem": origem})

    return {
        "lugares": lugares,
        "transicoes": transicoes
    }
