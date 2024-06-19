from src.Implementações.Tarefa.Tarefa import Tarefa
from src.Interfaces.Inter_ListadeTarefa import Inter_listadeTarefa

from typing import Optional, Union, List, Dict
import pandas as pd

class ListaTarefa(Inter_listadeTarefa):
    def __init__(self) -> None:
        self.__colunas = ['Email', 'Título', 'Descrição', 'Data', 'Prioridade', 'Estado', 'Tipo']
        self.__nome_do_arquivo = "Planilha_de_tarefas.xlsx"

    # @brief Carrega a planilha do arquivo Excel das tarefas salvas
    #
    # @return A planilha caso exista, cria uma nova caso nao exista
    def _carregar_planilha(self) -> pd.DataFrame:
        try:
            return pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            return pd.DataFrame(columns=self.__colunas)

    # @brief Adiciona uma tarefa no sistema
    #
    # @param tarefa A tarefa a ser adicionada
    #
    # @param user_email O email do usuario logado
    def adicionarTarefa(self, evento: Tarefa, user_email: str) -> None:
        planilha = self._carregar_planilha()

        nova_tarefa = {
            'Email': user_email,
            'Título': evento.getTitulo(),
            'Descrição': evento.getDescricao(),
            'Data': evento.getData(),
            'Prioridade': evento.getPrioridade(),
            'Estado': evento.getEstado(),
            'Tipo': 'Tarefa'
        }

        nova_tarefa_df = pd.DataFrame([nova_tarefa])

        planilha = pd.concat([planilha, nova_tarefa_df], ignore_index=True)

        planilha = planilha.drop_duplicates()
        planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')
            
    # @brief Remove uma tarefa no sistema
    #
    # @param tarefa A tarefa a ser removida
    #
    # @param user_email O email do usuario logado
    def removerTarefa(self, evento: Tarefa, user_email: str) -> None:    
        planilha = self._carregar_planilha()

        if user_email in planilha['Email'].values:
            planilha = planilha[~((planilha['Email'] == user_email) & (planilha['Título'] == evento.getTitulo()))]
            planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')

    # @brief Busca uma Tarefa pelo seu Título, Data ou Mês
    #
    # @param titulo o Título da Tarefa a ser procurada (opcional)
    # @param data a Data da Tarefa a ser procurada (opcional)
    # @param mes o Mês da Tarefa a ser procurada (opcional)
    #
    # @return A(s) tarefa(s), se existir(em). Caso nao exista(m), retorna None
    def buscarTarefa(self, user_email, titulo: Optional[str] = None, data: Optional[str] = None, mes: Optional[int] = None) -> Optional[Union[Dict, List[Dict]]]:
        planilha = self._carregar_planilha()

        if titulo:
            if titulo in planilha['Título'].values:
                linha = planilha[(planilha['Título'] == titulo) & (planilha['Email'] == user_email)]
                if not linha.empty:
                    return linha.to_dict(orient='records')[0]
            return None

        if data:
            tarefas_data = planilha[(planilha['Data'] == data) & (planilha['Email'] == user_email)]
            if not tarefas_data.empty:
                return tarefas_data.to_dict(orient='records')
            return None

        if mes:
            planilha['Mês'] = pd.to_datetime(planilha['Data'], format='%d/%m/%Y', errors='coerce').dt.month
            tarefas_mes = planilha[(planilha['Mês'] == mes) & (planilha['Email'] == user_email)]
            if not tarefas_mes.empty:
                return tarefas_mes.drop(columns=['Mês']).to_dict(orient='records')
            return None

        return None