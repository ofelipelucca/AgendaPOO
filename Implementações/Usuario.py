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
        lista_usuarios = ListaUsuario()
        if lista_usuarios.checkUsuario(novo_email):
            print("O email fornecido já está em uso")
            return
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", novo_email):
            print("Email deve estar no formato: usuario@dominio.com")
            return
        
        try:
            usuario, dominio = novo_email.split('@')
        except ValueError:
            print("Email deve estar no formato: usuario@dominio.com")
            return
        
        if not usuario or not dominio:
            print("Email deve estar no formato: usuario@dominio.com")
            return

        dominios_aceitos = ["gmail.com", "yahoo.com", "outlook.com"]
        if dominio not in dominios_aceitos:
            print("Domínios aceitos:")
            for d in dominios_aceitos:
                print(f"    - '{d}'")
            return

        self.__email = novo_email
        print("Email atualizado com sucesso")

    def checkSenha(self, senha_informada: str) -> bool:
        if self.__senha == senha_informada:
            print("Senha correta")
            return True
        else:
            print("Senha incorreta")
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
