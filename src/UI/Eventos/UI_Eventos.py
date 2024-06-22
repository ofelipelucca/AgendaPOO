from src.Implementações.Tarefa.Tarefa import Tarefa
from src.Implementações.Lembrete.Lembrete import Lembrete
from src.Implementações.Compromisso.Compromisso import Compromisso
from src.Implementações.Tarefa.ListaTarefa import ListaTarefa
from src.Implementações.Compromisso.ListaCompromisso import ListaCompromisso
from src.Implementações.Lembrete.ListaLembrete import ListaLembrete

import tkinter as tk
from tkinter import ttk, font
import calendar

class Eventos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#141414")
        self.controller = controller

        self.eventos_labels = []
        self.eventos_do_dia = {}
        self.criar_elementos()

    def criar_elementos(self):
        self.header_frame = ttk.Frame(self, style="Background.TFrame")
        self.header_frame.pack(padx=10, pady=50)

        self.dia_label = ttk.Label(self.header_frame, 
                                   font=font.Font(family="Tahoma", size=35, weight="bold"), 
                                   background="#141414", foreground="white")
        self.dia_label.grid(row=0, column=1, padx=20)

        self.eventos_frame = ttk.Frame(self, style="Background.TFrame", borderwidth=1, relief=tk.SOLID)
        self.eventos_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

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
        for widget in self.eventos_frame.winfo_children():
            widget.destroy()

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

                miniframe = tk.Frame(self.eventos_frame, bg=cor, pady=5)
                miniframe.pack(fill=tk.X, expand=True, padx=5, pady=5)

                evento_label = tk.Label(miniframe, text=evento_texto, font=font.Font(family="Tahoma", size=15, weight="bold"), 
                                        background=cor, foreground="white", padx=10, pady=5)
                evento_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

                ver_evento_button = tk.Button(miniframe, text="VER",
                                              command=lambda e=evento: self.ver_evento(e),
                                              background="#1f1f1f", foreground="white", 
                                              font=font.Font(family="Tahoma", size=10, weight="bold"), 
                                              width=10, height=1, bd=0, highlightthickness=0)
                ver_evento_button.pack(side=tk.RIGHT, padx=5)

                remover_evento_button = tk.Button(miniframe, text="REMOVER",
                                                  command=lambda e=evento: self.remover_evento(e, miniframe),
                                                  background="#1f1f1f", foreground="white", 
                                                  font=font.Font(family="Tahoma", size=10, weight="bold"), 
                                                  width=10, height=1, bd=0, highlightthickness=0)
                remover_evento_button.pack(side=tk.RIGHT, padx=5)

                self.eventos_labels.append(miniframe)
                self.eventos_labels.append(evento_label)
                self.eventos_labels.append(ver_evento_button)
                self.eventos_labels.append(remover_evento_button)
        
        # Garantindo que todos os elementos sejam criados se não existirem
        if self.header_frame is None or self.dia_label is None or self.voltar_button is None:
            self.criar_elementos()

    def ver_evento(self, evento):
        self.controller.passar_dados('Evento', evento)
        tipo_do_evento = evento['Tipo']
        if tipo_do_evento == 'Tarefa':
            self.controller.mostrar_tela("Ver_Tarefa")
        if tipo_do_evento == 'Compromisso':
            self.controller.mostrar_tela("Ver_Compromisso")
        if tipo_do_evento == 'Lembrete':
            self.controller.mostrar_tela("Ver_Lembrete")

    def remover_evento(self, evento, frame):
        email_do_usuario = self.controller.usuario['Email']
        tipo_do_evento = evento['Tipo']
        if tipo_do_evento == 'Lembrete':
            lista_de_lembretes = ListaLembrete()
            lembrete = Lembrete(evento['Data'], evento['Horário'], evento['Mensagem'])
            lista_de_lembretes.removerLembrete(lembrete, email_do_usuario)
        if tipo_do_evento == 'Compromisso':
            lista_de_compromissos = ListaCompromisso()
            compromisso = Compromisso(evento['Título'], evento['Descrição'], evento['Data'], evento['Prioridade'], evento['Estado'], 'laranja', evento['Local'], evento['Horário'])
            lista_de_compromissos.removerCompromisso(compromisso, email_do_usuario)
        if tipo_do_evento == 'Tarefa':
            lista_de_tarefas = ListaTarefa()
            tarefa = Tarefa(evento['Título'], evento['Descrição'], evento['Data'], evento['Prioridade'], evento['Estado'])
            lista_de_tarefas.removerTarefa(tarefa, email_do_usuario)
        frame.pack_forget()