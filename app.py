import PySimpleGUI as sg
from funcoes import *


class Tela:
    def __init__(self):
        sg.theme('BluePurple') # setando o tema da janela 
        # layout
        layout = [
            [sg.Text('Nome ou apelido :', size=(15,1)), 
                    sg.Input(size=(25,1),key='nome')], 
                [sg.Text('Email :', size=(15,1)),sg.Input(size=(25,1),key='email')],
                [sg.Text('Senha :', size=(15,1)),sg.InputText(size=(25,1),key='senha', password_char='*')],
                [sg.Button('Cadastrar', size=(15,1)), sg.Button('Sair', pad=(80,5,0)), sg.Push()],
                
                ] 
        #ler informaçoes dos inputs setados no layout
        self.tela = sg.Window('Cadastro de Player', layout, text_justification="r" )
        #extrair dados
        self.event, self.values = self.tela.read()
            
            
        
       
    def iniciar(self):
        
        
        idade = (self.values['idade'])
        email = (self.values['email'])
        senha = (self.values['senha'])

        # print(nome_completo, idade, email, senha)
        
         # layout 2
        layout = [
                [sg.Text('Informe seu Email e Senha', key='Info')],
                [sg.Text('Email :', size=(10,1)), 
                    sg.Input(size=(25,1),key='email_user')], 
                [sg.Text('Senha :', size=(10,1)),sg.Input(size=(25,1),key='senha_user')],[sg.Button('Validar Colaborador')],
                [sg.Text('Codigo de validação:', sg.Input(size=(10,1), key='codigo'))]
                ]



        if self.event == 'Cadastrar':
            self.tela = sg.Window('Validação de Colaborador', layout, resizable=True, element_justification='l')

        self.event, self.values = self.tela.read()

app = Tela()

