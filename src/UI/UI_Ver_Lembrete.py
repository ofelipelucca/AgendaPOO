from src.Implementações.Lembrete.Lembrete import Lembrete
from src.Implementações.Lembrete.ListaLembrete import ListaLembrete

import tkinter as tk
from tkinter import ttk, font

class Ver_Lembrete(tk.Frame):
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
            mensagem = self.evento['Mensagem']
            data = self.evento['Data']
            horario = self.evento['Horário']

            self.header_frame = ttk.Frame(self, style="Background.TFrame", padding=(20, 10))
            self.header_frame.grid(row=0, column=0, columnspan=2, pady=20, sticky="ew")

            tk.Button(self.header_frame, text="VOLTAR",
                      command=lambda: self.controller.mostrar_tela("Eventos"),
                      background="#1f1f1f", foreground="white", 
                      font=font.Font(family="Tahoma", size=12, weight="bold"), 
                      width=15, height=2, bd=0, highlightthickness=0).grid(row=0, column=0, padx=70)

            tk.Button(self.header_frame, text="REMOVER",
                      command=lambda: self.remover_tarefa(),
                      background="#1f1f1f", foreground="white", 
                      font=font.Font(family="Tahoma", size=12, weight="bold"), 
                      width=15, height=2, bd=0, highlightthickness=0).grid(row=0, column=2, padx=70)

            self.content_frame = ttk.Frame(self, style="Background.TFrame", padding=(20, 10))
            self.content_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

            self.content_frame.grid_columnconfigure(1, weight=1)

            ttk.Label(self.content_frame, text="MENSAGEM:", 
                      font=font.Font(family="Tahoma", size=18, weight="bold"), 
                      background="#141414", foreground="white").grid(row=0, column=0, padx=20)
            
            ttk.Label(self.content_frame, text=mensagem, 
                      font=font.Font(family="Tahoma", size=18, weight="bold"), 
                      background="#141414", foreground="white").grid(row=0, column=1, padx=20)

            ttk.Label(self.content_frame, text="HORARIO:", 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=1, column=0, sticky="w", padx=10, pady=5)
            
            ttk.Label(self.content_frame, text=horario, 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=1, column=1, sticky="w", padx=10, pady=5)
            
            ttk.Label(self.content_frame, text="DATA:", 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=2, column=0, sticky="w", padx=10, pady=5)
            
            ttk.Label(self.content_frame, text=data, 
                      font=font.Font(family="Tahoma", size=15, weight="bold"), 
                      background="#141414", foreground="white").grid(row=2, column=1, sticky="w", padx=10, pady=5)

    def remover_tarefa(self):
        email_do_usuario = self.controller.usuario['Email']
        lembrete = Lembrete(self.evento['Data'], self.evento['Horário'], self.evento['Mensagem'])
        lista_de_lembretes = ListaLembrete()
        lista_de_lembretes.removerLembrete(lembrete, email_do_usuario)
        self.controller.mostrar_tela("Eventos")