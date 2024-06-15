from Interfaces.Inter_Lembrete import Inter_Lembrete, Inter_ListaLembrete, Inter_ImprimirLembrete
import re
from datetime import datetime, timedelta

class Lembrete(Inter_Lembrete):
    def __init__(self, data, horario, mensagem) -> None:
        if not self._validar_data(data):
            raise ValueError("O dia deve estar no formato dd/mm/aaaa")
        if not self._validar_horario(horario):
            raise ValueError("O horário deve estar no formato hh:mm:ss")
        
        self.__data = data
        self.__mensagem = mensagem
        self.__horario = horario

    def getData(self) -> str:
        return self.__data
    
    def getHorario(self) -> str:
        return self.__horario
    
    def getMensagem(self) -> str:
        return self.__mensagem
    
    def setData(self, nova_Data: str) -> None:
        if not self._validar_data(nova_Data):
            raise ValueError("O dia deve estar no formato dd/mm/aaaa")
        self.__data = nova_Data

    def setHorario(self, novo_Horario: str) -> None:
        if not self._validar_horario(novo_Horario):
            raise ValueError("O horário deve ser real e no formato hh:mm:ss")
        self.__horario = novo_Horario
    
    def setMensagem(self, nova_mensagem: str):
        try:
            MAX_CARACTERES = 45

            if len(nova_mensagem) > MAX_CARACTERES:
                raise ValueError("Mensagem muito longa")
            if nova_mensagem == self.__mensagem:
                raise ValueError("Mensagem deve ser diferente da atual")
            if not nova_mensagem:
                raise ValueError("Mensagem não pode ser vazia")

            self.__mensagem = nova_mensagem
        except ValueError as e:
            print("A mensagem deve ser diferente da mensagem atual e possuir no máximo 45 caracteres")
            raise e

    def _validar_data(self, data: str) -> bool:
        try:
            datetime.strptime(data, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def _validar_horario(self, horario: str) -> bool:
        if not self._validar_formato_horario(horario):
            return False
        horas, minutos, segundos = map(int, horario.split(':'))
        if not self._validar_horas(horas):
            return False
        if not self._validar_minutos(minutos):
            return False
        if segundos < 0 or segundos > 59:
            return False
        return True
    def _validar_formato_horario(self, horario: str) -> bool:
        padrao_horario = re.compile(r'^\d{2}:\d{2}:\d{2}$')
        return padrao_horario.match(horario) is not None

    def _validar_horas(self, horas: int) -> bool:
        return 0 <= horas <= 23
    
    def _validar_minutos(self, minutos: int) -> bool:
        return 0 <= minutos <= 59

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
    
class ImprimirLembrete(Inter_ImprimirLembrete):
    def __init__(self, lista_lembrete: ListaLembrete):
        self.__lista_lembrete = lista_lembrete

    def adicionarLembrete(self, Lembrete: Inter_Lembrete, user_email: str):
        self.__lista_lembrete.adicionarLembrete(Lembrete, user_email)
    
    def removerLembrete(self, Lembrete: Inter_Lembrete, user_email: str):
        self.__lista_lembrete.removerLembrete(Lembrete, user_email)
    
    def buscarLembrete(self, mensagem: str) -> Inter_Lembrete:
        return self.__lista_lembrete.buscarLembrete(mensagem)
    
    def tamanho(self) -> int:
        return self.__lista_lembrete.tamanho()

    def verLembretes(self, user_email: str):
        lembrete = self.__lista_lembrete.obterLembretes(user_email)
        if lembrete:
            print("Lembrete: ", lembrete.getMensagem())
            print("Data: ", lembrete.getData())
            print("Horario: ", lembrete.getHorario())
            print("------------------------")
        else:
            print("Nenhum lembrete encontrado para o usuário.")