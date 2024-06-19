import tkinter as tk
from tkinter import ttk, font
import calendar
import math

class Eventos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#141414")
        self.controller = controller

        self.eventos_labels = []
        self.eventos_do_dia = {}
        self.criar_elementos()

    def criar_elementos(self):
        self.header_frame = ttk.Frame(self, style="Background.TFrame")
        self.header_frame.pack(pady=50)

        self.dia_label = ttk.Label(self.header_frame, 
                                   font=font.Font(family="Tahoma", size=35, weight="bold"), 
                                   background="#141414", foreground="white")
        self.dia_label.grid(row=0, column=1, padx=20)

        self.eventos_frame = ttk.Frame(self, style="Background.TFrame", borderwidth=1, relief=tk.SOLID)
        self.eventos_frame.pack(pady=60, padx=10, fill=tk.BOTH, expand=True)

        self.voltar_button = tk.Button(self, text="VOLTAR",
                                       command=lambda: self.controller.mostrar_tela("Calendario"),
                                       background="#1f1f1f", foreground="white", 
                                       font=font.Font(family="Tahoma", size=12, weight="bold"), 
                                       width=15, height=2, bd=0, highlightthickness=0)
        self.voltar_button.pack(pady=10)

        self.adicionar_button = tk.Button(self, text="ADICIONAR NOVO EVENTO",
                                       command=lambda: self.controller.mostrar_tela("Novo_Evento"),
                                       background="#1f1f1f", foreground="white", 
                                       font=font.Font(family="Tahoma", size=12, weight="bold"), 
                                       width=25, height=2, bd=0, highlightthickness=0)
        self.adicionar_button.pack(pady=10)
    
    def obter_cor_evento(self, evento):
        tipo_do_evento = evento['Tipo']
        if tipo_do_evento == 'Tarefa':
            return '#FFB61E'
        if tipo_do_evento == 'Compromisso':
            return evento['Cor']
        return '#32a8a4'
    
    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        
        # Limpando eventos anteriores
        for label in self.eventos_labels:
            label.destroy()
        self.eventos_labels.clear()

        data = self.controller.obter_dados('data')
        if data:
            dia = data.get('dia', '')
            mes = data.get('mes', '')
            ano = data.get('ano', '')
            mes_nome = "MARCO" if mes == 3 else calendar.month_name[mes].upper()     
            self.dia_label.config(text=f"{dia} DE {mes_nome}, {ano}")        
        
        eventos_do_dia = self.controller.obter_dados('eventos_do_dia')
        
        # Exibindo os eventos como uma lista dentro do eventos_frame
        if eventos_do_dia:
            for evento in eventos_do_dia:
                tipo_do_evento = evento['Tipo']
                if tipo_do_evento == 'Tarefa' or tipo_do_evento == 'Compromisso':
                    titulo = evento['Título']
                    descricao = evento['Descrição']
                    evento_texto = f"{titulo}: {descricao}"
                if tipo_do_evento == 'Lembrete':
                    mensagem = evento['Mensagem']
                    horario = evento['Horário']
                    evento_texto = f"({horario}): {mensagem}"

                cor = self.obter_cor_evento(evento)

                eventos_label = tk.Label(self.eventos_frame, text=evento_texto, font=font.Font(family="Tahoma", size=20, weight="bold"), 
                                        background=cor, foreground="white", padx=10, pady=5)
                eventos_label.pack(fill=tk.X)
                self.eventos_labels.append(eventos_label)
        
        # Garantindo que todos os elementos sejam criados se não existirem
        if self.header_frame is None or self.dia_label is None or self.voltar_button is None:
            self.criar_elementos()