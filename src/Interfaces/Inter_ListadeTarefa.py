from src.Implementações.Tarefa import Tarefa

from abc import ABC, abstractmethod
import pandas as pd
from typing import Optional, Union, List, Dict

class Inter_listadeTarefa(ABC):
    @abstractmethod
    # @brief Carrega a planilha do arquivo Excel das tarefas salvas
    #
    # @return A planilha caso exista, cria uma nova caso nao exista
    def _carregar_planilha(self) -> pd.DataFrame:
        pass

    @abstractmethod
    # @brief Adiciona uma tarefa no sistema
    #
    # @param tarefa A tarefa a ser adicionada
    #
    # @param user_email O email do usuario logado
    def adicionarTarefa(self, evento: Tarefa, user_email: str) -> None:
        pass

    @abstractmethod
    # @brief Remove uma tarefa no sistema
    #
    # @param tarefa A tarefa a ser removida
    #
    # @param user_email O email do usuario logado
    def removerTarefa(self, evento: Tarefa, user_email: str) -> None:
        pass

    @abstractmethod
    # @brief Busca uma Tarefa pelo seu Título
    #
    # @param titulo o Título da Tarefa a ser procurada
    #
    # @return A tarefa, se existir. Caso nao exista, retorna None
    def buscarTarefa(self, user_email, titulo: Optional[str] = None, data: Optional[str] = None, mes: Optional[int] = None) -> Optional[Union[Dict, List[Dict]]]:
        pass