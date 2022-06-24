class TelaUsuario:

    def tela_opcoes(self):
        print("-------- USUARIO ----------")
        print("Escolha a opcao")
        print("1 - Incluir Usuario")
        print("2 - Alterar Usuario")
        print("3 - Listar Usuario")
        print("4 - Excluir Usuario")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_usuario(self):
        print("-------- DADOS USUARIO ----------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        steam_id = input("STEAM ID: ")
        telefone = input("Telefone: ")


        return {"nome_usuario": nome, "cpf_usuario": cpf, "steam_id": steam_id, "telefone": telefone}

    def mostra_usuario(self, dados_usuario):
        print("NOME DO USUARIO: ", dados_usuario["nome_usuario"])
        print("CPF DO USUARIO: ", dados_usuario["cpf_usuario"])
        print("STEAM ID DO USUARIO: ", dados_usuario["steam_id"])
        print("FONE DO USUARIO: ", dados_usuario["telefone"])
        print("\n")

    def seleciona_usuario(self):
        cpf = input("CPF do usuario que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)