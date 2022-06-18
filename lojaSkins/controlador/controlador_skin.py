from lojaSkins.view.tela_skin import TelaSkin
from lojaSkins.entidade.skin import Skin


class ControladorSkins:

    def __init__(self, controlador_sistema):
        self.__skins = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_skin = TelaSkin()

    def pega_skin_por_codigo(self, codigo: int):
        for skin in self.__skins:
            if skin.codigo == codigo:
                return skin
        return None

    def incluir_skin(self):
        dados_skin = self.__tela_skin.get_dados_skin()
        skin = Skin(dados_skin["arma"], dados_skin["name_skin"],
                    dados_skin["raridade_float"], dados_skin["preco"],
                    dados_skin["codigo"])
        self.__skins.append(skin)

    def alterar_skin(self):
        self.lista_skin()
        codigo_skin = self.__tela_skin.seleciona_skin()
        skin = self.pega_skin_por_codigo(codigo_skin)

        if skin is not None:
            novos_dados_skin = self.__tela_skin.get_dados_skin()
            skin.arma = novos_dados_skin["arma"]
            skin.arma = novos_dados_skin["name_skin"]
            skin.arma = novos_dados_skin["raridade_float"]
            skin.arma = novos_dados_skin["preco"]
            skin.arma = novos_dados_skin["codigo"]
            self.lista_skin()
        else:
            self.__tela_skin.mostra_mensagem("--Skin não cadastrada--")

    def lista_skin(self):
        for skin in self.__skins:
            self.__tela_skin.mostra_dados_skin(
                {"arma": skin.arma,
                    "name_skin": skin.name_skin,
                    "raridade_float": skin.raridade_float,
                    "preco": skin.preco,
                    "codigo": skin.codigo})

    def excluir_skin(self):
        self.lista_skin()
        codigo_skin = self.__tela_skin.seleciona_skin()
        skin = self.pega_skin_por_codigo(codigo_skin)

        if skin is not None:
            self.__skins.remove(skin)
            self.lista_skin()
        else:
            self.__tela_skin.mostra_mensagem("--Skin não cadastrada--")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.lista_skin(),
                        2: self.alterar_skin(),
                        3: self.lista_skin(),
                        4: self.excluir_skin(),
                        5: self.retornar()}

        continua = True
        while continua:
            lista_opcoes[self.__tela_skin.tela_opcoes()]()