from abc import ABC, abstractmethod

class Inter_Lembrete(ABC):
    @abstractmethod
    # @brief Busca pela data do lembrete
    #
    # @return String da data
    def getData(self) -> str:
        pass
     
    @abstractmethod
    # @brief Busca pela mensagem do lembrete
    #
    # @return String da mensagem
    def getMensagem(self) -> str:
        pass
    
    @abstractmethod
    # @brief Busca pelo horario do lembrete
    #
    # @return String do horario
    def getHorario(self) -> str:
        pass
     
    @abstractmethod
    # @brief Muda a data de um lembrete
    #
    # @param nova_Data A nova data a ser adicionada
    #
    # @attention A data informada deve estar no formato: DD/MM/AAAA
    def setData(self, nova_data: str):
       pass

    @abstractmethod
    # @brief Muda a mensagem de um lembrete
    #
    # @param nova_mensagem A nova mensagem a ser adicionada
    def setMensagem(self, nova_mensagem: str):
        pass

    @abstractmethod
    # @brief Muda o horario de um compromisso
    #
    # @param novo_Horario O novo horario a ser colocado
    #
    # @attention O horario informado deve estar no formato: HH:MM:SS
    def setHorario(self, novo_horario: str):
        pass