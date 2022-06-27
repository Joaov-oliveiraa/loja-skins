class TelaUsuario:

    def tela_opcoes(self):
        print("\n")
        print("-------- USUARIO ----------")
        print("Escolha a opcao")
        print("1 - Incluir Usuario")
        print("2 - Alterar Steam ID e Telefone do Usuario")
        print("3 - Listar Usuarios")
        print("4 - Mostrar somatorio das compras do Usuario")
        print("5 - Excluir Usuario")
        print("0 - Retornar")

        opcao = input("Escolha a opcao: ")
        while not opcao.isdigit():
            print("\nOpcao invalida\n")
            opcao = input("Digite novamente uma opcao: ")
        opcao = int(opcao)
        while not 0 <= opcao <= 5:
            print("\nOpcao invalida\n")
            opcao = int(input("Digite novamente uma opcao: "))

        return opcao


    def pega_dados_usuario(self):
        print("\n")
        print("-------- DADOS USUARIO ----------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        steam_id = input("STEAM ID: ").upper()
        telefone = input("Telefone (apenas numero): ")

        while len(cpf) is not 11 or not cpf.isdigit() :
            cpf = input("CPF inválido, por favor, digite novamente:  ")
        while len(telefone) is not 9 or not telefone.isdigit():
            telefone = input("Telefone inválido, por favor digite novamente: ")

        return {"nome_usuario": nome, "cpf_usuario": cpf, "steam_id": steam_id, "telefone": telefone}

    def mostra_usuario(self, dados_usuario):
        print("\n")
        print("NOME DO USUARIO: ", dados_usuario["nome_usuario"])
        print("CPF DO USUARIO: ", dados_usuario["cpf_usuario"])
        print("STEAM ID DO USUARIO: ", dados_usuario["steam_id"])
        print("FONE DO USUARIO: ", dados_usuario["telefone"])

    def seleciona_usuario(self):
        print("\n")
        cpf = input("CPF do usuario que deseja selecionar: ")
        while len(cpf) is not 11 or not cpf.isdigit() :
            cpf = input("CPF inválido, por favor digite novamente :  ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)

    def pega_dados_usuario_para_alterar(self):
        print("\n")
        print("-------- ALTERAR DADOS USUARIO ----------")
        steam_id = input("STEAM ID: ")
        telefone = input("Telefone: ")

        while len(telefone) is not 9 or not telefone.isdigit():
            telefone = input("Telefone inválido, por favor digite novamente: ")

        return {"steam_id": steam_id, "telefone": telefone}

    def mostra_usuario_com_valores(self, dados_usuario):
        print("\n")
        print("NOME DO USUARIO: ", dados_usuario["nome_usuario"])
        print("CPF DO USUARIO: ", dados_usuario["cpf_usuario"])
        print("STEAM ID DO USUARIO: ", dados_usuario["steam_id"])
        print("FONE DO USUARIO: ", dados_usuario["telefone"])
        print("VALOR DAS SKINS COMPRADAS: ", dados_usuario["valores_vendas"])