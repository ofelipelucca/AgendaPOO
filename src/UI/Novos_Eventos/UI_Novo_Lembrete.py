from src.Implementações.Lembrete.Lembrete import Lembrete
from src.Implementações.Lembrete.ListaLembrete import ListaLembrete

import tkinter as tk
from tkinter import ttk

class UI_Lembrete(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="#141414")

        self.parent = parent

        self.error_label = ttk.Label(self, text="", 
                                     font=self.parent.fonte, 
                                     background="#141414", foreground="white")
        self.error_label.place(relx=0.5, rely=0.3, anchor='s')
                
        ttk.Label(self, text="", font=self.parent.fonte,
                  background="#141414", foreground="white").grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="MENSAGEM:", font=self.parent.fonte,
                  background="#141414", foreground="white").grid(row=1, column=1, padx=5, pady=5)
        self.mensagem = ttk.Entry(self, width=50)
        self.mensagem.grid(row=1, column=2, padx=10, pady=5)

        ttk.Label(self, text="HORARIO:", font=self.parent.fonte,
                background="#141414", foreground="white").grid(row=1, column=3, padx=5, pady=5)
        
        self.horas = ttk.Combobox(self, values=[str(f"{horas:02d}h") for horas in range(0, 24)], width=5, state='readonly')
        self.horas.grid(row=1, column=4, padx=2, pady=5)

        self.minutos = ttk.Combobox(self, values=[str(f"{minutos:02d} min") for minutos in range(0, 60)], width=10, state='readonly')
        self.minutos.grid(row=1, column=5, padx=2, pady=5)

        self.segundos = ttk.Combobox(self, values=[str(f"{segundo:02d} seg") for segundo in range(0, 60)], width=7, state='readonly')
        self.segundos.grid(row=1, column=6, padx=2, pady=5)

    def salvar_evento(self):
        try:
            mensagem = self.mensagem.get()
            if not mensagem:
                ValueError("Insira uma mensagem.")

            horas = int(self.horas.get().replace('h', ''))
            minutos = int(self.minutos.get().replace(' min', ''))
            segundos = int(self.segundos.get().replace(' seg', ''))
            horario = f"{horas:02d}:{minutos:02d}:{segundos:02d}"

            data_do_dia = self.parent.controller.obter_dados('data')
            
            dia = data_do_dia.get('dia', '')
            mes = data_do_dia.get('mes', '')
            ano = data_do_dia.get('ano', '')
            
            data = f"{dia:02d}/{mes:02d}/{ano}"

            novo_compromisso = Lembrete(data, horario, mensagem)
            lista_de_tarefas = ListaLembrete()

            email_do_usuario = self.parent.controller.usuario['Email']

            lista_de_tarefas.adicionarLembrete(novo_compromisso, email_do_usuario)

            self.error_label.configure(text="")

            self.parent.controller.mostrar_tela("Calendario")

        except ValueError as e:
            self.error_label.configure(text=str(e)) # Caso ocorra, exibindo o erro na error_label