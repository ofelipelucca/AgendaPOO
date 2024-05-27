from Interfaces.Inter_Usuario import Inter_Usuario,Inter_ListadeUsuario
import re

class Usuario(Inter_Usuario):
    def __init__(self, nome: str, sobrenome: str, senha: str, email: str):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__senha = senha
        self.__email = email
    
    def getNome(self) -> str:
        return self.__nome, self.__sobrenome
    
    def getEmail(self) -> str:
        return self.__email
    
    def getSenha(self) -> str:
        return self.__senha

    def setNome(self, novo_nome: str, novo_sobrenome: str):
        try:
            MAX_CARACTERES = 40

            if len(novo_nome) > 0 and len(novo_nome) <= MAX_CARACTERES:
                self.__nome = novo_nome
            else:
                raise ValueError("Nome inválido")

            if len(novo_sobrenome) > 0 and len(novo_sobrenome) <= MAX_CARACTERES:
                self.__sobrenome = novo_sobrenome
            else:
                raise ValueError("Sobrenome inválido")
        except Exception as e:
            print("O nome e sobrenome devem possuir entre 1 e 40 caracteres")
            self.handleExcecao(e)

    def setSenha(self, nova_senha: str):
        try:
            if re.match(r"^\d{6}$", nova_senha):
                self.__senha = nova_senha
            else:
                raise ValueError("Senha inválida")
        except Exception as e:
            print("A senha deve conter exatamente 6 números")
            self.handleExcecao(e)

    def setEmail(self, novo_email: str):
        try:
            if ListaUsuario.checkUsuario(novo_email):
                raise ValueError("O email fornecido já está em uso")

            usuario, dominio = novo_email.split('@')

            if not usuario or not dominio:
                raise ValueError("Email incompleto")

            if dominio not in ["gmail.com", "yahoo.com", "outlook.com"]:
                raise ValueError("Domínio do email inválido")

            self.__email = novo_email
        except ValueError as e:
            print("Email deve estar no formato: usuario@dominio.com")
            print("Domínios aceitos:")
            print("    - 'gmail.com'")
            print("    - 'yahoo.com'")
            print("    - 'outlook.com'")
            self.handleExcecao(e)
        except Exception as e:
            self.handleExcecao(e)

    def handleExcecao(self, e):
        print(f"Erro: {e}")

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
