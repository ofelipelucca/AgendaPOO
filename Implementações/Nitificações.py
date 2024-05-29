from Interfaces.Inter_Notificação import Inter_Notificação
from Implementações.Lembrete import Lembrete
from Implementações.Tarefa.Tarefa import Compromisso
from datetime import datetime, timedelta

class Notificação(Inter_Notificação):
    def __init__(self, minutos, horas) -> None:
        self.__min_Antes= minutos
        self.__horas_Antes = horas
        self.__estado = False
    
    def notificar(self, item):
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

        hora_item = int(horario_item[:2])
        min_item = int(horario_item[3:5])

        # Ajusta o horário do item subtraindo os tempos antecipados
        horario_notificacao = (hora_item * 60 + min_item) - (self.__horas_Antes * 60 + self.__min_Antes)
        hora_notificacao = horario_notificacao // 60
        min_notificacao = horario_notificacao % 60

        if self.__estado and hora_notificacao == hora_atual and min_notificacao == min_atual:
            print(f"{descricao} Daqui a: {self.__horas_Antes} horas e {self.__min_Antes} minutos")

    def ativarNotificacao(self):
        self.__estado = True

    def desativarNotificacao(self):
        self.__estado = False

    def checkEstado(self):
        return self.__estado
