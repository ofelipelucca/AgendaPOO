from src.Implementações.Compromisso.Compromisso import Compromisso
from src.Interfaces.Inter_ListadeCompromisso import Inter_listadeCompromisso

from typing import Optional, Union, List, Dict
import pandas as pd

class ListaCompromisso(Inter_listadeCompromisso):
    def __init__(self) -> None:
        self.__colunas = ['Email', 'Título', 'Descrição', 'Data', 'Prioridade', 'Estado', 'Cor', 'Local', 'Horário', 'Tipo']
        self.__nome_do_arquivo = "Planilha_de_compromissos.xlsx"

    # @brief Carrega a planilha do arquivo Excel dos compromissos salvos
    #
    # @return A planilha caso exista, cria uma nova caso nao exista
    def _carregar_planilha(self) -> pd.DataFrame:
        try:
            return pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            return pd.DataFrame(columns=self.__colunas)

    # @brief Adiciona um Compromisso no sistema
    #
    # @param Compromisso O Compromisso a ser adicionada
    #
    # @param user_email O email do usuario logado
    def adicionarCompromisso(self, evento: Compromisso, user_email: str) -> None:
        planilha = self._carregar_planilha()

        novo_compromisso = {
            'Email': user_email,
            'Título': evento.getTitulo(),
            'Descrição': evento.getDescricao(),
            'Data': evento.getData(),
            'Prioridade': evento.getPrioridade(),
            'Estado': evento.getEstado(),
            'Cor': evento.getCor(),
            'Local': evento.getLocal(),
            'Horário': evento.getHorario(),
            'Tipo': 'Compromisso'
        }

        novo_compromisso_df = pd.DataFrame([novo_compromisso])

        planilha = pd.concat([planilha, novo_compromisso_df], ignore_index=True)

        planilha = planilha.drop_duplicates()
        planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')
            
    # @brief Remove um Compromisso no sistema
    #
    # @param Compromisso O Compromisso a ser removido
    #
    # @param user_email O email do usuario logado
    def removerCompromisso(self, evento: Compromisso, user_email: str) -> None:    
        planilha = self._carregar_planilha()

        if user_email in planilha['Email'].values:
            planilha = planilha[~((planilha['Email'] == user_email) & (planilha['Título'] == evento.getTitulo()))]
            planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')

    # @brief Busca um Compromisso pelo seu Título
    #
    # @param titulo o Título do Compromisso a ser procurado (opcional)
    # @param data a Data do Compromisso a ser procurado (opcional)
    # @param mes o Mês do Compromisso a ser procurado (opcional)
    #
    # @return O Compromisso, se existir. Caso nao exista, retorna None
    def buscarCompromisso(self, user_email, titulo: Optional[str] = None, data: Optional[str] = None, mes: Optional[int] = None) -> Optional[Union[Dict, List[Dict]]]:
        planilha = self._carregar_planilha()

        if titulo:
            if titulo in planilha['Título'].values:
                linha = planilha[(planilha['Título'] == titulo) & (planilha['Email'] == user_email)]
                if not linha.empty:
                    return linha.to_dict(orient='records')[0]
            return None

        if data:
            compromissos_data = planilha[(planilha['Data'] == data) & (planilha['Email'] == user_email)]
            if not compromissos_data.empty:
                return compromissos_data.to_dict(orient='records')
            return None

        if mes:
            planilha['Mês'] = pd.to_datetime(planilha['Data'], format='%d/%m/%Y', errors='coerce').dt.month
            compromissos_mes = planilha[(planilha['Mês'] == mes) & (planilha['Email'] == user_email)]
            if not compromissos_mes.empty:
                return compromissos_mes.drop(columns=['Mês']).to_dict(orient='records')
            return None

        return None