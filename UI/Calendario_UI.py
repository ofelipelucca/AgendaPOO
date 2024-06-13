##########################################################################################
#
#                       TO DO:
#                          - Sistema e janela de login para o usuário acessar seus eventos *
#                          - Carregar os eventos direto do banco de dados, importando e salvando todos os campos necessários, 
#                            incluindo a cor de cada tipo de evento (Tarefa, Compromisso, Lembrete) *
#                          - Sistema e janela para o usuário adicionar seus próprios eventos
#                          - Organizar e modularizar o código
#           
#                           * depende da implementação do banco de dados
#                          
##########################################################################################

import tkinter as tk
from tkinter import ttk, font
import calendar
import locale
from datetime import datetime

class Calendario(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Agenda")
        self.geometry("900x600")
        self.minsize(900, 600)
        self.resizable(True, True)
        self.configure(bg="#141414")
        self.iconbitmap('assets/favicon.ico')

        style = ttk.Style(self)
        style.configure("Background.TFrame", background="#141414")
        style.configure('Custom.TButton', background="#141414", foreground="black", padding=10)
        style.map('Custom.TButton', background=[('active', '#282828')], foreground=[('active', '#282828')])

        self.data_atual = datetime.now()
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
        self.eventos = {}
        self.criar_elementos()
        self.mostrar_mes(self.data_atual.year, self.data_atual.month)

    def criar_elementos(self):
        self.header_frame = ttk.Frame(self, style="Background.TFrame") 
        self.header_frame.pack(pady=50)

        self.prev_button =  tk.Button(self.header_frame, text="<<", command=self.mes_anterior, background="#1f1f1f", foreground="white", font=font.Font(family="Tahoma", size=12, weight="normal"), width=15, height=2, bd=0, highlightthickness=0)
        self.prev_button.grid(row=0, column=0)

        self.mes_label = ttk.Label(self.header_frame, font=font.Font(family="Tahoma", size=35, weight="bold"), background="#141414", foreground="white")
        self.mes_label.grid(row=0, column=1, padx=20)

        self.next_button = tk.Button(self.header_frame, text=">>", command=self.mes_seguinte, background="#1f1f1f", foreground="white", font=font.Font(family="Tahoma", size=12, weight="normal"), width=15, height=2, bd=0, highlightthickness=0)
        self.next_button.grid(row=0, column=2)

        self.dias_frame = ttk.Frame(self, style="Background.TFrame")  
        self.dias_frame.pack()

        dias_da_semana = ["SEG", "TER", "QUA", "QUI", "SEX", "SÁB", "DOM"]
        for idx, day in enumerate(dias_da_semana):
            ttk.Label(self.dias_frame, font=font.Font(family="Tahoma", size=10), text=day, background="#141414", foreground="white").grid(row=1, column=idx, padx=34.5, pady=5)

        self.dias_grid_frame = ttk.Frame(self, style="Background.TFrame") 
        self.dias_grid_frame.pack()

    def mostrar_mes(self, ano, mes):
        self.mes_label.config(text=f"{calendar.month_name[mes].upper()} {ano}")

        for widget in self.dias_grid_frame.winfo_children():
            widget.destroy()

        primeira_semana, total_dias_do_mes = calendar.monthrange(ano, mes)

        dia = 1
        self.botoes = []
        coluna = 2
        for i in range(primeira_semana):
            ttk.Label(self.dias_grid_frame, text="", background="#141414").grid(row=coluna, column=i, padx=5, pady=5)
        for col in range(primeira_semana, 7):
            button_frame = ttk.Frame(self.dias_grid_frame, style="Background.TFrame")
            button_frame.grid(row=coluna, column=col, padx=5, pady=(0, 5))
            button = tk.Button(button_frame, text=str(dia), command=lambda d=dia: self.click_callback(d, mes, ano), background="#1f1f1f", foreground="white", font=font.Font(family="Tahoma", size=12, weight="normal"), width=10, height=2, bd=0, highlightthickness=0)
            button.pack(side=tk.TOP)
            self.botoes.append(button)
            self.mostrar_eventos(button_frame, dia, mes, ano)
            dia += 1

        while dia <= total_dias_do_mes:
            coluna += 1
            for col in range(7):
                if dia > total_dias_do_mes:
                    break
                button_frame = ttk.Frame(self.dias_grid_frame, style="Background.TFrame")
                button_frame.grid(row=coluna, column=col, padx=5, pady=(0, 5))
                button = tk.Button(button_frame, text=str(dia), command=lambda d=dia: self.click_callback(d, mes, ano), background="#1f1f1f", foreground="white", font=font.Font(family="Tahoma", size=12, weight="normal"), width=10, height=2, bd=0, highlightthickness=0)
                button.pack(side=tk.TOP)
                self.botoes.append(button)
                self.mostrar_eventos(button_frame, dia, mes, ano)
                dia += 1

    def mostrar_eventos(self, button_frame, dia, mes, ano):
        eventos = self.eventos.get(ano, {}).get(mes, {}).get(dia, [])
        if eventos:
            canvas = tk.Canvas(button_frame, width=100, height=15, bg="#1f1f1f", highlightthickness=0)
            canvas.place(x=button_frame.winfo_x() // 2, y=button_frame.winfo_height() - 1)
            qtd_bolinhas = len(eventos)
            if qtd_bolinhas > 3:
                for i, (tipo, nome, cor, descricao) in enumerate(eventos[:2]):
                    canvas.create_oval(5 + i*12, 2, 15 + i*12, 12, fill=cor, outline="black")
                canvas.create_text(3*12 + 44, 7, text=f"+{qtd_bolinhas-2}", fill="white", font=font.Font(size=8, weight="bold"))
            else:
                for i, (tipo, nome, cor, descricao) in enumerate(eventos):
                    canvas.create_oval(5 + i*12, 2, 15 + i*12, 12, fill=cor, outline="black")

    def adicionar_evento(self, ano, mes, dia, tipo, nome, cor, descricao):
        total_dias_do_mes = calendar.monthrange(ano, mes)[1]

        if mes <= 12 and dia <= total_dias_do_mes:
            if ano not in self.eventos:
                self.eventos[ano] = {}
            if mes not in self.eventos[ano]:
                self.eventos[ano][mes] = {}
            if dia not in self.eventos[ano][mes]:
                self.eventos[ano][mes][dia] = []

            print(f"Evento '{nome}' adicionado. {total_dias_do_mes} ({dia}/{mes})")

            self.eventos[ano][mes][dia].append((tipo, nome, cor, descricao))
        self.mostrar_mes(self.data_atual.year, self.data_atual.month)

    def click_callback(self, dia, mes, ano):
        if ano in self.eventos and mes in self.eventos[ano] and dia in self.eventos[ano][mes]:
            eventos_do_dia = self.eventos[ano][mes][dia]
            for evento in eventos_do_dia:
                tipo, nome, cor, descricao = evento
                print(f"{tipo}: {nome}")
                print(f"Descrição: {descricao}\n")
        else:
            print(f"Nenhum evento encontrado para o dia {dia} do mês {mes} do ano {ano}.\n")

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

if __name__ == "__main__":
    app = Calendario()
    # Exemplo de adição de eventos
    app.adicionar_evento(2024, 6, 1, "Compromisso", "João", "#FF6347", "Aniversário do João")
    app.adicionar_evento(2024, 6, 15, "Compromisso", "Reunião", "#FF6347", "Reunião importante")
    app.adicionar_evento(2024, 6, 26, "Lembrete", "Compras", "#32CD32", "Ir ao mercado")
    app.adicionar_evento(2024, 6, 20, "Lembrete", "Conta", "#32CD32", "Pagar contas de luz e agua")
    app.adicionar_evento(2024, 6, 5, "Tarefa", "Relatorio", "#32CD32", "Revisar o relatorio para a reunião")
    app.adicionar_evento(2024, 6, 5, "Compromisso", "Reunião", "#FF6347", "Reunião importante")
    app.adicionar_evento(2024, 6, 5, "Lembrete", "Compras", "#32CD32", "Ir ao mercado")

    app.mainloop()
