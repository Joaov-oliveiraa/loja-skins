class Skin:
    def __init__(self, arma: str, name_skin: str, raridade_float: float, preco: float, codigo: int):
        self.__arma = arma
        self.__name_skin = name_skin
        self.__raridade_float = raridade_float
        self.__preco = preco
        self.__codigo = codigo

    @property
    def gun(self):
        return self.__arma

    @gun.setter
    def gun(self, gun):
        self.__arma = gun

    @property
    def name_skin(self):
        return self.__name_skin

    @name_skin.setter
    def name_skin(self, name_skin):
        self.__name_skin = name_skin

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
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
