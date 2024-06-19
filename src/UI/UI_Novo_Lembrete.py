import tkinter as tk
from tkinter import ttk

class UI_Lembrete(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="#141414")

        self.parent = parent

        ttk.Label(self, text="MENSAGEM:", font=self.parent.fonte,
                  background="#141414", foreground="white").grid(row=1, column=1, padx=5, pady=5)
        ttk.Entry(self, width=50).grid(row=1, column=2, padx=10, pady=5)

        ttk.Label(self, text="HORARIO:", font=self.parent.fonte,
                background="#141414", foreground="white").grid(row=1, column=3, padx=5, pady=5)
        
        self.combobox_horas = ttk.Combobox(self, values=[str(f"{horas:02d}h") for horas in range(0, 24)], width=5, state='readonly')
        self.combobox_horas.grid(row=1, column=4, padx=2, pady=5)

        self.combobox_minutos = ttk.Combobox(self, values=[str(f"{minutos:02d} min") for minutos in range(0, 60)], width=10, state='readonly')
        self.combobox_minutos.grid(row=1, column=5, padx=2, pady=5)

        self.combobox_segundos = ttk.Combobox(self, values=[str(f"{segundo:02d} seg") for segundo in range(0, 60)], width=7, state='readonly')
        self.combobox_segundos.grid(row=1, column=6, padx=2, pady=5)