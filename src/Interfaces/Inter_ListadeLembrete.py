from src.Interfaces.Inter_Lembrete import Inter_Lembrete

from abc import ABC, abstractmethod
import pandas as pd
from typing import Optional, Union, List, Dict

class Inter_ListaLembrete(ABC):
    @abstractmethod
    # @brief Carrega a planilha do arquivo Excel dos lembretes salvos
    #
    # @return A planilha caso exista, cria uma nova caso nao exista
    def _carregar_planilha(self) -> pd.DataFrame:
        pass

    @abstractmethod
    # @brief Adiciona um Lembrete a lista de Lembretes
    #
    # @param lembrete O lembrete a ser adicionado
    #
    # @param user_email O email do usuário logado
    def adicionarLembrete(self, lembrete: Inter_Lembrete, user_email: str) -> None:
        pass

    @abstractmethod
    # @brief Remove um lembrete da lista
    #
    # @param lembrete O lembrete a ser removido
    #
    # @param user_email O email do usuário logado
    def removerLembrete(self, lembrete: Inter_Lembrete, user_email: str) -> None:
        pass

    @abstractmethod
    # @brief Procura pelo lembrete pela mensagem
    #
    # @param mensagem A mensagem do lembrete a ser buscado
    def buscarLembrete(self, user_email: str, mensagem: Optional[str] = None, data: Optional[str] = None, mes: Optional[int] = None) -> Optional[Union[Dict, List[Dict]]]:
        pass

    @abstractmethod
    # @brief Calcula o tamanho do mapa
    #
    # @return Um unsigned com o tamanho
    def tamanho(self) -> int:
        pass

    # @brief Obtém todos os lembretes de um usuário específico
    #
    # @param user_email O email do usuário logado
    #
    # @return Uma lista de lembretes do usuário, se existirem. Caso não existam, retorna None
    def obterLembretes(self, user_email: str) -> Optional[List[Dict[str, str]]]:
        pass

class Inter_ImprimirLembrete(Inter_ListaLembrete):
    @abstractmethod
    # @brief Imprime todos lembretes da lista 
    #
    # @param user_email O email do usuario logado
    def verLembretes(self, user_email: str):
        pass