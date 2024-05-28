from abc import ABC, abstractmethod
from Implementações.Tarefa.Tarefa import Compromisso
from Implementações.Lembrete import Lembrete

class Inter_Notificação(ABC):

    @abstractmethod
    # @brief Compara com o horario real e notifica um compromisso no horario programado
    #
    # @param compromisso O compromisso a ser notificado
    def notificar(self, item):
        pass
    
    @abstractmethod
    # @brief Ativa uma notificação
    def ativarNotificacao():
        pass

    @abstractmethod
    # @brief Desativa uma notificação
    def desativarNotificacao():
        pass

    @abstractmethod
    # @brief Verifica o estado da notificação
    #
    # @return true (se está ativada) ou false (se está desativada)
    def checkEstado():
        pass