from interface_Lembrete import Inter_Lembrete, Inter_ListaLembrete, Inter_ImprimirLembrete
import re
from datetime import datetime, timedelta

class Lembrete(Inter_Lembrete):
    def __init__(self, data, mensagem, horario) -> None:
        self. _data = data
        self. __mensagem = mensagem
        self. __horario = horario

    def getData(self) -> str:
        return self._data
    
    def getHorario(self) -> str:
        return self.__horario
    
    def getMensagem(self) -> str:
        return self.__horario
    
    def setData(self, nova_Data: str):
        try:
            # Verifica o formato da nova data
            if not re.match(r'\d{2}/\d{2}/\d{4}', nova_Data):
                raise ValueError("Formato da data inválido")

            dia, mes, ano = map(int, nova_Data.split('/'))
            nova_data_dt = datetime(ano, mes, dia)

            # Obtem a data atual do sistema
            data_atual = datetime.now()

            # Verifica se a nova data está no futuro
            if nova_data_dt <= data_atual:
                raise ValueError("Data no passado")

            self._data = nova_Data
        except ValueError as e:
            print("Data deve estar no formato DD/MM/AAAA")
            raise e

    def setHorario(self, novo_Horario: str):
        try:
            # Verifica o formato do novo horário
            if not re.match(r'\d{2}:\d{2}:\d{2}', novo_Horario):
                raise ValueError("Formato do horário inválido")

            hora, minuto, segundo = map(int, novo_Horario.split(':'))
            novo_Horario = timedelta(hours=hora, minutes=minuto, seconds=segundo)

            if self._data:
                dia, mes, ano = map(int, self._data.split('/'))
                data_lembrete_dt = datetime(ano, mes, dia, hora, minuto, segundo)

                # Obtem a data atual do sistema
                data_atual = datetime.now()

                # Verifica se o novo horário está no futuro
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
            if nova_mensagem == self._mensagem:
                raise ValueError("Mensagem deve ser diferente da atual")
            if not nova_mensagem:
                raise ValueError("Mensagem não pode ser vazia")

            self.__mensagem = nova_mensagem
        except ValueError as e:
            print("A mensagem deve ser diferente da mensagem atual e possuir no máximo 45 caracteres")
            raise e
    
class ListaLembrete(Inter_ListaLembrete):
    def __init__(self) -> None:
        self._listadeLembretes = {}
    
    def adicionarLembrete(self, Lembrete: Inter_Lembrete, user_email: str):
        self._listadeLembretes[user_email] = Lembrete
    
    def removerLembrete(self, Lembrete: Inter_Lembrete, user_email: str):
        if user_email in self._listadeLembretes and self._listadeLembretes[user_email] == Lembrete:
            del self._listadeLembretes[user_email]
    
    def buscarLembrete(self, mensagem: str) -> Inter_Lembrete:
        for Lembrete in self._listadeLembretes.values():
            if Lembrete.get_mensagem() == mensagem:
                return Lembrete
        return None

    def tamanho(self) -> int:
        return len(self._listadeLembretes)
    
class ImprimirLembrete(Inter_ImprimirLembrete):
    def verLembretes(self, user_email: str):
        lembrete = self._listadeLembretes.get(user_email)
        if lembrete:
            print("Lembrete: ", lembrete.getData())
            print("Data: ", lembrete.getData())
            print("Horario: ", lembrete.getHorario())
            print("------------------------")
        else:
            print("Nenhum lembrete encontrado para o usuário.")
