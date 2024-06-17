from src.Implementações.Usuario.Usuario import Usuario
from src.Implementações.Usuario.ListaUsuario import ListaUsuario

import tkinter as tk
from tkinter import ttk, font

class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#141414")
        self.controller = controller

        self.criar_elementos()

    def criar_elementos(self):
        self.header_frame = ttk.Frame(self, style="Background.TFrame")
        self.header_frame.pack(pady=50)

        self.register_label = ttk.Label(self.header_frame, text="REGISTRE SUA CONTA", 
                                     font=font.Font(family="Tahoma", size=35, weight="bold"), 
                                     background="#141414", foreground="white")
        self.register_label.grid(row=0, column=1, padx=20)

        self.error_frame = ttk.Frame(self, style="Background.TFrame")
        self.error_frame.pack(pady=5)

        self.error_label = ttk.Label(self.error_frame, text="", 
                                     font=font.Font(family="Tahoma", size=10, weight="bold"), 
                                     background="#141414", foreground="white")
        self.error_label.grid(row=0, column=1, padx=20)

        self.input_frame = ttk.Frame(self, style="Background.TFrame")
        self.input_frame.pack(pady=5)

        self.nome_label = ttk.Label(self.input_frame, text="NOME:", 
                                    font=font.Font(family="Tahoma", size=12), 
                                    background="#141414", foreground="white")
        self.nome_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.nome_entry = ttk.Entry(self.input_frame, font=font.Font(family="Tahoma", size=12), width=30)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)

        self.sobrenome_label = ttk.Label(self.input_frame, text="SOBRENOME:", 
                                    font=font.Font(family="Tahoma", size=12), 
                                    background="#141414", foreground="white")
        self.sobrenome_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.sobrenome_entry = ttk.Entry(self.input_frame, font=font.Font(family="Tahoma", size=12), width=30)
        self.sobrenome_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_label = ttk.Label(self.input_frame, text="EMAIL:", 
                                     font=font.Font(family="Tahoma", size=12), 
                                     background="#141414", foreground="white")
        self.email_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.email_entry = ttk.Entry(self.input_frame, font=font.Font(family="Tahoma", size=12), width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.senha_label = ttk.Label(self.input_frame, text="SENHA:", 
                                     font=font.Font(family="Tahoma", size=12), 
                                     background="#141414", foreground="white")
        self.senha_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.senha_entry = ttk.Entry(self.input_frame, font=font.Font(family="Tahoma", size=12), width=30, show="*")
        self.senha_entry.grid(row=3, column=1, padx=10, pady=10)

        self.button_frame = ttk.Frame(self, style="Background.TFrame")
        self.button_frame.pack(pady=20)

        self.register_button = tk.Button(self.button_frame, text="REGISTRAR-SE", command=lambda: self.check_dados(),
                                    background="#1f1f1f", foreground="white", font=font.Font(family="Tahoma", size=12, weight="normal"), 
                                    width=25, height=2, bd=0, highlightthickness=0)
        self.register_button.pack(side=tk.TOP)
        
        self.button_frame = ttk.Frame(self, style="Background.TFrame")
        self.button_frame.pack(pady=5)

        self.login_button = tk.Button(self.button_frame, text="JA ESTOU REGISTRADO", command=lambda: self.controller.mostrar_tela("Login"),
                                    background="#1f1f1f", foreground="white", font=font.Font(family="Tahoma", size=12, weight="normal"), 
                                    width=25, height=2, bd=0, highlightthickness=0)
        self.login_button.pack(side=tk.TOP)
        self.login_button.grid(row=0, column=1, pady=5)

    def check_dados(self):
        nome = self.nome_entry.get()
        sobrenome = self.sobrenome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        try:
            self.controller.usuario = Usuario(nome, sobrenome, email, senha)
            lista_usuarios = ListaUsuario()

            lista_usuarios.adicionarUsuario(self.controller.usuario)

            self.error_label.configure(text="")
            self.controller.mostrar_tela("Login") # Caso registrado com sucesso (objeto Usuario pôde ser criado), ir para a tela de login
        except ValueError as e:
            self.error_label.configure(text=str(e)) # Caso ocorra, exibindo o erro na error_label