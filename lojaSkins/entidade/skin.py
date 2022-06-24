class Skin:
    def __init__(self, arma: str, nome_skin: str, raridade_float: float, preco: float, codigo_skin: int):
        self.__arma = arma
        self.__nome_skin = nome_skin
        self.__raridade_float = raridade_float
        self.__preco = preco
        self.__codigo_skin = codigo_skin

    @property
    def arma(self):
        return self.__arma

    @arma.setter
    def arma(self, arma):
        self.__arma = arma

    @property
    def nome_skin(self):
        return self.__nome_skin

    @nome_skin.setter
    def nome_skin(self, nome_skin):
        self.__nome_skin = nome_skin

    @property
    def raridade_float(self):
        return self.__raridade_float

    @raridade_float.setter
    def raridade_float(self, raridade_float):
        self.__raridade_float = raridade_float

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def codigo_skin(self):
        return self.__codigo_skin

    @codigo_skin.setter
    def codigo_skin(self, codigo_skin):
        self.__codigo_skin = codigo_skin
