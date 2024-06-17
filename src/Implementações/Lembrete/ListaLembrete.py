from src.Interfaces.Inter_Lembrete import Inter_Lembrete, Inter_ListaLembrete

import pandas as pd

class ListaLembrete(Inter_ListaLembrete):
    def __init__(self) -> None:
        self.__colunas = ['Email', 'Data', 'Mensagem', 'Horário']
        self.__nome_do_arquivo = "Planilha_de_lembretes.xlsx"
    
    def adicionarLembrete(self, Lembrete: Inter_Lembrete, user_email: str) -> None:
        try:
            planilha = pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            planilha = pd.DataFrame(columns=self.__colunas)
            
        novo_lembrete = {self.__colunas[0]: user_email, self.__colunas[1]: Lembrete.getData(), 
                         self.__colunas[2]: Lembrete.getMensagem(), self.__colunas[3]: Lembrete.getHorario()}
            
        planilha.loc[planilha.shape[0]] = novo_lembrete
        
        planilha = planilha.drop_duplicates()
        planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')
    
    def removerLembrete(self, Lembrete: Inter_Lembrete, user_email: str) -> None:
        try:
            planilha = pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            planilha = pd.DataFrame(columns=self.__colunas)
            
        if user_email in planilha[self.__colunas[0]].values:
            planilha = planilha.drop(planilha.query('Email == @user_email and Mensagem == @Lembrete.getMensagem()').index)
            planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')
    
    def buscarLembrete(self, mensagem: str) -> list:
        try:
            planilha = pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            planilha = pd.DataFrame(columns=self.__colunas)
            
        if mensagem in planilha[self.__colunas[3]].values:
            linha = planilha.query('Mensagem == @mensagem')

            return linha.to_dict(orient='list')
        return None

    def tamanho(self) -> int:
        try:
            planilha = pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            planilha = pd.DataFrame(columns=self.__colunas)
            
        return planilha.shape[0]

    def obterLembretes(self, user_email: str) -> Inter_Lembrete:
        try:
            planilha = pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            planilha = pd.DataFrame(columns=self.__colunas)
            
        if user_email in planilha[self.__colunas[1]].values:
            linha = planilha.query('Email == @user_email')
            
            return linha.to_dict(orient='list')
        return None
    