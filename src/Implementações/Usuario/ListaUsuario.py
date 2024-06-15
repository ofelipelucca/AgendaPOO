from src.Interfaces.Inter_Usuario import Inter_ListadeUsuario
from src.Implementações.Usuario import Usuario

import pandas as pd

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
