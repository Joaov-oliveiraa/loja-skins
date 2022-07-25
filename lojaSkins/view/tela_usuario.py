import PySimpleGUI as sg

class TelaUsuario():

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-- USUARIO --', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Usuario', "RD1", key='1')],
            [sg.Radio('Alterar Steam Id e Telefone', "RD1", key='2')],
            [sg.Radio('Listar Usuario', "RD1", key='3')],
            [sg.Radio('Mostrar somatorio das compras do Usuario', "RD1", key='4')],
            [sg.Radio('Excluir Usuario', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('SIN Skins').Layout(layout)

    def pega_dados_usuario(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS USUARIO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome_usuario')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf_usuario')],
            [sg.Text('Steam id:', size=(15, 1)), sg.InputText('', key='steam_id')],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Loja Skins').Layout(layout)

        button, values = self.open()
        nome = values['nome_usuario']
        cpf = values['cpf_usuario']
        steam_id = values['steam_id']
        telefone = values['telefone']

        self.close()
        return {"nome_usuario": nome,"cpf_usuario": cpf, "steam_id": steam_id, "telefone": telefone}

    def mostra_usuario(self, dados_usuario):
        string_todos_usuarios = ""

        string_todos_usuarios = string_todos_usuarios + "NOME DO USUARIO: " + dados_usuario["nome_usuario"] + '\n'
        string_todos_usuarios = string_todos_usuarios + "CPF DO USUARIO: " + dados_usuario["cpf_usuario"] + '\n'
        string_todos_usuarios = string_todos_usuarios + "STEAM ID DO USUARIO: " + dados_usuario["steam_id"] + '\n'
        string_todos_usuarios = string_todos_usuarios + "TELEFONE DO USUARIO: " + dados_usuario["telefone"] + '\n'

        sg.Popup('-------- LISTA DE USUARIOS ----------', string_todos_usuarios)

    def seleciona_usuario(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-- SELECIONAR USUARIO --', font=("Helvica", 25))],
            [sg.Text('Digite o CPF do usuario que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf_usuario')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona usuario').Layout(layout)

        button, values = self.open()
        cpf = values['cpf_usuario']
        self.close()
        return cpf

    def mostra_usuario_com_valores(self, dados_usuario):
        string_todos_usuarios = ""

        string_todos_usuarios = string_todos_usuarios + "NOME DO USUARIO: " + dados_usuario["nome_usuario"] + '\n'
        string_todos_usuarios = string_todos_usuarios + "CPF DO USUARIO: " + dados_usuario["cpf_usuario"] + '\n'
        string_todos_usuarios = string_todos_usuarios + "STEAM ID DO USUARIO: " + dados_usuario["steam_id"] + '\n'
        string_todos_usuarios = string_todos_usuarios + "TELEFONE DO USUARIO: " + dados_usuario["telefone"] + '\n'
        string_todos_usuarios = string_todos_usuarios + "VALOR DAS SKINS COMPRADAS: " + dados_usuario["valores_venda"] + '\n'

        sg.Popup('-------- LISTA DE USUARIOS ----------', string_todos_usuarios)

    def pega_dados_usuario_para_alterar(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-- DADOS USUARIO PARA ALTERAR --', font=("Helvica", 25))],
            [sg.Text('Steam id:', size=(15, 1)), sg.InputText('', key='steam_id')],
            [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Loja Skins').Layout(layout)

        button, values = self.open()
        steam_id = values['steam_id']
        telefone = values['telefone']

        self.close()
        return {"steam_id": steam_id, "telefone": telefone}

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
