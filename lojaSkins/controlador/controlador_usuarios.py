from lojaSkins.view.tela_usuario import TelaUsuario
from lojaSkins.entidade.usuario import Usuario


class ControladorUsuarios:

    def __init__(self, controlador_sistema):
        self.usuarios = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_usuario = TelaUsuario()

    def adiciona_2_usuarios(self):
        usuario1 = Usuario("Renan Felix", "111", "renanfelix", "99")
        usuario2 = Usuario("Joao Victor", "222", "joao", "91")
        self.usuarios.append(usuario1)
        self.usuarios.append(usuario2)


    def pega_usuario_por_cpf(self, cpf: str):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def adicionar_usuario(self):
        dados_usuario = self.__tela_usuario.pega_dados_usuario()
        usuario = Usuario(dados_usuario["nome_usuario"],
                          dados_usuario["cpf_usuario"],
                          dados_usuario["steam_id"],
                          dados_usuario["telefone"])
        self.usuarios.append(usuario)

    def alterar_usuario(self):
        self.lista_usuarios()
        cpf_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.pega_usuario_por_cpf(cpf_usuario)

        if usuario is not None:
            novos_dados_usuario = self.__tela_usuario.pega_dados_usuario()
            usuario.nome = novos_dados_usuario["nome_usuario"]
            usuario.cpf = novos_dados_usuario["cpf_usuario"]
            usuario.steam_id = novos_dados_usuario["steam_id"]
            usuario.telefone = novos_dados_usuario["telefone"]
            self.lista_usuarios()
        else:
            self.__tela_usuario.mostra_mensagem("Usuario nao cadastrado")

    def lista_usuarios(self):
        for usuario in self.usuarios:
            self.__tela_usuario.mostra_usuario({"nome_usuario": usuario.nome,
                                                "cpf_usuario": usuario.cpf,
                                                "steam_id": usuario.steam_id,
                                                "telefone": usuario.telefone})

    def excluir_usuario(self):
        self.lista_usuarios()
        cpf_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.pega_usuario_por_cpf(cpf_usuario)

        if usuario is not None:
            self.usuarios.remove(usuario)
            self.lista_usuarios()
        else:
            self.__tela_usuario.mostra_mensagem("Usuario nao cadastrado")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_usuario,
                        2: self.alterar_usuario,
                        3: self.lista_usuarios,
                        4: self.excluir_usuario,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()
