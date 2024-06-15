from Interfaces.Inter_Usuario import Inter_Usuario, Inter_ListadeUsuario
import re
import pandas as pd

class Usuario(Inter_Usuario):
    def __init__(self):
        self.__nome = ""
        self.__sobrenome = ""
        self.__senha = ""
        self.__email = ""
    
    def getNome(self) -> str:
        return f"{self.__nome} {self.__sobrenome}"
    
    def getEmail(self) -> str:
        return self.__email
    
    def getSenha(self) -> str:
        return self.__senha

    def setNome(self, novo_nome: str, novo_sobrenome: str) -> str:
        MAX_CARACTERES = 40
        if 0 < len(novo_nome) <= MAX_CARACTERES:
            self.__nome = novo_nome
        else:
            return "O nome deve possuir entre 1 e 40 caracteres."

        if 0 < len(novo_sobrenome) <= MAX_CARACTERES:
            self.__sobrenome = novo_sobrenome
            return "Sucesso"
        else:
            return "O sobrenome deve possuir entre 1 e 40 caracteres."
    
    def setSenha(self, nova_senha: str) -> str:
        if re.match(r"^\d{6}$", nova_senha):
            self.__senha = nova_senha
            return "Sucesso"
        else:
            return "A senha deve conter exatamente 6 números."

    def setEmail(self, novo_email: str) -> str:
        lista_usuarios = ListaUsuario()
        if lista_usuarios.checkUsuario(novo_email):
            return "O email fornecido já está em uso."
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", novo_email):
            return "Email deve estar no formato: usuario@dominio.com"
        
        try:
            usuario, dominio = novo_email.split('@')
        except ValueError:
            return "Email deve estar no formato: usuario@dominio.com"
        
        if not usuario or not dominio:
            return "Email deve estar no formato: usuario@dominio.com"

        dominios_aceitos = ["gmail.com", "yahoo.com", "outlook.com"]
        if dominio not in dominios_aceitos:
            return "Dominio de email invalido."

        self.__email = novo_email
        return "Sucesso"

    def checkSenha(self, senha_informada: str) -> bool:
        if self.__senha == senha_informada:
            return True
        else:
            return False
        
class ListaUsuario(Inter_ListadeUsuario):
    def __init__(self) -> None:
        self.__colunas = ['Usuário', 'E-mail']
        self.__dataframe_usuarios = pd.DataFrame({}, columns=self.__colunas)
        
        self.__dataframe_usuarios.to_excel('Planilha_de_usuarios.xlsx',index=True, engine='openpyxl')

    def adicionarUsuario(self, usuario: Usuario):
        #nova_linha = pd.Series({'Usuário': usuario.getNome(), 'E-mail': usuario.getEmail()}, name=self.__dataframe_usuarios.shape[0])
        self.__dataframe_usuarios[self.__dataframe_usuarios.shape[0], [0]] = usuario.getNome()
        
        self.__dataframe_usuarios.to_excel('Planilha_de_usuarios.xlsx',index=True, engine='openpyxl')

    def removerUsuario(self, usuario: Usuario):
        planilha = pd.read_excel('Planilha_de_usuarios.xlsx')
        
        if usuario.getEmail() in planilha:
            self.__dataframe_usuarios.drop(planilha[usuario.getEmail()])
            self.__dataframe_usuarios.to_excel('Planilha_de_usuarios.xlsx',index=True, engine='openpyxl')

    def checkUsuario(self, email: str, nome: str = None) -> bool:
        try:
            planilha = pd.read_excel('Planilha_de_usuarios.xlsx')
            
        except:
            print("Arquivo não encontrado!")
            return True
            
        if nome:
            return email in planilha and planilha.iloc[email] == nome
        return email in planilha
