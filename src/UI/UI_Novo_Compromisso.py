from src.Implementações.Tarefa.Tarefa import Compromisso
from src.Implementações.Tarefa.ListaTarefa import ListaTarefa

import tkinter as tk
from tkinter import ttk

class UI_Compromisso(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="#141414")

        self.parent = parent

        ttk.Label(self, text="", font=self.parent.fonte,
                  background="#141414", foreground="white").grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self, text="TITULO:", font=self.parent.fonte,
                background="#141414", foreground="white").grid(row=1, column=1, padx=5, pady=5)
        self.titulo = ttk.Entry(self, width=50)
        self.titulo.grid(row=1, column=2, padx=10, pady=5)

        ttk.Label(self, text="DESCRICAO:", font=self.parent.fonte,
                background="#141414", foreground="white").grid(row=2, column=1, padx=10, pady=5)
        self.descricao = ttk.Entry(self, width=50)
        self.descricao.grid(row=2, column=2, padx=10, pady=5)

        ttk.Label(self, text="LOCAL:", font=self.parent.fonte,
                        background="#141414", foreground="white").grid(row=3, column=1, padx=10, pady=5)
        self.local = ttk.Entry(self, width=50)
        self.local.grid(row=3, column=2, padx=10, pady=5)

        ttk.Label(self, text="ESTADO:", font=self.parent.fonte,
                background="#141414", foreground="white").grid(row=4, column=1, padx=10, pady=5)
        self.estado = ttk.Combobox(self, values=["NÃO FEITO", "EM PROGRESSO", "FEITO"], width=30, state='readonly')
        self.estado.grid(row=4, column=2, padx=10, pady=5)

        ttk.Label(self, text="PRIORIDADE:", font=self.parent.fonte,
                background="#141414", foreground="white").grid(row=5, column=1, padx=10, pady=5)
        self.prioridade = ttk.Combobox(self, values=["MUITO IMPORTANTE", "IMPORTANTE", "MENOS IMPORTANTE"], width=30, state='readonly')
        self.prioridade.grid(row=5, column=2, padx=10, pady=5)

        ttk.Label(self, text="COR:", font=self.parent.fonte,
                background="#141414", foreground="white").grid(row=6, column=1, padx=5, pady=5)
        self.cor = ttk.Combobox(self, values=['LARANJA', 'AZUL', 'ROXO', 'ROSA'], width=15, state='readonly')
        self.cor.grid(row=6, column=2, padx=2, pady=5)

        ttk.Label(self, text="HORARIO:", font=self.parent.fonte,
                background="#141414", foreground="white").grid(row=1, column=3, padx=5, pady=5)
        self.horas = ttk.Combobox(self, values=[str(f"{horas:02d}h") for horas in range(0, 24)], width=5, state='readonly')
        self.horas.grid(row=1, column=4, padx=2, pady=5)

        self.minutos = ttk.Combobox(self, values=[str(f"{minutos:02d} min") for minutos in range(0, 60)], width=10, state='readonly')
        self.minutos.grid(row=1, column=5, padx=2, pady=5)

        self.segundos = ttk.Combobox(self, values=[str(f"{segundo:02d} seg") for segundo in range(0, 60)], width=7, state='readonly')
        self.segundos.grid(row=1, column=6, padx=2, pady=5)

        self.error_label = ttk.Label(self, text="", 
                                     font=self.parent.fonte, 
                                     background="#141414", foreground="white")
        self.error_label.place(relx=0.5, rely=0.15, anchor='s')

    def salvar_evento(self):
        try:
            titulo = self.titulo.get()
            if not titulo:
                ValueError("Insira um titulo.")

            descricao = self.descricao.get()
            if not descricao:
                ValueError("Insira uma descricao.")
            
            data_do_dia = self.parent.controller.obter_dados('data')
            
            dia = data_do_dia.get('dia', '')
            mes = data_do_dia.get('mes', '')
            ano = data_do_dia.get('ano', '')
            
            data = f"{dia:02d}/{mes:02d}/{ano}"

            prioridades_validas = {
                "MUITO IMPORTANTE": 1,
                "IMPORTANTE": 2,
                "MENOS IMPORTANTE": 3
            }
            prioridade = int(prioridades_validas.get(self.prioridade.get(), 3))
            if not prioridade:
                ValueError("Selecione uma prioridade.")

            estado = str(self.estado.get()).lower()
            if not estado:
                ValueError("Selecione um estado.")

            cor = self.cor.get()
            if not cor:
                ValueError("Selecione uma cor.")
        
            local = self.local.get()
            if not local:
                ValueError("Insira um local.")

            horas = self.horas.get().replace('h', '')
            minutos = self.minutos.get().replace(' min', '')
            segundos = self.segundos.get().replace(' seg', '')
            horario = f"{horas}:{minutos}:{segundos}"
            
            novo_compromisso = Compromisso(titulo, descricao, data, prioridade, estado, cor, local, horario)
            lista_de_tarefas = ListaTarefa()

            email_do_usuario = self.parent.controller.usuario['Email']

            lista_de_tarefas.adicionarTarefa(novo_compromisso, email_do_usuario)

            self.error_label.configure(text="")

            self.parent.controller.mostrar_tela("Calendario")

        except ValueError as e:
            self.error_label.configure(text=str(e)) # Caso ocorra, exibindo o erro na error_label