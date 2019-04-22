# -*- coding: utf-8 -*-


class Lugar:

    def __init__(self, lugar_conf):
        self.id = lugar_conf["id"]
        self.nome = lugar_conf["nome"]
        self.marcas = lugar_conf["marcas"]
        self.origens = []  # {"peso": 1, "origem": Transcao()}
        self.destinos = []  # {"peso": 1, "destino": Transcao()}

    @property
    def is_inicial(self):
        return not self.origens
