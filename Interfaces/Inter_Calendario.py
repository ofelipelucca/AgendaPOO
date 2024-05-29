from abc import ABC, abstractmethod
from typing import List

class Inter_Calendario(ABC):
    
    @abstractmethod
    # @brief Insere um grupo de atividades em um determinado horário
    #
    # @param key O horario das atividades ou o dia se for chamada com um parâmetro só
    #
    # @param atividades As atividades que serão inseridas
    def inserir(self, key: str, atividades: List[str] = []) -> None:
        pass
     
    @abstractmethod
    # @brief Calcula o tamanho do mapa de horários
    #
    # @return Um int com o tamanho
    def sizeMapaHorario(self) -> int:
        pass
     
    @abstractmethod
    # @brief Calcula o tamanho da agenda
    #
    # @return Um int com o tamanho
    def sizeAgenda(self) -> int:
        pass
     
    @abstractmethod
    # @brief Ordena a agenda de forma crescente de horários
    def ordenarAgenda(self) -> None:
       pass

    @abstractmethod
    # @brief Imprime o calendario de 7 dias a partir do dia escolhido (Contando com ele)
    #
    # @param dia_inicial O primero dia da sequência a ser mostrada
    def imprimirCalendario(self, dia_inicial: str) -> None:
        pass
