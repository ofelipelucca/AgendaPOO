from src.Implementações.Usuario.Usuario import Usuario
from src.Implementações.Usuario.ListaUsuario import ListaUsuario

import tkinter as tk
from tkinter import ttk, font

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#141414")
        self.controller = controller

        self.criar_elementos()

    def criar_elementos(self):
        self.header_frame = ttk.Frame(self, style="Background.TFrame")
        self.header_frame.pack(pady=50)

        self.login_label = ttk.Label(self.header_frame, text="ENTRE NA SUA CONTA", 
                                     font=font.Font(family="Tahoma", size=35, weight="bold"), 
                                     background="#141414", foreground="white")
        self.login_label.grid(row=0, column=1, padx=20)

        self.error_frame = ttk.Frame(self, style="Background.TFrame")
        self.error_frame.pack(pady=5)

        self.error_label = ttk.Label(self.error_frame, text="", 
                                     font=font.Font(family="Tahoma", size=10, weight="bold"), 
                                     background="#141414", foreground="white")
        self.error_label.grid(row=0, column=1, padx=20)

        self.input_frame = ttk.Frame(self, style="Background.TFrame")
        self.input_frame.pack(pady=5)

        self.email_label = ttk.Label(self.input_frame, text="EMAIL:", 
                                     font=font.Font(family="Tahoma", size=12), 
                                     background="#141414", foreground="white")
        self.email_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.email_entry = ttk.Entry(self.input_frame, font=font.Font(family="Tahoma", size=12), width=30)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        self.senha_label = ttk.Label(self.input_frame, text="SENHA:", 
                                     font=font.Font(family="Tahoma", size=12), 
                                     background="#141414", foreground="white")
        self.senha_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.senha_entry = ttk.Entry(self.input_frame, font=font.Font(family="Tahoma", size=12), width=30, show="*")
        self.senha_entry.grid(row=2, column=1, padx=10, pady=10)

        self.button_frame = ttk.Frame(self, style="Background.TFrame")
        self.button_frame.pack(pady=20)
                               
        self.login_button = tk.Button(self.button_frame, text="FAZER LOGIN", command=lambda: self.check_dados(),
                                  background="#1f1f1f", foreground="white", font=font.Font(family="Tahoma", size=12, weight="normal"), 
                                  width=25, height=2, bd=0, highlightthickness=0)
        self.login_button.pack(side=tk.TOP)

        self.register_button = tk.Button(self.button_frame, text="NAO POSSUO UMA CONTA", command=lambda: self.controller.mostrar_tela("Register"),
                                    background="#1f1f1f", foreground="white", font=font.Font(family="Tahoma", size=12, weight="normal"), 
                                    width=25, height=2, bd=0, highlightthickness=0)
        self.register_button.pack(side=tk.TOP, pady=30)

    def check_dados(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        lista_usuarios = ListaUsuario()

        try:
            if lista_usuarios.checkLogin(email, senha):
                dados_do_usuario = lista_usuarios.obterUsuario(email)
                
                self.controller.usuario = dados_do_usuario

                self.error_label.configure(text="")
                self.controller.mostrar_tela("Calendario") # Caso logado com sucesso, ir para a tela de login
            else:
                self.error_label.configure(text="Email ou Senha incorretos.") # Exibindo erro de login
        except ValueError as e:
            self.error_label.configure(text=str(e))