from lojaSkins.entidade.usuario import Usuario
from lojaSkins.entidade.skin import Skin


class Venda:
    def __init__(self, usuario: Usuario, skin: Skin, codigo_transacao: int):
        if isinstance(usuario, Usuario):
            self.__usuario = usuario
        if isinstance(skin, Skin):
            self.__skin = skin
        self.__codigo_transacao = codigo_transacao

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario: Usuario):
        if isinstance(usuario, Usuario):
            self.__usuario = usuario

    @property
    def skin(self):
        return self.__skin

    @skin.setter
    def skin(self, skin: Skin):
        if isinstance(skin, Skin):
            self.__skin = skin

    @property
    def codigo_transacao(self):
        return self.__codigo_transacao

    @codigo_transacao.setter
    def codigo_transacao(self, codigo_transacao: int):
        self.__codigo_transacao = codigo_transacao
