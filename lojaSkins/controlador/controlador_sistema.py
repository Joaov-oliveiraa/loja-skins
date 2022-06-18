from lojaSkins.view.tela_sistema import TelaSistema
from lojaSkins.controlador.controlador_usuario import ControladorUsuarios
from lojaSkins.controlador.controlador_skin import ControladorSkins
from lojaSkins.controlador.controlador_venda import ControladorVendas


class ControladorSistema:

    def __int__(self):
        self.__controlador_skins = ControladorSkins(self)
        self.__controlador_usuarios = ControladorUsuarios(self)
        self.__controlador_vendas = ControladorVendas(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios

    @property
    def controlador_skins(self):
        return self.__controlador_skins

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_skins(self):
        self.__controlador_skins.abre_tela()

    def cadastra_usuarios(self):
        self.__controlador_usuarios.abre_tela()

    def cadastra_vendas(self):
        self.__controlador_vendas.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        print("executou abre tela do controlador sistema")
        lista_opcoes = {1: self.cadastra_skins,
                        2: self.cadastra_usuarios,
                        3: self.cadastra_vendas,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
