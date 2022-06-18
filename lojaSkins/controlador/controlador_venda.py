from lojaSkins.view.tela_venda import TelaVenda
from lojaSkins.entidade.venda import Venda

from random import randint


class ControladorVendas:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__vendas = []
        self.__tela_venda = TelaVenda()

    def pega_venda_por_codigo(self, codigo: int):
        for venda in self.__vendas:
            if venda.codigo == codigo:
                return venda
        return None

    def incluir_venda(self):
        self.__controlador_sistema.controlador_usuaarios.lista_usuarios()
        self.__controlador_sistema.controlador_skins.lista_skins()
        dados_venda = self.__tela_venda.pega_dados_venda()

        usuario = self.__controlador_sistema.controlador_amigos.pega_venda_por_cpf(dados_venda["cpf"])
        skin = self.__controlador_sistema.controlador_skins.pega_skin_por_codigo(dados_venda["codigo"])
        venda = Venda(usuario, skin, randint(0, 100))
        self.__vendas.append(venda)

    def lista_venda(self):
        for venda in self.__vendas:
            self.__tela_venda.mostra_venda({"codigo": venda.codigo,
                                            "titulo_livro": venda.skin.name_skin,
                                            "codigo_livro": venda.skin.codigo,
                                            "nome_amigo": venda.usuario.nome,
                                            "cpf_amigo": venda.usuario.cpf})

    def excluir_venda(self):
        self.lista_venda()
        codigo_venda = self.__tela_venda.seleciona_venda()
        venda = self.pega_venda_por_codigo(int(codigo_venda))

        if venda is not None:
            self.__vendas.remove(venda)
            self.lista_venda()
        else:
            self.__tela_venda.mostra_mensagem("Venda não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_venda, 2: self.lista_venda, 3: self.excluir_venda,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_venda.tela_opcoes()]()
