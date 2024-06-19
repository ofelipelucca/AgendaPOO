from src.Interfaces.Inter_Lembrete import Inter_Lembrete
import re
from datetime import datetime

class Lembrete(Inter_Lembrete):
    def __init__(self, data, horario, mensagem) -> None:
        self.setMensagem(mensagem)
        self.setData(data)
        self.setHorario(horario)

    def getData(self) -> str:
        return self.__data
    
    def getHorario(self) -> str:
        return self.__horario
    
    def getMensagem(self) -> str:
        return self.__mensagem
    
    def setData(self, nova_Data: str) -> None:
        self._validar_data(nova_Data)
        self.__data = nova_Data

    def setHorario(self, novo_Horario: str) -> None:
        self._validar_horario(novo_Horario)
        self.__horario = novo_Horario
    
    def setMensagem(self, nova_mensagem: str) -> None:
        if len(nova_mensagem) > 40:
            raise ValueError("A mensagem deve contar entre 1 e 40 caracteres")
        self.__mensagem = nova_mensagem

    def _validar_data(self, data: str) -> None:
        try:
            datetime.strptime(data, '%d/%m/%Y')
        except ValueError:
            raise ValueError("O dia deve estar no formato dd/mm/aaaa")

    def _validar_horario(self, horario: str) -> bool:
        if not self._validar_formato_horario(horario):
            raise ValueError(f"Formato de horário inválido")
        horas, minutos, segundos = map(int, horario.split(':'))
        if not self._validar_horas(horas):
            raise ValueError(f"Hora inválida")
        if not self._validar_minutos(minutos):
            raise ValueError(f"Minutos inválidos")
        if segundos < 0 or segundos > 59:
            raise ValueError(f"Segundos inválidos")
    
    def _validar_formato_horario(self, horario: str) -> bool:
        padrao_horario = re.compile(r'^\d{2}:\d{2}:\d{2}$')
        return padrao_horario.match(horario) is not None

    def _validar_horas(self, horas: int) -> bool:
        return 0 <= horas <= 23
    
    def _validar_minutos(self, minutos: int) -> bool:
        return 0 <= minutos <= 59