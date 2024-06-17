from src.Implementações.Tarefa.Tarefa import Tarefa
from src.Interfaces.Inter_ListadeTarefa import Inter_listadeTarefa

import pandas as pd

class ListaTarefa(Inter_listadeTarefa):

    def __init__(self) -> None:
        self.__colunas = ['Email', 'Título', 'Descrição', 'Data', 'Prioridade', 'Estado', 'Cor', 'Local', 'Horário']
        self.__nome_do_arquivo = "Planilha_de_tarefas.xlsx"

    # @brief Adiciona uma tarefa no sistema
    #
    # @param tarefa A tarefa a ser adicionada
    #
    # @param user_email O email do usuario logado
    def adicionarTarefa(self, tarefa: Tarefa, user_email: str) -> None:
        try:
            planilha = pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            planilha = pd.DataFrame(columns=self.__colunas)
        
        tipo_de_tarefa = "compromisso"
        try:
            tarefa.getCor()
        except:
            tipo_de_tarefa = "tarefa"
            
        nova_tarefa = {self.__colunas[0]: user_email, self.__colunas[1]: tarefa.getTitulo(), 
                        self.__colunas[2]: tarefa.getDescricao(), self.__colunas[3]: tarefa.getData(), 
                        self.__colunas[4]: tarefa.getPrioridade(), self.__colunas[5]: tarefa.getEstado(),
                        self.__colunas[6]: '', self.__colunas[7]: '', self.__colunas[8]: ''}
        
        if (tipo_de_tarefa == "compromisso"):
            nova_tarefa[self.__colunas[6]] = tarefa.getCor()
            nova_tarefa[self.__colunas[7]] = tarefa.getLocal()
            nova_tarefa[self.__colunas[8]] = tarefa.getHorario()
            
        planilha.loc[planilha.shape[0]] = nova_tarefa
        
        planilha = planilha.drop_duplicates()
        planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')
            

    # @brief Remove uma tarefa no sistema
    #
    # @param tarefa A tarefa a ser removida
    #
    # @param user_email O email do usuario logado
    def removerTarefa(self, tarefa: Tarefa, user_email: str) -> None:
        try:
            planilha = pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            planilha = pd.DataFrame(columns=self.__colunas)
            
            
        if user_email in planilha[self.__colunas[0]].values:
            planilha = planilha.drop(planilha.query('Email == @user_email and Título == @tarefa.getTitulo()').index)
            planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')
            

    # @brief Busca uma Tarefa pelo seu Título
    #
    # @param titulo o Título da Tarefa a ser procurada
    #
    # @return A tarefa, se existir. Caso nao exista, retorna None
    def buscarTarefa(self, titulo: str) -> Tarefa:
        try:
            planilha = pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            planilha = pd.DataFrame(columns=self.__colunas)
            
        if titulo in planilha[self.__colunas[1]].values:
            linha = planilha.query('Título == @titulo')

            return linha.to_dict(orient='list')
        return None
