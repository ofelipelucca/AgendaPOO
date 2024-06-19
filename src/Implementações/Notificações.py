from src.Interfaces.Inter_Notificação import Inter_Notificação
from src.Implementações.Lembrete import Lembrete
from src.Implementações.Compromisso import Compromisso

from datetime import datetime

class Notificação(Inter_Notificação):
    def __init__(self, horas:int, minutos:int) -> None:
        if not self._validar_minutos(minutos):
            raise ValueError("Minutos de antecedencia devem estar entre 0 e 59.")
        if not self._validar_horas(horas):
            raise ValueError("Horas de antecedencia devem estar entre 0 e 24.")
        
        self.__min_Antes = minutos
        self.__horas_Antes = horas
        self.__estado = False

    def getMinAntes(self) -> int:
        return self.__min_Antes

    def getHorasAntes(self) -> int:
        return self.__horas_Antes

    def setMinAntes(self, minutos: int) -> None:
        if not self._validar_minutos(minutos):
            raise ValueError("Minutos de antecedencia devem estar entre 0 e 59.")
        self.__min_Antes = minutos

    def setHorasAntes(self, horas: int) -> None:
        if not self._validar_horas(horas):
            raise ValueError("Horas de antecedencia devem estar entre 0 e 24.")
        self.__horas_Antes = horas
    
    def notificar(self, item: any) -> None:
        # Obtem a hora atual do sistema
        agora = datetime.now()
        hora_atual = agora.hour
        min_atual = agora.minute

        if isinstance(item, Compromisso):
            descricao = item.getDescricao()
            horario_item = item.getHorario()
        elif isinstance(item, Lembrete):
            descricao = item.getMensagem()
            horario_item = item.getHorario()
        else:
            return

        # Verifica se o horário do item não está vazio
        if horario_item:
            hora_item = int(horario_item[:2])
            min_item = int(horario_item[3:5])

            # Ajusta o horário do item subtraindo os tempos antecipados
            horario_notificacao = (hora_item * 60 + min_item) - (self.__horas_Antes * 60 + self.__min_Antes)
            hora_notificacao = horario_notificacao // 60
            min_notificacao = horario_notificacao % 60

            if self.__estado and hora_notificacao == hora_atual and min_notificacao == min_atual:
                print(f"{descricao} Daqui a: {self.__horas_Antes} horas e {self.__min_Antes} minutos")
        else:
            print("Horario do item está vazio.")

    def ativarNotificacao(self) -> None:
        self.__estado = True

    def desativarNotificacao(self) -> None:
        self.__estado = False

    def checkEstado(self) -> bool:
        return self.__estado
    
    def _validar_horas(self, horas: int) -> bool:
        return 0 <= horas <= 24

    def _validar_minutos(self, minutos: int) -> bool:
        return 0 <= minutos <= 59
