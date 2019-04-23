# -*- coding: utf-8 -*-


class Transicao:

    def __init__(self, transicao_conf):
        self.id = transicao_conf["id"]
        self.nome = transicao_conf["nome"]
        self.origens = []  # {"peso": 1, "origem": Lugar()}
        self.destinos = []  # {"peso": 1, "destino": Lugar()}

    @property
    def habilitada(self):
        habilitada = True
        for origem in self.origens:
            habilitada = origem["origem"].marcas >= origem["peso"] and habilitada

        return habilitada

    def executar(self):
        # se chegar aqui, já está habilitada
        for origem in self.origens:
            origem["origem"].marcas = origem["origem"].marcas - origem["peso"]

        for destino in self.destinos:
            destino["destino"].marcas = destino["destino"].marcas + destino["peso"]
        # print(self.id)
