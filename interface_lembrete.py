from abc import ABC, abstractmethod

class Lembrete(ABC):
     
     @abstractmethod
     def __init__(self, data:str, mensagem:str, horario:str) -> None:
          pass
    
     @abstractmethod
     def getData(self,):
          pass
     
     @abstractmethod
     def getMensagem(self,):
          pass
     
     @abstractmethod
     def getHorario(self,):
        pass
     
     @abstractmethod
     def setData(self, nova_Data):
        pass

     @abstractmethod
     def setMensagem(self, nova_mensagem):
         pass

     @abstractmethod
     def setHorario(self, novo_Horario):
         pass


class ListaLembrete(ABC):
    @abstractmethod
    def __init__(self, listadeLembrete ) -> None:
        pass

    @abstractmethod
    def adicionarLembrete(self, Lembrete, user_email):
        pass

    @abstractmethod
    def removerLembrete(self, Lembrete, user_email):
        pass

    @abstractmethod
    def buscarLembrete(self, mensagem):
        pass

    @abstractmethod
    def tamanho(self,):
        pass

class ImprimirLembrete(ABC, ListaLembrete):
    @abstractmethod
    def verLembretes(self, user_email):
        pass

        
         
