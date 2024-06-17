from src.Implementações.Tarefa import Compromisso

import tkinter as tk
from tkinter import ttk, font
import calendar

class Novo_Evento(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#141414")
        self.controller = controller
        
        self.tipo_evento = tk.StringVar()
        
        self.meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                      'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        
        self.anos_validos = [str(year) for year in range(2020, 2031)]  # Intervalo de anos
        
        self.dias_validos = []
        
        self.criar_elementos()

    def criar_elementos(self):
        self.fonte = font.Font(family="Tahoma", size=13, weight="normal")
        self.header_frame = ttk.Frame(self, style="Background.TFrame")
        self.header_frame.pack(pady=50)

        self.register_label = ttk.Label(self.header_frame, text="NOVO EVENTO",
                                        font=font.Font(family="Tahoma", size=35, weight="bold"),
                                        background="#141414", foreground="white")
        self.register_label.grid(row=0, column=1, padx=20)

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

        # Frame para dados específicos de Tarefa
        self.frame_tarefa = ttk.Frame(self, style="Background.TFrame")
        self.criar_elementos_tarefa()

        # Frame para dados específicos de Compromisso
        self.frame_compromisso = ttk.Frame(self, style="Background.TFrame")
        self.criar_elementos_compromisso()

        # Frame para dados específicos de Lembrete
        self.frame_lembrete = ttk.Frame(self, style="Background.TFrame")
        self.criar_elementos_lembrete()

        # Exibição inicial dos elementos de Tarefa
        self.atualizar_aparencia_radiobuttons()

    def criar_elementos_tarefa(self):
        ttk.Label(self.frame_tarefa, text="TITULO:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=0, column=1, padx=5, pady=5)
        ttk.Entry(self.frame_tarefa, width=50).grid(row=0, column=2, padx=10, pady=5)

        ttk.Label(self.frame_tarefa, text="DATA:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=0, column=3, padx=5, pady=5)
        
        self.combobox_dia = ttk.Combobox(self.frame_tarefa, values=[], width=5, state='readonly')
        self.combobox_dia.grid(row=0, column=5, padx=2, pady=5)

        self.combobox_mes = ttk.Combobox(self.frame_tarefa, values=self.meses, width=10, state='readonly')
        self.combobox_mes.grid(row=0, column=6, padx=2, pady=5)
        self.combobox_mes.bind("<<ComboboxSelected>>", self.atualizar_dias_validos)
        
        self.combobox_ano = ttk.Combobox(self.frame_tarefa, values=self.anos_validos, width=7, state='readonly')
        self.combobox_ano.grid(row=0, column=7, padx=2, pady=5)
        self.combobox_ano.bind("<<ComboboxSelected>>", self.atualizar_dias_validos)

        ttk.Label(self.frame_tarefa, text="DESCRICAO:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=2, column=1, padx=10, pady=5)
        ttk.Entry(self.frame_tarefa, width=50).grid(row=2, column=2, padx=10, pady=5)

        ttk.Label(self.frame_tarefa, text="PRIORIDADE:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=3, column=1, padx=10, pady=5)
        ttk.Combobox(self.frame_tarefa, values=["MUITO IMPORTANTE", "IMPORTANTE", "MENOS IMPORTANTE"], width=30, state='readonly').grid(row=3, column=2, padx=10, pady=5)

        ttk.Label(self.frame_tarefa, text="ESTADO:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=4, column=1, padx=10, pady=5)
        ttk.Combobox(self.frame_tarefa, values=["NÃO FEITO", "EM PROGRESSO", "FEITO"], width=30, state='readonly').grid(row=4, column=2, padx=10, pady=5)

        self.atualizar_dias_validos()

    def criar_elementos_compromisso(self):
        ttk.Label(self.frame_compromisso, text="TITULO:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=0, column=1, padx=5, pady=5)
        ttk.Entry(self.frame_compromisso, width=50).grid(row=0, column=2, padx=10, pady=5)

        ttk.Label(self.frame_compromisso, text="DESCRICAO:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=1, column=1, padx=10, pady=5)
        ttk.Entry(self.frame_compromisso, width=50).grid(row=1, column=2, padx=10, pady=5)

        ttk.Label(self.frame_compromisso, text="ESTADO:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=2, column=1, padx=10, pady=5)
        ttk.Combobox(self.frame_compromisso, values=["NÃO FEITO", "EM PROGRESSO", "FEITO"], width=30, state='readonly').grid(row=2, column=2, padx=10, pady=5)

        ttk.Label(self.frame_compromisso, text="PRIORIDADE:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=3, column=1, padx=10, pady=5)
        ttk.Combobox(self.frame_compromisso, values=["MUITO IMPORTANTE", "IMPORTANTE", "MENOS IMPORTANTE"], width=30, state='readonly').grid(row=3, column=2, padx=10, pady=5)

        ttk.Label(self.frame_compromisso, text="COR:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=5, column=1, padx=5, pady=5)
        self.combobox_horas = ttk.Combobox(self.frame_compromisso, values=['LARANJA', 'AZUL', 'ROXO', 'ROSA'], width=15, state='readonly')
        self.combobox_horas.grid(row=5, column=2, padx=2, pady=5)

        ttk.Label(self.frame_compromisso, text="HORARIO:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=1, column=3, padx=5, pady=5)
        
        self.combobox_horas = ttk.Combobox(self.frame_compromisso, values=[str(f"{horas:02d}h") for horas in range(0, 24)], width=5, state='readonly')
        self.combobox_horas.grid(row=1, column=4, padx=2, pady=5)

        self.combobox_minutos = ttk.Combobox(self.frame_compromisso, values=[str(f"{minutos:02d} min") for minutos in range(0, 60)], width=10, state='readonly')
        self.combobox_minutos.grid(row=1, column=5, padx=2, pady=5)

        self.combobox_segundos = ttk.Combobox(self.frame_compromisso, values=[str(f"{segundo:02d} seg") for segundo in range(0, 60)], width=7, state='readonly')
        self.combobox_segundos.grid(row=1, column=6, padx=2, pady=5)


        ttk.Label(self.frame_compromisso, text="DATA:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=0, column=3, padx=5, pady=5)
        
        self.combobox_dia = ttk.Combobox(self.frame_compromisso, values=[], width=5, state='readonly')
        self.combobox_dia.grid(row=0, column=4, padx=2, pady=5)

        self.combobox_mes = ttk.Combobox(self.frame_compromisso, values=self.meses, width=10, state='readonly')
        self.combobox_mes.grid(row=0, column=5, padx=2, pady=5)
        self.combobox_mes.bind("<<ComboboxSelected>>", self.atualizar_dias_validos)
        
        self.combobox_ano = ttk.Combobox(self.frame_compromisso, values=self.anos_validos, width=7, state='readonly')
        self.combobox_ano.grid(row=0, column=6, padx=2, pady=5)
        self.combobox_ano.bind("<<ComboboxSelected>>", self.atualizar_dias_validos)

        self.atualizar_dias_validos()

    def criar_elementos_lembrete(self):
        ttk.Label(self.frame_lembrete, text="MENSAGEM:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=0, column=1, padx=5, pady=5)
        ttk.Entry(self.frame_lembrete, width=50).grid(row=0, column=2, padx=10, pady=5)

        ttk.Label(self.frame_lembrete, text="DATA:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=0, column=3, padx=5, pady=5)
        
        self.combobox_dia = ttk.Combobox(self.frame_lembrete, values=[], width=5, state='readonly')
        self.combobox_dia.grid(row=0, column=5, padx=2, pady=5)

        self.combobox_mes = ttk.Combobox(self.frame_lembrete, values=self.meses, width=10, state='readonly')
        self.combobox_mes.grid(row=0, column=6, padx=2, pady=5)
        self.combobox_mes.bind("<<ComboboxSelected>>", self.atualizar_dias_validos)
        
        self.combobox_ano = ttk.Combobox(self.frame_lembrete, values=self.anos_validos, width=7, state='readonly')
        self.combobox_ano.grid(row=0, column=7, padx=2, pady=5)
        self.combobox_ano.bind("<<ComboboxSelected>>", self.atualizar_dias_validos)

        ttk.Label(self.frame_lembrete, text="HORARIO:", font=self.fonte,
                  background="#141414", foreground="white").grid(row=1, column=3, padx=5, pady=5)
        
        self.combobox_horas = ttk.Combobox(self.frame_lembrete, values=[str(f"{horas:02d}h") for horas in range(0, 24)], width=5, state='readonly')
        self.combobox_horas.grid(row=1, column=5, padx=2, pady=5)

        self.combobox_minutos = ttk.Combobox(self.frame_lembrete, values=[str(f"{minutos:02d} min") for minutos in range(0, 60)], width=10, state='readonly')
        self.combobox_minutos.grid(row=1, column=6, padx=2, pady=5)

        self.combobox_segundos = ttk.Combobox(self.frame_lembrete, values=[str(f"{segundo:02d} seg") for segundo in range(0, 60)], width=7, state='readonly')
        self.combobox_segundos.grid(row=1, column=7, padx=2, pady=5)

        self.atualizar_dias_validos()

    def atualizar_tipo_evento(self):
        tipo_selecionado = self.tipo_evento.get()

        if tipo_selecionado == "Tarefa":
            self.frame_tarefa.pack(fill=tk.BOTH, expand=True, padx=50, pady=20)
            self.frame_compromisso.pack_forget()
            self.frame_lembrete.pack_forget()
        elif tipo_selecionado == "Compromisso":
            self.frame_tarefa.pack_forget()
            self.frame_compromisso.pack(fill=tk.BOTH, expand=True, padx=50, pady=20)
            self.frame_lembrete.pack_forget()
        elif tipo_selecionado == "Lembrete":
            self.frame_tarefa.pack_forget()
            self.frame_compromisso.pack_forget()
            self.frame_lembrete.pack(fill=tk.BOTH, expand=True, padx=50, pady=20)
        
        self.atualizar_aparencia_radiobuttons()

    def atualizar_aparencia_radiobuttons(self):
        if self.tipo_evento.get() == "Tarefa":
            self.radiobutton_tarefa.config(background="#333333")
            self.radiobutton_compromisso.config(background="#1f1f1f")
            self.radiobutton_lembrete.config(background="#1f1f1f")
        elif self.tipo_evento.get() == "Compromisso":
            self.radiobutton_tarefa.config(background="#1f1f1f")
            self.radiobutton_compromisso.config(background="#333333")
            self.radiobutton_lembrete.config(background="#1f1f1f")
        elif self.tipo_evento.get() == "Lembrete":
            self.radiobutton_tarefa.config(background="#1f1f1f")
            self.radiobutton_compromisso.config(background="#1f1f1f")
            self.radiobutton_lembrete.config(background="#333333")

    def atualizar_dias_validos(self, event=None):
        mes_selecionado = self.combobox_mes.get()
        ano_selecionado = self.combobox_ano.get()
        
        dia_selecionado = self.combobox_dia.get()

        if mes_selecionado and ano_selecionado:
            mes_selecionado = self.meses.index(mes_selecionado) + 1  # Converter o nome dos meses para índice de 1 a 12
            ano_selecionado = int(ano_selecionado)

            self.dias_validos = [str(day) for day in range(1, calendar.monthrange(ano_selecionado, mes_selecionado)[1] + 1)]

            self.combobox_dia.config(values=self.dias_validos)

            if dia_selecionado not in self.dias_validos:
                if self.dias_validos:
                    self.combobox_dia.set(self.dias_validos[0])