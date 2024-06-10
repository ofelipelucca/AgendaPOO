from Interfaces.Inter_Lembrete import Inter_Lembrete, Inter_ListaLembrete, Inter_ImprimirLembrete
import re
from datetime import datetime, timedelta

class Lembrete(Inter_Lembrete):
    def __init__(self,) -> None:
        self.__data = ""
        self.__mensagem = ""
        self.__horario = ""

    def getData(self) -> str:
        return self.__data
    
    def getHorario(self) -> str:
        return self.__horario
    
    def getMensagem(self) -> str:
        return self.__mensagem
    
    def setData(self, nova_Data: str):
        try:
            
            if not re.match(r'\d{2}/\d{2}/\d{4}', nova_Data):
                raise ValueError("Formato da data inválido")

            dia, mes, ano = map(int, nova_Data.split('/'))
            nova_data_dt = datetime(ano, mes, dia)

            
            data_atual = datetime.now()

            
            if nova_data_dt <= data_atual:
                raise ValueError("Data no passado")

            self.__data = nova_Data
        except ValueError as e:
            print("Data deve estar no formato DD/MM/AAAA")
            raise e

    def setHorario(self, novo_Horario: str):
        try:
            
            if not re.match(r'\d{2}:\d{2}:\d{2}', novo_Horario):
                raise ValueError("Formato do horário inválido")

            hora, minuto, segundo = map(int, novo_Horario.split(':'))
            novo_Horario = timedelta(hours=hora, minutes=minuto, seconds=segundo)

            if self.__data:
                dia, mes, ano = map(int, self.__data.split('/'))  # Corrigido aqui
                data_lembrete_dt = datetime(ano, mes, dia, hora, minuto, segundo)

                
                data_atual = datetime.now()

                
                if data_lembrete_dt <= data_atual:
                    raise ValueError("Horário no passado")

            self.__horario = novo_Horario
        except ValueError as e:
            print("Horário deve estar no formato HH:MM:SS")
            raise e
    
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
    
class ImprimirLembrete(Inter_ImprimirLembrete):
    def __init__(self, lista_lembrete: ListaLembrete):
        self.__lista_lembrete = lista_lembrete

    def verLembretes(self, user_email: str):
        lembrete = self.__lista_lembrete.__listadeLembretes.get(user_email)
        if lembrete:
            print("Lembrete: ", lembrete.getMensagem())
            print("Data: ", lembrete.getData())
            print("Horario: ", lembrete.getHorario())
            print("------------------------")
        else:
            print("Nenhum lembrete encontrado para o usuário.")