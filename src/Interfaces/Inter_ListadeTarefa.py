from abc import ABC, abstractmethod
from src.Implementações.Tarefa import Tarefa

class Inter_listadeTarefa(ABC):
    @abstractmethod
    # @brief Adiciona uma tarefa no sistema
    #
    # @param tarefa A tarefa a ser adicionada
    #
    # @param user_email O email do usuario logado
    def adicionarTarefa(self, tarefa: Tarefa, user_email: str) -> None:
        pass

    @abstractmethod
    # @brief Remove uma tarefa no sistema
    #
    # @param tarefa A tarefa a ser removida
    #
    # @param user_email O email do usuario logado
    def removerTarefa(self, tarefa: Tarefa, user_email: str) -> None:
        pass

    @abstractmethod
    # @brief Busca uma Tarefa pelo seu Título
    #
    # @param titulo o Título da Tarefa a ser procurada
    #
    # @return A tarefa, se existir. Caso nao exista, retorna None
    def buscarTarefa(self, titulo: str) -> Tarefa:
        pass