class TelaVenda:

    def tela_opcoes(self):
        print("-------- VENDA ----------")
        print("Escolha a opcao")
        print("1 - Fazer Compra")
        print("2 - Listar Compras")
        print("3 - Devolver Compra")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_venda(self):
        print("-------- DADOS COMPRA ----------")
        cpf = input("CPF Usuario: ")
        codigo = input("Codigo Skin: ")

        return {"cpf": cpf, "codigo": codigo}

    def mostra_venda(self, dados_venda):
        print("CODIGO DA VENDA: ", dados_venda["codigo_venda"])
        print("NOME DA SKIN: ", dados_venda["nome_skin"])
        print("CODIGO DA SKIN: ", dados_venda["codigo_skin"])
        print("NOME DO USUARIO: ", dados_venda["nome_usuario"])
        print("CPF DO USUARIO: ", dados_venda["cpf_usuario"])
        print("\n")

    def seleciona_venda(self):
        codigo = input("Código da venda que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)