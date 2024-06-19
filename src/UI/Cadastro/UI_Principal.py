##########################################################################################
#
#                       TO DO:
#                          - Sistema de login para o usuário acessar seus eventos *
#                          - Carregar os eventos direto do banco de dados, importando e salvando todos os campos necessários, 
#                            incluindo a cor de cada tipo de evento (Tarefa, Compromisso, Lembrete) *
#                          - Sistema e janela para o usuário adicionar seus próprios eventos
#                          - Organizar e modularizar o código
#           
#                           * depende da implementação do banco de dados
#                          
##########################################################################################

from src.UI.Calendario.UI_Calendario import Calendario
from src.UI.Cadastro.UI_Login import Login
from src.UI.Cadastro.UI_Register import Register
from src.UI.Eventos.UI_Eventos import Eventos
from src.UI.Novos_Eventos.UI_Novo_Evento import Novo_Evento
from src.UI.Ver_Evento.UI_Ver_Tarefa import Ver_Tarefa
from src.UI.Ver_Evento.UI_Ver_Compromisso import Ver_Compromisso
from src.UI.Ver_Evento.UI_Ver_Lembrete import Ver_Lembrete

import tkinter as tk

class Principal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Agenda")
        self.geometry("950x625")
        self.minsize(950, 625)
        self.resizable(True, True)
        self.configure(background="#141414")
        self.iconbitmap('assets/favicon.ico')

        container = tk.Frame(self, bg="#141414")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.usuario = None
        self.args = {}
        self.frames = {}
        self.classes = {Register, Login, Calendario, Eventos, Novo_Evento, Ver_Tarefa, Ver_Compromisso, Ver_Lembrete}

        for F in self.classes:
            pagina_nome = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[pagina_nome] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela("Login")

    def mostrar_tela(self, pagina_nome):
        frame = self.frames[pagina_nome]
        frame.tkraise()

    def passar_dados(self, chave, valor):
        self.args[chave] = valor

    def obter_dados(self, chave):
        return self.args.get(chave, None)