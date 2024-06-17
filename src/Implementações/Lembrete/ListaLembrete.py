from src.Implementações.Lembrete import Lembrete
from src.Interfaces.Inter_Lembrete import Inter_ListaLembrete

import pandas as pd
from typing import Optional, List, Dict

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
    
    # @brief Busca um lembrete pelo seu conteúdo de mensagem
    #
    # @param mensagem A mensagem do lembrete a ser procurada
    #
    # @return O lembrete, se existir. Caso não exista, retorna None
    def buscarLembrete(self, mensagem: str) -> Optional[Dict[str, str]]:
        planilha = self._carregar_planilha()

        if mensagem in planilha['Mensagem'].values:
            linha = planilha[planilha['Mensagem'] == mensagem]
            return linha.to_dict(orient='records')[0]  

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