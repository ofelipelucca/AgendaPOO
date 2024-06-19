from src.Implementações.Lembrete import Lembrete
from src.Interfaces.Inter_Lembrete import Inter_ListaLembrete

import pandas as pd
from typing import Optional, Union, List, Dict

class ListaLembrete(Inter_ListaLembrete):
    def __init__(self) -> None:
        self.__colunas = ['Email', 'Data', 'Mensagem', 'Horário']
        self.__nome_do_arquivo = "Planilha_de_lembretes.xlsx"

    # @brief Carrega a planilha do arquivo Excel dos lembretes salvos
    #
    # @return A planilha caso exista, cria uma nova caso nao exista
    def _carregar_planilha(self) -> pd.DataFrame:
        try:
            return pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            return pd.DataFrame(columns=self.__colunas)
    
    # @brief Adiciona um novo lembrete ao banco de dados
    #
    # @param lembrete o lembrete a ser adicionado
    #
    # @param user_email O email do usuário que adicionou o lembrete
    def adicionarLembrete(self, lembrete: Lembrete, user_email: str) -> None:
        planilha = self._carregar_planilha()

        novo_lembrete = {
            'Email': user_email,
            'Data': lembrete.getData(),
            'Mensagem': lembrete.getMensagem(),
            'Horário': lembrete.getHorario()
        }

        novo_lembrete_df = pd.DataFrame([novo_lembrete])

        planilha = pd.concat([planilha, novo_lembrete_df], ignore_index=True)
        planilha = planilha.drop_duplicates()
        planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')
    
    # @brief Remove um lembrete do banco da dados
    #
    # @param lembrete O lembrete a ser removido
    #
    # @param user_email O email do usuário logado
    def removerLembrete(self, lembrete: Lembrete, user_email: str) -> None:
        planilha = self._carregar_planilha()

        if user_email in planilha['Email'].values:
            planilha = planilha[~((planilha['Email'] == user_email) & (planilha['Mensagem'] == lembrete.getMensagem()))]
            planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')
    
    # @brief Busca um Lembrete pela sua Mensagem, Data ou Mês
    #
    # @param mensagem a Mensagem do Lembrete a ser procurado (opcional)
    # @param data a Data do Lembrete a ser procurado (opcional)
    # @param mes o Mês do Lembrete a ser procurado (opcional)
    #
    # @return O(s) lembrete(s), se existir(em). Caso nao exista(m), retorna None
    def buscarLembrete(self, mensagem: Optional[str] = None, data: Optional[str] = None, mes: Optional[int] = None) -> Optional[Union[Dict, List[Dict]]]:
        planilha = self._carregar_planilha()

        if mensagem:
            if mensagem in planilha['Mensagem'].values:
                linha = planilha[planilha['Mensagem'] == mensagem]
                return linha.to_dict(orient='records')[0]
            return None

        if data:
            lembretes_data = planilha[planilha['Data'] == data]
            if not lembretes_data.empty:
                return lembretes_data.to_dict(orient='records')
            return None

        if mes:
            planilha['Mês'] = pd.to_datetime(planilha['Data'], format='%d/%m/%Y', errors='coerce').dt.month
            lembretes_mes = planilha[planilha['Mês'] == mes]
            if not lembretes_mes.empty:
                return lembretes_mes.drop(columns=['Mês']).to_dict(orient='records')
            return None

        return None
    
    # @brief Retorna o número de lembretes na planilha
    #
    # @return O número total de lembretes
    def tamanho(self) -> int:
        planilha = self._carregar_planilha()
        return planilha.shape[0]

    # @brief Obtém todos os lembretes de um usuário específico
    #
    # @param user_email O email do usuário logado
    #
    # @return Uma lista de lembretes do usuário, se existirem. Caso não existam, retorna None
    def obterLembretes(self, user_email: str) -> Optional[List[Dict[str, str]]]:
        planilha = self._carregar_planilha()

        if user_email in planilha['Email'].values:
            linha = planilha[planilha['Email'] == user_email]
            return linha.to_dict(orient='records')

        return None