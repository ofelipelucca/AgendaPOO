from src.Implementações.Lembrete.Lembrete import Lembrete
from src.Interfaces.Inter_Lembrete import Inter_ImprimirLembrete
from src.Implementações.Lembrete.ListaLembrete import ListaLembrete

class ImprimirLembrete(Inter_ImprimirLembrete):
    def __init__(self, lista_lembrete: ListaLembrete):
        self.__lista_lembrete = lista_lembrete

    def adicionarLembrete(self, Lembrete: Lembrete, user_email: str):
        self.__lista_lembrete.adicionarLembrete(Lembrete, user_email)
    
    def removerLembrete(self, Lembrete: Lembrete, user_email: str):
        self.__lista_lembrete.removerLembrete(Lembrete, user_email)
    
    def buscarLembrete(self, mensagem: str) -> Lembrete:
        return self.__lista_lembrete.buscarLembrete(mensagem)
    
    def tamanho(self) -> int:
        return self.__lista_lembrete.tamanho()

    def verLembretes(self, user_email: str):
        lembrete = self.__lista_lembrete.obterLembretes(user_email)
        if lembrete:
            print("Lembrete: ", lembrete['Mensagem'][0])
            print("Data: ", lembrete['Data'][0])
            print("Horario: ", lembrete['Horário'][0])
            print("------------------------")
        else:
            print("Nenhum lembrete encontrado para o usuário.")