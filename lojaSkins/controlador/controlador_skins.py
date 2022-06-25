from lojaSkins.view.tela_skin import TelaSkin
from lojaSkins.entidade.skin import Skin


class ControladorSkins:

    def __init__(self, controlador_sistema):
        self.__skins = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_skin = TelaSkin()

    def adiciona_2_skins(self):
        skin1 = Skin("AK-47", "Red Line", 0.003, 25.50, 1)
        skin2 = Skin("AWP", "Red Line", 0.0673, 50.00, 2)
        self.__skins.append(skin1)
        self.__skins.append(skin2)

    def pega_skin_por_codigo(self, codigo: int):
        for skin in self.__skins:
            if skin.codigo_skin == codigo:
                return skin
        return None

    def incluir_skin(self):
        dados_skin = self.__tela_skin.get_dados_skin()
        skin = Skin(dados_skin["arma"], dados_skin["nome_skin"],
                    dados_skin["raridade_float"], dados_skin["preco"],
                    dados_skin["codigo_skin"])
        self.__skins.append(skin)

    def alterar_skin(self):
        self.lista_skin()
        codigo_skin = int(self.__tela_skin.seleciona_skin())
        skin = self.pega_skin_por_codigo(codigo_skin)

        if skin is not None:
            novos_dados_skin = self.__tela_skin.get_dados_skin()
            skin.arma = novos_dados_skin["arma"]
            skin.nome_skin = novos_dados_skin["nome_skin"]
            skin.raridade_float = novos_dados_skin["raridade_float"]
            skin.preco = novos_dados_skin["preco"]
            skin.codigo_skin = novos_dados_skin["codigo_skin"]
            self.lista_skin()
        else:
            self.__tela_skin.mostra_mensagem("--Skin não cadastrada--")

    def lista_skin(self):
        for skin in self.__skins:
            self.__tela_skin.mostra_dados_skin(
                {"arma": skin.arma,
                    "nome_skin": skin.nome_skin,
                    "raridade_float": skin.raridade_float,
                    "preco": skin.preco,
                    "codigo_skin": skin.codigo_skin})

    def excluir_skin(self):
        self.lista_skin()
        codigo_skin = int(self.__tela_skin.seleciona_skin())
        skin = self.pega_skin_por_codigo(codigo_skin)

        if skin is not None:
            self.__skins.remove(skin)
            self.lista_skin()
        else:
            self.__tela_skin.mostra_mensagem("--Skin não cadastrada--")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_skin, 2: self.alterar_skin, 3: self.lista_skin, 4: self.excluir_skin,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_skin.tela_opcoes()]()
