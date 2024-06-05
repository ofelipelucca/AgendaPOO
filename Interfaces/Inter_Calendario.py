from abc import ABC, abstractmethod
from typing import List

class Inter_Calendario(ABC):
    
    @abstractmethod
    # @brief - 2 parâmetros - Insere uma lista com uma ou mais atividade em um determinado horário
    #
    # @brief - 1 parâmetro - Insere os horários, atribuídos anteriormente, na agenda em um determinado dia
    #
    # @param key - 2 parâmetros - O horário das atividades
    #
    # @param key - 1 parâmetro - O dia em que os horários serão inseridos na agenda
    #
    # @param atividades As atividades que serão inseridas
    #
    # @Atention Para inserir as atividades na agenda, primeiro insira em um hórario e depois insira em um dia, 
    #         não é suficiente inserir apenas no hórario
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
