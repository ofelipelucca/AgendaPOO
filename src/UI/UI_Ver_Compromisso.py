from src.Implementações.Tarefa.Tarefa import Compromisso
from src.Implementações.Tarefa.ListaTarefa import ListaTarefa

import tkinter as tk
from tkinter import ttk, font

class Ver_Compromisso(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#141414")
        self.controller = controller
        self.parent = parent

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)

        # Limpar widgets anteriores
        for widget in self.winfo_children():
            widget.destroy()

        self.evento = self.controller.obter_dados('Evento')
        
        if self.evento:
            titulo = self.evento['Título']
            descricao = self.evento['Descrição']
            data = self.evento['Data']
            prioridades_validas = {
                1: "MUITO IMPORTANTE",
                2: "IMPORTANTE",
                3: "MENOS IMPORTANTE"
            }
            prioridade = prioridades_validas[self.evento['Prioridade']]
            estado = self.evento['Estado'].upper()
            cor = self.evento['Cor'].upper()
            local = self.evento['Local']
            horario = self.evento['Horário']

            self.header_frame = ttk.Frame(self, style="Background.TFrame", padding=(20, 10))
            self.header_frame.grid(row=0, column=0, columnspan=2, pady=20, sticky="ew")

            tk.Button(self.header_frame, text="VOLTAR",
                      command=lambda: self.controller.mostrar_tela("Eventos"),
                      background="#1f1f1f", foreground="white", 
                      font=font.Font(family="Tahoma", size=12, weight="bold"), 
                      width=15, height=2, bd=0, highlightthickness=0).grid(row=0, column=0, padx=5)

            ttk.Label(self.header_frame, text=titulo, 
                      font=font.Font(family="Tahoma", size=35, weight="bold"), 
                      background="#141414", foreground="white").grid(row=0, column=1, padx=20)

            tk.Button(self.header_frame, text="REMOVER",
                      command=lambda: self.remover_tarefa(),
                      background="#1f1f1f", foreground="white", 
                      font=font.Font(family="Tahoma", size=12, weight="bold"), 
                      width=15, height=2, bd=0, highlightthickness=0).grid(row=0, column=2, padx=5)

            self.content_frame = ttk.Frame(self, style="Background.TFrame", padding=(20, 10))
            self.content_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

            self.content_frame.grid_columnconfigure(1, weight=1)

            ttk.Label(self.content_frame, text="DESCRIÇÃO:", 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
            
            ttk.Label(self.content_frame, text=descricao, 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=0, column=1, sticky="w", padx=10, pady=5)
            
            ttk.Label(self.content_frame, text="DATA:", 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=1, column=0, sticky="w", padx=10, pady=5)
            
            ttk.Label(self.content_frame, text=data, 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=1, column=1, sticky="w", padx=10, pady=5)

            ttk.Label(self.content_frame, text="PRIORIDADE:", 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=2, column=0, sticky="w", padx=10, pady=5)
            
            ttk.Label(self.content_frame, text=prioridade, 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=2, column=1, sticky="w", padx=10, pady=5)
            
            ttk.Label(self.content_frame, text="ESTADO:", 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=3, column=0, sticky="w", padx=10, pady=5)
            
            ttk.Label(self.content_frame, text=estado, 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=3, column=1, sticky="w", padx=10, pady=5)
          
            ttk.Label(self.content_frame, text="LOCAL:", 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=5, column=0, sticky="w", padx=10, pady=5)
            
            ttk.Label(self.content_frame, text=local, 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=5, column=1, sticky="w", padx=10, pady=5)

            ttk.Label(self.content_frame, text="HORARIO:", 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=6, column=0, sticky="w", padx=10, pady=5)
            
            ttk.Label(self.content_frame, text=horario, 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=6, column=1, sticky="w", padx=10, pady=5)

    def remover_tarefa(self):
        email_do_usuario = self.controller.usuario['Email']
        compromisso = Compromisso(self.evento['Título'], self.evento['Descrição'], self.evento['Data'], self.evento['Prioridade'], self.evento['Estado'], 'laranja', self.evento['Local'], self.evento['Horário'])
        lista_de_tarefas = ListaTarefa()
        lista_de_tarefas.removerTarefa(compromisso, email_do_usuario)
        self.controller.mostrar_tela("Eventos")