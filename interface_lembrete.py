from abc import ABC, abstractmethod

class Inter_Lembrete(ABC):
     
     @abstractmethod
     def getData(self,) -> str:
          pass
     
     @abstractmethod
     def getMensagem(self,) -> str:
          pass
     
     @abstractmethod
     def getHorario(self,) -> str:
        pass
     
     @abstractmethod
     def setData(self, nova_Data: str):
        pass

     @abstractmethod
     def setMensagem(self, nova_mensagem: str):
         pass

     @abstractmethod
     def setHorario(self, novo_Horario: str):
         pass

class Inter_ListaLembrete(ABC):
    @abstractmethod
    def adicionarLembrete(self, Lembrete: Inter_Lembrete, user_email: str):
        pass

    @abstractmethod
    def removerLembrete(self, Lembrete: Inter_Lembrete, user_email: str):
        pass

    @abstractmethod
    def buscarLembrete(self, mensagem: str) -> Inter_Lembrete :
        pass

    @abstractmethod
    def tamanho(self,) -> int:
        pass

class Inter_ImprimirLembrete(ABC, Inter_ListaLembrete):
    @abstractmethod
    def verLembretes(self, user_email: str):
        pass

        
         
