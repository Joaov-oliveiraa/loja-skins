class TelaSistema:

    def tela_opcoes(self):
        print("\n")
        print("-------- Bem vindo ao SIN Skins!!! ---------")
        print("Escolha sua opcao")
        print("1 - Skins")
        print("2 - Usuarios")
        print("3 - Vendas")
        print("0 - Finalizar sistema")

        opcao = input("Escolha a opcao: ")
        while not opcao.isdigit():
            print("\nOpcao invalida\n")
            opcao = input("Digite novamente uma opcao: ")
        opcao = int(opcao)
        while not 0 <= opcao <= 3:
            print("\nOpcao invalida\n")
            opcao = int(input("Digite novamente uma opcao: "))

        return opcao
