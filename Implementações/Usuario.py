from Interfaces.Inter_Usuario import Inter_Usuario, Inter_ListadeUsuario
import re

class Usuario(Inter_Usuario):
    def __init__(self, nome: str, sobrenome: str, senha: str, email: str):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__senha = senha
        self.__email = email
    
    def getNome(self) -> str:
        return f"{self.__nome} {self.__sobrenome}"
    
    def getEmail(self) -> str:
        return self.__email
    
    def getSenha(self) -> str:
        return self.__senha

    def setNome(self, novo_nome: str, novo_sobrenome: str):
        MAX_CARACTERES = 40
        if 0 < len(novo_nome) <= MAX_CARACTERES:
            self.__nome = novo_nome
        else:
            print("O nome deve possuir entre 1 e 40 caracteres")
            return

        if 0 < len(novo_sobrenome) <= MAX_CARACTERES:
            self.__sobrenome = novo_sobrenome
        else:
            print("O sobrenome deve possuir entre 1 e 40 caracteres")
    
    def setSenha(self, nova_senha: str):
        if re.match(r"^\d{6}$", nova_senha):
            self.__senha = nova_senha
        else:
            print("A senha deve conter exatamente 6 números")

    def setEmail(self, novo_email: str):
        # Verifica se o email já está em uso
        if ListaUsuario.checkUsuario(novo_email):
            print("O email fornecido já está em uso")
            return
        
        # Valida o formato básico do email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", novo_email):
            print("Email deve estar no formato: usuario@dominio.com")
            return
        
        try:
            usuario, dominio = novo_email.split('@')
        except ValueError:
            print("Email deve estar no formato: usuario@dominio.com")
            return
        
        # Verifica se o usuário e domínio não estão vazios
        if not usuario or not dominio:
            print("Email deve estar no formato: usuario@dominio.com")
            return

        # Valida o domínio do email
        dominios_aceitos = ["gmail.com", "yahoo.com", "outlook.com"]
        if dominio not in dominios_aceitos:
            print("Domínios aceitos:")
            for d in dominios_aceitos:
                print(f"    - '{d}'")
            return

        # Se todas as validações passarem, atualiza o email
        self.__email = novo_email
        print("Email atualizado com sucesso")


class ListaUsuario(Inter_ListadeUsuario):
    _listadeusuario = {}

    def adicionarUsuario(cls, usuario: Usuario):
        cls._listadeusuario[usuario.getEmail()] = usuario

    def removerUsuario(cls, usuario: Usuario):
        if usuario.getEmail() in cls._listadeusuario:
            del cls._listadeusuario[usuario.getEmail()]

    def checkUsuario(cls, email: str, nome: str = None) -> bool:
        if nome:
            return email in cls._listadeusuario and cls._listadeusuario[email].getNome() == nome
        return email in cls._listadeusuario
