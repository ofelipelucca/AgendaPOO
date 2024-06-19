from abc import ABC, abstractmethod

#   GUIA DE PRIORIDADES DAS TAREFAS:
#
#       1 - MAIS IMPORTANTE
#         2 - IMPORTANTE
#           3 - MENOS IMPORTANTE

#   GUIA DE ESTADOS DAS TAREFAS:
#
#       FEITO (DELETAR EM SEGUIDA)
#         EM PROGRESSO
#           NAO FEITO (ALERTAR)

class Inter_Tarefa(ABC):

    @abstractmethod
    # @brief Busca pelo titulo da tarefa
    #
    # @return String do titulo
    def getTitulo(self) -> str:
        pass

    @abstractmethod
    # @brief Busca pela descricao da tarefa
    #
    # @return String da destricao
    def getDescricao(self) -> str:
        pass
    
    @abstractmethod
    # @brief Busca pela data da tarefa
    #
    # @return String da data
    def getData(self) -> str:
        pass
    
    @abstractmethod
    # @brief Busca pela prioridade da tarefa
    #
    # @return Unsigned (1, 2 ou 3)
    def getPrioridade(self) -> str:
        pass
    
    @abstractmethod
    # @brief Busca pelo estado da tarefa
    #
    # @return String do estado
    def getEstado(self) -> str:
        pass
    
    @abstractmethod
    # @brief Muda o titulo de uma tarefa
    #
    # @param novo_Titulo O novo titulo 
    def setTitulo(self, novo_Titulo: str) -> None:
        pass

    @abstractmethod
    # @brief Muda a descricao de uma tarefa
    #
    # @param nova_Descricao A nova descricao
    def setDescricao(self, nova_Descricao: str) -> None:
        pass
    
    @abstractmethod
    # @brief Muda a data de uma tarefa
    #
    # @param nova_Data a nova data 
    #
    # @attention A data informada deve estar no formato: DD/MM/AAAA
    def setData(self, nova_Data: str) -> None:
        pass
    
    @abstractmethod
    # @brief Muda a prioridade de uma tarefa
    #
    # @param nova_Prioridade A nova prioridade 
    def setPrioridade(self, nova_Prioridade: int) -> None:
        pass
    
    @abstractmethod
    # @brief Muda o estado de uma tarefa
    #
    # @param novo_Estado O novo estado
    def setEstado(self, novo_Estado: str) -> None:
        pass