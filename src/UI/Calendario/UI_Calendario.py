from src.Implementações.Tarefa.ListaTarefa import ListaTarefa
from src.Implementações.Compromisso.ListaCompromisso import ListaCompromisso
from src.Implementações.Lembrete.ListaLembrete import ListaLembrete

import tkinter as tk
from tkinter import ttk, font
import calendar
import locale
from datetime import datetime
import pandas as pd

class Calendario(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#141414")
        self.controller = controller

        style = ttk.Style(self)
        style.configure("Background.TFrame", background="#141414")
        style.configure('Custom.TButton', background="#141414", 
                        foreground="black", padding=10)
        style.map('Custom.TButton', background=[('active', '#282828')], 
                  foreground=[('active', '#282828')])

        self.data_atual = datetime.now()
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
        self.eventos = {}
        self.criar_elementos()

        self.lista_de_tarefas = ListaTarefa()
        self.lista_de_compromissos = ListaCompromisso()
        self.lista_de_lembretes = ListaLembrete()

    def criar_elementos(self):
        self.header_frame = ttk.Frame(self, style="Background.TFrame") 
        self.header_frame.pack(pady=50)

        self.prev_button =  tk.Button(self.header_frame, text="<<", command=self.mes_anterior, 
                                      background="#1f1f1f", foreground="white", 
                                      font=font.Font(family="Tahoma", size=12, weight="normal"), 
                                      width=15, height=2, bd=0, highlightthickness=0)
        self.prev_button.grid(row=0, column=0)

        self.mes_label = ttk.Label(self.header_frame, font=font.Font(family="Tahoma", size=35, weight="bold"), 
                                   background="#141414", foreground="white")
        self.mes_label.grid(row=0, column=1, padx=20)

        self.next_button = tk.Button(self.header_frame, text=">>", command=self.mes_seguinte, 
                                     background="#1f1f1f", foreground="white", 
                                     font=font.Font(family="Tahoma", size=12, weight="normal"), 
                                     width=15, height=2, bd=0, highlightthickness=0)
        self.next_button.grid(row=0, column=2)

        self.dias_frame = ttk.Frame(self, style="Background.TFrame")  
        self.dias_frame.pack()

        dias_da_semana = ["SEG", "TER", "QUA", "QUI", "SEX", "SÁB", "DOM"]
        for idx, day in enumerate(dias_da_semana):
            ttk.Label(self.dias_frame, font=font.Font(family="Tahoma", size=10), text=day, 
                      background="#141414", foreground="white").grid(row=1, column=idx, padx=38.5, pady=7)

        self.dias_grid_frame = ttk.Frame(self, style="Background.TFrame") 
        self.dias_grid_frame.pack()
    
    def get_eventos(self, mes):
        try:
            email_do_usuario = self.controller.usuario['Email']
        except:
            return
        tarefas = self.lista_de_tarefas.buscarTarefa(email_do_usuario, mes=mes)
        compromissos = self.lista_de_compromissos.buscarCompromisso(email_do_usuario, mes=mes)
        lembretes = self.lista_de_lembretes.buscarLembrete(email_do_usuario, mes=mes)
        
        tarefas = tarefas if tarefas is not None else []
        compromissos = compromissos if compromissos is not None else []
        lembretes = lembretes if lembretes is not None else []

        self.eventos = tarefas + compromissos + lembretes


    def mostrar_mes(self, ano, mes):
        self.get_eventos(mes)

        # O Ç não existe na fonte usada
        mes_nome = "MARCO" if mes == 3 else calendar.month_name[mes].upper()
        
        self.mes_label.config(text=f"{mes_nome} {ano}")

        # Removendo os elementos existentes ao trocar de mes a ser exibido
        for widget in self.dias_grid_frame.winfo_children():
            widget.destroy()

        primeira_semana, total_dias_do_mes = calendar.monthrange(ano, mes)

        dia = 1
        self.botoes = []
        coluna = 2

        # Preenchendo os campos vazios com uma string vazia para ficar alinhado aos nomes dos dias da semana
        for i in range(primeira_semana):
            ttk.Label(self.dias_grid_frame, text="", background="#141414").grid(row=coluna, column=i, padx=5, pady=5)
        for col in range(primeira_semana, 7):
            button_frame = ttk.Frame(self.dias_grid_frame, style="Background.TFrame")
            button_frame.grid(row=coluna, column=col, padx=5, pady=(0, 5))
            button = tk.Button(button_frame, text=str(dia), command=lambda d=dia: self.click_callback(d, mes, ano), 
                               background="#1f1f1f", foreground="white", font=font.Font(family="Tahoma", size=12, weight="normal"),
                               width=10, height=3, bd=0, highlightthickness=0)
            button.pack(side=tk.TOP)
            self.botoes.append(button)
            self.mostrar_eventos(button_frame, dia, mes, ano)
            dia += 1

        # Criando botões para o resto dos dias do mes
        while dia <= total_dias_do_mes:
            coluna += 1
            for col in range(7):
                if dia > total_dias_do_mes:
                    break
                button_frame = ttk.Frame(self.dias_grid_frame, style="Background.TFrame")
                button_frame.grid(row=coluna, column=col, padx=5, pady=(0, 5))
                button = tk.Button(button_frame, text=str(dia), command=lambda d=dia: self.click_callback(d, mes, ano), 
                                   background="#1f1f1f", foreground="white", font=font.Font(family="Tahoma", size=12, weight="normal"), 
                                   width=10, height=3, bd=0, highlightthickness=0)
                button.pack(side=tk.TOP)
                self.botoes.append(button)
                self.mostrar_eventos(button_frame, dia, mes, ano)
                dia += 1

    def mostrar_eventos(self, button_frame, dia, mes, ano):
        data = f"{dia:02d}/{mes:02d}/{ano}"  # Formatar a data para DD-MM-YYYY

        canvas = tk.Canvas(button_frame, width=100, height=15, bg="#282828", highlightthickness=0)
        canvas.place(x=button_frame.winfo_x() // 2, y=button_frame.winfo_height() - 1)

        eventos_do_dia = self.get_eventos_do_dia(dia, mes, ano)

        # Criando uma bolinha para cada evento no dia com sua determinada cor
        if eventos_do_dia:
            qtd_bolinhas = len(eventos_do_dia)
            if qtd_bolinhas > 3:
                # Desenhar bolinhas para os dois primeiros eventos
                for indice, evento in enumerate(eventos_do_dia[:2]):
                    if str(evento['Data']) != data:
                        continue
                    cor = self.obter_cor_evento(evento)
                    self.desenhar_bolinha(indice, canvas, cor)
                
                # Adicionar texto indicando eventos adicionais
                canvas.create_text(3*12 + 44, 7, text=f"+{qtd_bolinhas-2}", 
                                   fill="white", font=font.Font(size=8, weight="bold"))
            else:
                for indice, evento in enumerate(eventos_do_dia):
                    if str(evento['Data']) != data:
                        continue
                    cor = self.obter_cor_evento(evento)
                    self.desenhar_bolinha(indice, canvas, cor)
    
    def obter_cor_evento(self, evento):
        tipo_do_evento = evento['Tipo']
        if tipo_do_evento == 'Tarefa':
            return '#FFB61E'
        if tipo_do_evento == 'Compromisso':
            return evento['Cor']
        return '#32a8a4'
    
    def desenhar_bolinha(self, i, canvas, cor):
        canvas.create_oval(5 + i*12, 2, 15 + i*12, 12, fill=cor, outline="black")
    
    def get_eventos_do_dia(self, dia, mes, ano):
        data = f"{dia:02d}/{mes:02d}/{ano}"

        eventos_do_dia = []

        if self.eventos:
            for evento in self.eventos:
                if evento['Data'] == data:
                    eventos_do_dia.append(evento)

        return eventos_do_dia

    def click_callback(self, dia, mes, ano):
        eventos_do_dia = self.get_eventos_do_dia(dia, mes, ano)
        self.controller.passar_dados("eventos_do_dia", eventos_do_dia)
        self.controller.passar_dados("data", {"dia": dia, "mes": mes, "ano": ano})
        self.controller.mostrar_tela("Eventos")

    def mes_anterior(self):
        if self.data_atual.month == 1:
            self.data_atual = self.data_atual.replace(year=self.data_atual.year - 1, month=12)
        else:
            self.data_atual = self.data_atual.replace(month=self.data_atual.month - 1)
        self.mostrar_mes(self.data_atual.year, self.data_atual.month)

    def mes_seguinte(self):
        if self.data_atual.month == 12:
            self.data_atual = self.data_atual.replace(year=self.data_atual.year + 1, month=1)
        else:
            self.data_atual = self.data_atual.replace(month=self.data_atual.month + 1)
        self.mostrar_mes(self.data_atual.year, self.data_atual.month)

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)

        self.mostrar_mes(self.data_atual.year, self.data_atual.month)