class Usuario:

    def __init__(self, nome: str, cpf: str, steam_id: str, telefone: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__steam_id = steam_id
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def steam_id(self):
        return self.__steam_id

    @steam_id.setter
    def steam_id(self, steam_id: str):
        self.__steam_id = steam_id

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone
