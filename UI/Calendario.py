import tkinter as tk
from tkinter import ttk, font
import calendar
import locale
from datetime import datetime

class Calendario(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Agenda")
        self.geometry("800x500")
        self.minsize(800, 500)
        self.resizable(True, True)
        self.configure(bg="#141414")
        self.iconbitmap('assets/favicon.ico')

        style = ttk.Style(self)
        style.configure("Background.TFrame", background="#141414")  

        self.data_atual = datetime.now()
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
        self.criar_elementos()
        self.mostrar_mes(self.data_atual.year, self.data_atual.month)

    def criar_elementos(self):
        # Header frame de botoes de navegacao e texto de Mes/Ano
        self.header_frame = ttk.Frame(self, style="Background.TFrame") 
        self.header_frame.pack(pady=50)

        # Botao de mes anterior
        self.prev_button = ttk.Button(self.header_frame, text="<<", command=self.mes_anterior)
        self.prev_button.grid(row=0, column=0)
        self.prev_button.configure(style='Custom.TButton')

        # Texto de Mes/Ano
        self.mes_label = ttk.Label(self.header_frame, font=font.Font(family="Tahoma", size=16, weight="bold"), background="#141414", foreground="white")
        self.mes_label.grid(row=0, column=1, padx=20)

        # Botao de mes seguinte
        self.next_button = ttk.Button(self.header_frame, text=">>", command=self.mes_seguinte)
        self.next_button.grid(row=0, column=2)
        self.next_button.configure(style='Custom.TButton')

        # Texto de dias da semana
        self.dias_frame = ttk.Frame(self, style="Background.TFrame")  
        self.dias_frame.pack()

        dias_da_semana = ["SEG", "TER", "QUA", "QUI", "SEX", "SÁB", "DOM"]
        for idx, day in enumerate(dias_da_semana):
            ttk.Label(self.dias_frame, font=font.Font(family="Tahoma", size=10), text=day, background="#141414", foreground="white").grid(row=1, column=idx, padx=30, pady=30)

        # Frame for days grid
        self.dias_grid_frame = ttk.Frame(self, style="Background.TFrame") 
        self.dias_grid_frame.pack()

    def mostrar_mes(self, ano, mes):
        # Update the month/year label
        self.mes_label.config(text=f"{calendar.month_name[mes].upper()} {ano}")

        # Clear the current days grid
        for widget in self.dias_grid_frame.winfo_children():
            widget.destroy()

        # Get the first weekday of the month and the number of days in the month
        primeira_semana, total_dias_do_mes = calendar.monthrange(ano, mes)

        # Fill the days grid with buttons

        s = ttk.Style()
        s.configure('Custom.TButton', background="#141414", foreground="black")  

        dia = 1
        coluna = 2
        for i in range(primeira_semana):
            ttk.Label(self.dias_grid_frame, text="", background="#141414").grid(row=coluna, column=i, padx=5, pady=5) 
        for col in range(primeira_semana, 7):
            button = ttk.Button(self.dias_grid_frame, text=str(dia), command=lambda d=dia: self.click_callback(d))
            button.grid(row=coluna, column=col, padx=5, pady=5)
            button.configure(style='Custom.TButton')
            dia += 1

        while dia <= total_dias_do_mes:
            coluna += 1
            for col in range(7):
                if dia > total_dias_do_mes:
                    break
                button = ttk.Button(self.dias_grid_frame, text=str(dia), command=lambda d=dia: self.click_callback(d))
                button.grid(row=coluna, column=col, padx=5, pady=5)
                button.configure(style='Custom.TButton')
                dia += 1

    def click_callback(self, dia):
        # O que fazer quando o dia é clicado
        print(f"Dia {dia} selecionado.")

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
    app.mainloop()
