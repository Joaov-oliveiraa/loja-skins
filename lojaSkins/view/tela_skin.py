class TelaSkin:

    def tela_opcoes(self):

        print("-------- SKINS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Skin")
        print("2 - Alterar Skin")
        print("3 - Listar Skin")
        print("4 - Excluir Skin")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def get_dados_skin(self):
        print("-------- DADOS SKIN ----------")
        arma = input("Nome da Arma: ")
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
        print("TITULO DA SKIN: ", dados_skin["arma"])
        print("NOME DA SKIN: ", dados_skin["nome_skin"])
        print("FLOAT DA SKIN: ", dados_skin["raridade_float"])
        print("PRECO DA SKIN: ", dados_skin["preco"])
        print("CODIGO DA SKIN: ", dados_skin["codigo_skin"])
        print("\n")

    def seleciona_skin(self):
        codigo_skin = input("Digite o codigo da skin: ")
        return codigo_skin

    def mostra_mensagem(self, msg):
        print(msg)
