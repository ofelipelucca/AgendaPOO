from src.UI.UI_Nova_Tarefa import UI_Tarefa
from src.UI.UI_Novo_Compromisso import UI_Compromisso
from src.UI.UI_Novo_Lembrete import UI_Lembrete

import tkinter as tk
from tkinter import ttk, font
import calendar

class Novo_Evento(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#141414")
        self.controller = controller
        
        self.tipo_evento = tk.StringVar(value="Tarefa")
        
        self.meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                      'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        
        self.anos_validos = [str(year) for year in range(2020, 2031)]  # Intervalo de anos

        self.fonte = font.Font(family="Tahoma", size=13, weight="normal")
        
        self.frames = {}
        
        self.criar_elementos()

    def criar_elementos(self):
        self.fonte = font.Font(family="Tahoma", size=13, weight="normal")
        self.header_frame = ttk.Frame(self, style="Background.TFrame")
        self.header_frame.pack(pady=50)

        self.register_label = ttk.Label(self.header_frame, text="NOVO EVENTO",
                                        font=font.Font(family="Tahoma", size=35, weight="bold"),
                                        background="#141414", foreground="white")
        self.register_label.grid(row=0, column=1, padx=20)

        self.voltar_button = tk.Button(self.header_frame, text="VOLTAR",
                                       command=lambda: self.controller.mostrar_tela("Calendario"),
                                       background="#1f1f1f", foreground="white", 
                                       font=font.Font(family="Tahoma", size=12, weight="bold"), 
                                       width=15, height=2, bd=0, highlightthickness=0)
        self.voltar_button.grid(row=0, column=0, padx=10)

        self.salvar_button = tk.Button(self.header_frame, text="SALVAR",
                                       command=lambda: self.salvar_evento(),
                                       background="#1f1f1f", foreground="white", 
                                       font=font.Font(family="Tahoma", size=12, weight="bold"), 
                                       width=15, height=2, bd=0, highlightthickness=0)
        self.salvar_button.grid(row=0, column=3, padx=10)

        # Frame para seleção do tipo de evento
        self.tipo_frame = ttk.Frame(self, style="Background.TFrame")
        self.tipo_frame.pack(pady=20)

        ttk.Label(self.tipo_frame, text="TIPO DE EVENTO:", font=font.Font(size=12),
                  background="#141414", foreground="white").grid(row=0, column=0, padx=10, pady=10)

        self.radiobutton_tarefa = tk.Radiobutton(self.tipo_frame, text="Tarefa", variable=self.tipo_evento, value="Tarefa", 
                                                 command=self.atualizar_tipo_evento, background="#1f1f1f", foreground="white", 
                                                 font=font.Font(family="Tahoma", size=12, weight="normal"), width=15, height=2, bd=0, highlightthickness=0)
        self.radiobutton_tarefa.grid(row=0, column=1, padx=10)
        
        self.radiobutton_compromisso = tk.Radiobutton(self.tipo_frame, text="Compromisso", variable=self.tipo_evento, value="Compromisso", 
                                                      command=self.atualizar_tipo_evento, background="#1f1f1f", foreground="white", 
                                                      font=font.Font(family="Tahoma", size=12, weight="normal"), width=15, height=2, bd=0, highlightthickness=0)
        self.radiobutton_compromisso.grid(row=0, column=2, padx=10)
        
        self.radiobutton_lembrete = tk.Radiobutton(self.tipo_frame, text="Lembrete", variable=self.tipo_evento, value="Lembrete", 
                                                   command=self.atualizar_tipo_evento, background="#1f1f1f", foreground="white", 
                                                   font=font.Font(family="Tahoma", size=12, weight="normal"), width=15, height=2, bd=0, highlightthickness=0)
        self.radiobutton_lembrete.grid(row=0, column=3, padx=10)

        # Frames para cada tipo de evento
        self.frame_tarefa = UI_Tarefa(self)
        self.frame_compromisso = UI_Compromisso(self)
        self.frame_lembrete = UI_Lembrete(self)
        
        self.frames["Tarefa"] = self.frame_tarefa
        self.frames["Compromisso"] = self.frame_compromisso
        self.frames["Lembrete"] = self.frame_lembrete
        
        self.frame_tarefa.pack(pady=20)
        self.frame_compromisso.pack_forget()
        self.frame_lembrete.pack_forget()

    def atualizar_tipo_evento(self):
        tipo = self.tipo_evento.get()
        for frame in self.frames.values():
            frame.pack_forget()
        
        self.frames[tipo].pack(pady=20)

    def atualizar_dias_validos(self, combobox_dia, combobox_mes, combobox_ano):
        try:
            dia = combobox_dia.get()
            mes = combobox_mes.get()
            ano = combobox_ano.get()
        except:
            return

        if mes and ano:
            mes_selecionado = self.meses.index(mes) + 1  # Converter o nome dos meses para índice de 1 a 12
            ano_selecionado = int(ano)

            self.dias_validos = [str(day) for day in range(1, calendar.monthrange(ano_selecionado, mes_selecionado)[1] + 1)]

            combobox_dia.config(values=self.dias_validos)

            if dia not in self.dias_validos:
                if self.dias_validos:
                    combobox_dia.set(self.dias_validos[0])
                    
    def salvar_evento(self):
        tipo = self.tipo_evento.get()
        self.frames[tipo].salvar_evento()