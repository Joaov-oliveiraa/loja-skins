class TelaSkin:

    def tela_opcoes(self):
        print("\n")
        print("-------- SKINS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Skin")
        print("2 - Alterar Skin")
        print("3 - Listar Skin")
        print("4 - Excluir Skin")
        print("0 - Retornar")

        opcao = input("Escolha a opcao: ")
        while not opcao.isdigit():
            print("\nOpcao invalida\n")
            opcao = input("Digite novamente uma opcao: ")
        opcao = int(opcao)
        while not 0 <= opcao <= 4:
            print("\nOpcao invalida\n")
            opcao = int(input("Digite novamente uma opcao: "))

        return opcao

    def get_dados_skin(self):
        print("\n")
        print("-------- DADOS SKIN ----------")
        arma = input("Arma: ")
        nome_skin = input("Nome da Skin: ")
        raridade_float = float(input("Float da skin: "))
        preco = float(input("Preco da skin: "))
        codigo_skin = int(input("Codigo da skin: "))

        return {"arma": arma,
                "nome_skin": nome_skin,
                "raridade_float": raridade_float,
                "preco": preco,
                "codigo_skin": codigo_skin}

    def mostra_dados_skin(self, dados_skin):
        print("\n")
        print("ARMA: ", dados_skin["arma"])
        print("NOME DA SKIN: ", dados_skin["nome_skin"])
        print("FLOAT DA SKIN: ", dados_skin["raridade_float"])
        print("PRECO DA SKIN: ", dados_skin["preco"])
        print("CODIGO DA SKIN: ", dados_skin["codigo_skin"])

    def seleciona_skin(self):
        print("\n")
        codigo_skin = input("Digite o codigo da skin: ")
        return codigo_skin

    def mostra_mensagem(self, msg):
        print(msg)

    def get_dados_skin_para_alterar(self):
        print("\n")
        print("-------- ALTERAÇÃO DOS DADOS DA SKIN ----------")
        preco = float(input("Preco da skin: "))

        return {"preco": preco}