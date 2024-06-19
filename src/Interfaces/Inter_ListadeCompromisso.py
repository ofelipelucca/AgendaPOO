from src.Implementações.Compromisso import Compromisso

from abc import ABC, abstractmethod
import pandas as pd
from typing import Optional, Union, List, Dict

class Inter_listadeCompromisso(ABC):
    @abstractmethod
    # @brief Carrega a planilha do arquivo Excel dos compromissos salvos
    #
    # @return A planilha caso exista, cria uma nova caso nao exista
    def _carregar_planilha(self) -> pd.DataFrame:
        pass

    @abstractmethod
    # @brief Adiciona um Compromisso no sistema
    #
    # @param Compromisso O Compromisso a ser adicionada
    #
    # @param user_email O email do usuario logado
    def adicionarCompromisso(self, evento: Compromisso, user_email: str) -> None:
        pass

    @abstractmethod
    # @brief Remove um Compromisso no sistema
    #
    # @param Compromisso O Compromisso a ser removido
    #
    # @param user_email O email do usuario logado
    def removerCompromisso(self, evento: Compromisso, user_email: str) -> None:
        pass

    @abstractmethod
    # @brief Busca um Compromisso pelo seu Título
    #
    # @param titulo o Título do Compromisso a ser procurado (opcional)
    # @param data a Data do Compromisso a ser procurado (opcional)
    # @param mes o Mês do Compromisso a ser procurado (opcional)
    #
    # @return O Compromisso, se existir. Caso nao exista, retorna None
    def buscarCompromisso(self, user_email, titulo: Optional[str] = None, data: Optional[str] = None, mes: Optional[int] = None) -> Optional[Union[Dict, List[Dict]]]:
        pass