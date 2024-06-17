from src.Interfaces.Inter_Usuario import Inter_Usuario
from src.Implementações.Usuario.ListaUsuario import ListaUsuario

import re

class Usuario(Inter_Usuario):
    def __init__(self, nome:str, sobrenome:str, email:str, senha:str) -> None:
        self.setNome(nome, sobrenome)
        self.setEmail(email)
        self.setSenha(senha)
    
    def getNomeCompleto(self) -> str:
        return f"{self.__nome} {self.__sobrenome}"
    
    def getNome(self) -> str:
        return self.__nome
    
    def getSobrenome(self) -> str:
        return self.__sobrenome
    
    def getEmail(self) -> str:
        return self.__email
    
    def getSenha(self) -> str:
        return self.__senha

    def setNome(self, novo_nome: str, novo_sobrenome: str) -> None:
        MIN_CARACTERES = 3
        MAX_CARACTERES = 40
        if not (MIN_CARACTERES <= len(novo_nome) <= MAX_CARACTERES):
            raise ValueError(f"O nome deve possuir entre {MIN_CARACTERES} e {MAX_CARACTERES} caracteres.")

        if not (MIN_CARACTERES <= len(novo_sobrenome) <= MAX_CARACTERES):
            raise ValueError(f"O sobrenome deve possuir entre {MIN_CARACTERES} e {MAX_CARACTERES} caracteres.")

        self.__nome = novo_nome
        self.__sobrenome = novo_sobrenome
    
    def setSenha(self, nova_senha: str) -> None:
        if not re.match(r"^\d{6}$", nova_senha):
            raise ValueError("A senha deve conter exatamente 6 números.")
        
        self.__senha = nova_senha

    def setEmail(self, novo_email: str) -> None:
        lista_usuarios = ListaUsuario()
        if lista_usuarios.checkUsuario(novo_email):
            raise ValueError("O email fornecido já está em uso.")
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", novo_email):
            raise ValueError("Email deve estar no formato: usuario@dominio.com")
        
        try:
            usuario, dominio = novo_email.split('@')
        except ValueError:
            raise ValueError("Email deve estar no formato: usuario@dominio.com")
        
        if not usuario or not dominio:
            raise ValueError("Email deve estar no formato: usuario@dominio.com")

        dominios_aceitos = ["gmail.com", "yahoo.com", "outlook.com"]
        if dominio not in dominios_aceitos:
            raise ValueError("Dominio de email invalido.")
        self.__email = novo_email