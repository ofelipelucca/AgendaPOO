from src.Interfaces.Inter_Usuario import Inter_ListadeUsuario
from src.Implementações.Usuario import Usuario

import pandas as pd

class ListaUsuario(Inter_ListadeUsuario):
    def __init__(self) -> None:
        self.__colunas = ['Email', 'Usuário']
        self.__nome_do_arquivo = "Planilha_de_usuarios.xlsx"
        
    def adicionarUsuario(self, usuario: Usuario) -> None:
        try:
            planilha = pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            planilha = pd.DataFrame(columns=self.__colunas)
            
        if (self.checkUsuario(usuario.getEmail(), usuario.getNome())):
            print("O usuário fornecido já está cadastrado")
        else:
            novo_usuario = {self.__colunas[0]: usuario.getEmail(), self.__colunas[1]: usuario.getNome()}
            planilha.loc[planilha.shape[0]] = novo_usuario
            
        planilha = planilha.drop_duplicates()
        planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')

    def removerUsuario(self, usuario: Usuario) -> None:
        try:
            planilha = pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            planilha = pd.DataFrame(columns=self.__colunas)
            
        if usuario.getEmail() in planilha[self.__colunas[0]].values:
            planilha = planilha[planilha[self.__colunas[0]] != usuario.getEmail()]
            planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')
            
            print("Usuário removido com sucesso")
        else:
            print("Usuário não encontrado")

    def checkUsuario(self, email: str, nome: str = None) -> bool:
        try:
            planilha = pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            planilha = pd.DataFrame(columns=self.__colunas)
            
        if (nome == None):
            if email in planilha[self.__colunas[0]].values:
                return True
            else:
                return False
            
        else:
            if nome in planilha[self.__colunas[1]].values:
                if planilha[self.__colunas[0]][planilha[self.__colunas[1]] == nome].values[0] == email:
                    return True
            else:
                return False
