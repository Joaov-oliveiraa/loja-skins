import PySimpleGUI as sg


class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem Vindo ao SIN Skins', font=("Helvica",25))],
            [sg.Text('Escolha uma opção', font=("Helvica",15))],
            [sg.Radio('Skins',"RD1", key='1')],
            [sg.Radio('Usuarios',"RD1", key='2')],
            [sg.Radio('Vendas',"RD1", key='3')],
            [sg.Radio('Encerrar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)
