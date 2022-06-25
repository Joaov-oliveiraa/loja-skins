class TelaVenda:

    def tela_opcoes(self):
        print("-------- VENDA ----------")
        print("Escolha a opcao")
        print("1 - Fazer Venda")
        print("2 - Listar Vendas")
        print("3 - Excluir Venda")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_venda(self):
        print("-------- DADOS COMPRA ----------")
        cpf_usuario = input("CPF Usuario: ")
        codigo_skin = input("Codigo Skin: ")

        return {"cpf_usuario": cpf_usuario, "codigo_skin": codigo_skin}

    def mostra_venda(self, dados_venda):
        print("CODIGO DA VENDA: ", dados_venda["codigo_transacao"])
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