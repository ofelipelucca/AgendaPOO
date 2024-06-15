from abc import ABC, abstractmethod

class Inter_Notificação(ABC):
    @abstractmethod
    # @brief Busca pelo minutos de antecedência para a notificação
    #
    # @return Inteiro representado os minutos de antecedência
    def getMinAntes(self):
        pass
    
    @abstractmethod
    # @brief Busca pelas horas de antecedência para a notificação
    #
    # @return Inteiro representado as horas de antecedência
    def getHorasAntes():
        pass
    
    @abstractmethod
    # @brief Muda os minutos de antecedência de uma Notificação
    #
    # @param minutos A nova antecedencia a ser mudada
    def setMinAntes(minutos: int):
        pass 
    
    @abstractmethod
    # @brief Muda as horas de antecedência de uma Notificação
    #
    # @param horas A nova antecedencia a ser mudada
    def setHorasAntes(horas: int): 
        pass
    
    @abstractmethod
    # @brief Compara com o horario real e notifica um compromisso no horario programado
    #
    # @param compromisso O compromisso a ser notificado
    def notificar(self, item):
        pass
    
    @abstractmethod
    # @brief Ativa uma notificação
    def ativarNotificacao(self):
        pass

    @abstractmethod
    # @brief Desativa uma notificação
    def desativarNotificacao(self):
        pass

    @abstractmethod
    # @brief Verifica o estado da notificação
    #
    # @return true (se está ativada) ou false (se está desativada)
    def checkEstado(self):
        pass