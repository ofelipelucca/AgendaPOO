from abc import ABC, abstractmethod

class Inter_Lembrete(ABC):
    
    @abstractmethod
    # @brief Busca pela data do lembrete
    #
    # @return String da data
    def getData(self,) -> str:
        pass
     
    @abstractmethod
    # @brief Busca pela mensagem do lembrete
    #
    # @return String da mensagem
    def getMensagem(self,) -> str:
        pass
     
    @abstractmethod
    # @brief Busca pelo horario do lembrete
    #
    # @return String do horario
    def getHorario(self,) -> str:
        pass
     
    @abstractmethod
    # @brief Muda a data de um lembrete
    #
    # @param nova_Data A nova data a ser adicionada
    #
    # @attention A data informada deve estar no formato: DD/MM/AAAA
    def setData(self, nova_Data: str):
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
    def setHorario(self, novo_Horario: str):
        pass

class Inter_ListaLembrete(ABC):
    @abstractmethod
    # @brief Adiciona um Lembrete a lista de Lembretes
    #
    # @param lembrete O lembrete a ser adicionado
    #
    # @param user_email O email do usuário logado
    def adicionarLembrete(self, Lembrete: Inter_Lembrete, user_email: str):
        pass

    @abstractmethod
    # @brief Remove um lembrete da lista
    #
    # @param lembrete O lembrete a ser removido
    #
    # @param user_email O email do usuário logado
    def removerLembrete(self, Lembrete: Inter_Lembrete, user_email: str):
        pass

    @abstractmethod
    # @brief Procura pelo lembrete pela mensagem
    #
    # @param mensagem A mensagem do lembrete a ser buscado
    def buscarLembrete(self, mensagem: str) -> Inter_Lembrete :
        pass

    @abstractmethod
    # @brief Calcula o tamanho do mapa
    #
    # @return Um unsigned com o tamanho
    def tamanho(self,) -> int:
        pass

class Inter_ImprimirLembrete(ABC, Inter_ListaLembrete):
    @abstractmethod
    # @brief Imprime todos lembretes da lista 
    #
    # @param user_email O email do usuario logado
    def verLembretes(self, user_email: str):
        pass