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
            if venda.codigo_transacao == codigo:
                return venda
        return None

    def incluir_venda(self):
        self.__controlador_sistema.controlador_usuarios.lista_usuarios()
        self.__controlador_sistema.controlador_skins.lista_skin()
        dados_venda = self.__tela_venda.pega_dados_venda()

        usuario = self.__controlador_sistema.controlador_usuarios.pega_usuario_por_cpf(dados_venda["cpf_usuario"])
        skin = self.__controlador_sistema.controlador_skins.pega_skin_por_codigo(dados_venda["codigo_skin"])
        self.__controlador_sistema.controlador_skins.alterar_preco_skin(skin, dados_venda["preco"])
        venda = Venda(usuario, skin, randint(0, 100))
        if venda not in self.__vendas:
            self.__vendas.append(venda)
            self.__controlador_sistema.controlador_usuarios.adiciona_valor_da_venda(usuario, dados_venda["preco"])
        if skin is not None:
            self.__controlador_sistema.controlador_skins.remove_skin_da_lista(skin)

    def alterar_venda(self):
        self.lista_venda()
        codigo_transacao = self.__tela_venda.seleciona_venda()
        venda = self.pega_venda_por_codigo(codigo_transacao)

        if venda is not None:
            novos_dados_venda = self.__tela_venda.pega_dados_venda_para_alterar()
            venda.skin.preco = novos_dados_venda["preco"]
            self.lista_venda()
        else:
            self.__tela_venda.mostra_mensagem("Venda nao cadastrada")

    def lista_venda(self):
        for venda in self.__vendas:
            self.__tela_venda.mostra_venda({"codigo_transacao": venda.codigo_transacao,
                                            "nome_usuario": venda.usuario.nome,
                                            "cpf_usuario": venda.usuario.cpf,
                                            "codigo_skin": venda.skin.codigo_skin,
                                            "nome_skin": venda.skin.nome_skin,
                                            "preco": venda.skin.preco})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_venda, 2: self.lista_venda,
                        3: self.estatisticas_das_vendas, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_venda.tela_opcoes()]()


    def estatisticas_das_vendas(self):
        saldo_vendas = 0
        quantidade_de_vendas = len(self.__vendas)
        for venda in self.__vendas:
            saldo_vendas += venda.skin.preco

        media_vendas = round(saldo_vendas / quantidade_de_vendas, 2)
        self.__tela_venda.mostra_estatisticas_das_vendas({"saldo_vendas": saldo_vendas,
                                                          "quantidade_vendas": quantidade_de_vendas,
                                                          "media_vendas": media_vendas})

    def faca_2_vendas(self):
        usuario1 = self.__controlador_sistema.controlador_usuarios.pega_usuario_por_cpf("11122233344")
        skin3 = self.__controlador_sistema.controlador_skins.pega_skin_por_codigo(3)
        venda1 = Venda(usuario1, skin3, randint(0, 100))
        self.__vendas.append(venda1)
        self.__controlador_sistema.controlador_skins.remove_skin_da_lista(skin3)
        usuario2 = self.__controlador_sistema.controlador_usuarios.pega_usuario_por_cpf("12345678900")
        skin4 = self.__controlador_sistema.controlador_skins.pega_skin_por_codigo(4)
        venda2 = Venda(usuario2, skin4, randint(0, 100))
        self.__vendas.append(venda2)
        self.__controlador_sistema.controlador_skins.remove_skin_da_lista(skin4)