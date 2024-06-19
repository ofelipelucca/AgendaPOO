from src.Interfaces.Inter_Tarefa import Inter_Tarefa

from abc import ABC, abstractmethod

class Inter_Compromisso(Inter_Tarefa):
    @abstractmethod
    # @brief Busca pela cor do compromisso
    #
    # @return String com o codigo ANSI da cor
    def getCor(self) -> str:
        pass
    
    @abstractmethod
    # @brief Busca pelo local do compromisso
    #
    # @return String do local 
    def getLocal(self) -> str:
        pass
    
    @abstractmethod
    # @brief Busca pelo horario do compromisso
    #
    # @return String do horario
    def getHorario(self) -> str:
        pass

    @abstractmethod
    # @brief Muda a cor de um compromisso
    #
    # @attencion Cores aceitas: 'laranja', 'azul', 'roxo', 'rosa'
    #
    # @param nova_Cor A nova cor 
    def setCor(self, nova_Cor: str) -> None:
        pass

    @abstractmethod
    # @brief Muda o local de um compromisso
    #
    # @param novo_Local O novo local 
    def setLocal(self, novo_Local: str) -> None:
        pass
    
    @abstractmethod
    # @brief Muda o horario de um compromisso
    #
    # @param novo_Horario O novo horario
    #
    # @attention O horario informado deve estar no formato: HH:MM:SS
    def setHorario(self, novo_Horario: str) -> None:
        pass