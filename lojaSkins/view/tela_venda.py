class TelaVenda:

    def tela_opcoes(self):
        print("\n")
        print("-------- VENDA ----------")
        print("Escolha a opcao")
        print("1 - Fazer Venda")
        print("2 - Listar Vendas")
        print("3 - Mostrar Estatísticas")
        print("0 - Retornar")

        opcao = input("Escolha a opcao: ")
        while not opcao.isdigit():
            print("\nOpcao invalida\n")
            opcao = input("Digite novamente uma opcao: ")
        opcao = int(opcao)
        while not 0 <= opcao <= 3:
            print("\nOpcao invalida\n")
            opcao = int(input("Digite novamente uma opcao: "))

        return opcao

    def pega_dados_venda(self):
        print("\n")
        print("-------- DADOS COMPRA ----------")
        cpf_usuario = input("CPF Usuario: ")
        codigo_skin = int(input("Codigo Skin: "))
        preco = float(input("Valor da transação: R$ "))

        return {"cpf_usuario": cpf_usuario, "codigo_skin": codigo_skin, "preco": preco}

    def mostra_venda(self, dados_venda):
        print("\n")
        print("CODIGO DA VENDA: ", dados_venda["codigo_transacao"])
        print("NOME DO USUARIO: ", dados_venda["nome_usuario"])
        print("CPF DO USUARIO: ", dados_venda["cpf_usuario"])
        print("CODIGO DA SKIN: ", dados_venda["codigo_skin"])
        print("NOME DA SKIN: ", dados_venda["nome_skin"])
        print("PREÇO: R$ ", dados_venda["preco"])
        print("\n")

    def seleciona_venda(self):
        print("\n")
        codigo = input("Código da venda que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)

    def pega_dados_venda_para_alterar(self):
        print("\n")
        print("-------- NOVO VALOR DA TRANSAÇÃO ----------")
        preco = float(input("Valor da transação: R$ "))

        return {"preco": preco}


    def mostra_estatisticas_das_vendas(self, estatisticas):
        print("\n")
        print("SALDO TOTAL DAS VENDAS: R$ ", estatisticas["saldo_vendas"])
        print("QUANTIDADE DE VENDAS: ", estatisticas["quantidade_vendas"])
        print("TICKET MÉDIO DAS VENDAS: ", estatisticas["media_vendas"])