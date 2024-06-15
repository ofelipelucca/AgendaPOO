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

import tkinter as tk

from UI_Calendario import Calendario
from UI_Login import Login
from UI_Register import Register

class Principal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Agenda")
        self.geometry("900x600")
        self.minsize(900, 600)
        self.resizable(True, True)
        self.configure(background="#141414")
        self.iconbitmap('assets/favicon.ico')

        container = tk.Frame(self, bg="#141414")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.usuario = None

        self.frames = {}
        for F in (Register, Login, Calendario):
            pagina_nome = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[pagina_nome] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela("Register")

    def mostrar_tela(self, pagina_nome):
        frame = self.frames[pagina_nome]
        frame.tkraise()

if __name__ == "__main__":
    app = Principal()
    app.mainloop()