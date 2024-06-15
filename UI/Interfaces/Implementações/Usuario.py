from Interfaces.Inter_Usuario import Inter_Usuario, Inter_ListadeUsuario
import re
import pandas as pd

class Usuario(Inter_Usuario):
    def __init__(self, nome, sobrenome, email, senha):
        self.setNome(nome, sobrenome)
        self.setEmail(email)
        self.setSenha(senha)
    
    def getNome(self) -> str:
        return f"{self.__nome} {self.__sobrenome}"
    
    def getEmail(self) -> str:
        return self.__email
    
    def getSenha(self) -> str:
        return self.__senha

    def setNome(self, novo_nome: str, novo_sobrenome: str) -> None:
        MAX_CARACTERES = 40
        if not (0 < len(novo_nome) <= MAX_CARACTERES):
            raise ValueError("O nome deve possuir entre 1 e 40 caracteres.")

        if not (0 < len(novo_sobrenome) <= MAX_CARACTERES):
            raise ValueError("O sobrenome deve possuir entre 1 e 40 caracteres.")

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

    def checkSenha(self, senha_informada: str) -> bool:
        return self.__senha == senha_informada

class ListaUsuario(Inter_ListadeUsuario):
    def __init__(self) -> None:
        self.__colunas = ['Usuário', 'E-mail']
        self.__dataframe_usuarios = pd.DataFrame({}, columns=self.__colunas)
        
        self.__dataframe_usuarios.to_excel('Planilha_de_usuarios.xlsx',index=True, engine='openpyxl')

    def adicionarUsuario(self, usuario: Usuario):
        self.__dataframe_usuarios.loc[self.__dataframe_usuarios.shape[0]] = [usuario.getNome(), usuario.getEmail()]
        self.__dataframe_usuarios.to_excel('Planilha_de_usuarios.xlsx',index=True, engine='openpyxl')

    def removerUsuario(self, usuario: Usuario):
        planilha = pd.read_excel('Planilha_de_usuarios.xlsx')
        
        if usuario.getEmail() in planilha['E-mail'].values:
            index = planilha[planilha['E-mail'] == usuario.getEmail()].index
            self.__dataframe_usuarios.drop(index, inplace=True)
            self.__dataframe_usuarios.to_excel('Planilha_de_usuarios.xlsx',index=True, engine='openpyxl')

    def checkUsuario(self, email: str, nome: str = None) -> bool:
        try:
            planilha = pd.read_excel('Planilha_de_usuarios.xlsx')
        except FileNotFoundError:
            print("Arquivo não encontrado!")
            return False
            
        if nome:
            return not planilha[(planilha['E-mail'] == email) & (planilha['Usuário'] == nome)].empty
        return not planilha[planilha['E-mail'] == email].empty
