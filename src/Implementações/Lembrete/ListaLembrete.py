from src.Interfaces.Inter_Lembrete import Inter_Lembrete, Inter_ListaLembrete

class ListaLembrete(Inter_ListaLembrete):
    def __init__(self) -> None:
        self.__listadeLembretes = {}
    
    def adicionarLembrete(self, Lembrete: Inter_Lembrete, user_email: str):
        self.__listadeLembretes[user_email] = Lembrete
    
    def removerLembrete(self, Lembrete: Inter_Lembrete, user_email: str):
        if user_email in self.__listadeLembretes and self.__listadeLembretes[user_email] == Lembrete:
            del self.__listadeLembretes[user_email]
    
    def buscarLembrete(self, mensagem: str) -> Inter_Lembrete:
        for Lembrete in self.__listadeLembretes.values():
            if Lembrete.getMensagem() == mensagem:
                return Lembrete
        return None

    def tamanho(self) -> int:
        return len(self.__listadeLembretes)

    def obterLembretes(self, user_email: str) -> Inter_Lembrete:
        return self.__listadeLembretes.get(user_email)