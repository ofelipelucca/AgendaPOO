from src.Implementações.Tarefa.Tarefa import Tarefa
from src.Interfaces.Inter_Compromisso import Inter_Compromisso

import re

class Compromisso(Inter_Compromisso, Tarefa):
    def __init__(self, titulo, descricao, data, prioridade, estado, cor, local, horario) -> None:
        super().__init__(titulo, descricao, data, prioridade, estado)
        self.cores_validas = {
            "laranja": "#FF8C00",
            "azul": "#0080FF",
            "roxo": "#9933FF",
            "rosa": "#FFCCFF"
        }

        self.setCor(cor.lower())
        self.setLocal(local)
        self.setHorario(horario)
    
    def getTitulo(self) -> str:
        return super().getTitulo()

    def getCor(self) -> str:
        return self._cor

    def getLocal(self) -> str:
        return self._local

    def getHorario(self) -> str:
        return self._horario

    def setCor(self, nova_cor: str) -> None:
        self._validar_cor(nova_cor.lower())
        self._cor = self._obter_codigo_cor(nova_cor.lower())

    def setLocal(self, novo_local: str) -> None:
        self._validar_local(novo_local)
        self._local = novo_local

    def setHorario(self, novo_horario: str) -> None:
        self._validar_horario(novo_horario)
        self._horario = novo_horario

    def _validar_horario(self, horario: str) -> None:
        padrao_horario = re.compile(r'^\d{2}:\d{2}:\d{2}$')
        if not padrao_horario.match(horario):
            raise ValueError("O horário deve ser real e no formato hh:mm:ss")
        horas, minutos, segundos = map(int, horario.split(':'))
        if not (0 <= horas < 24 and 0 <= minutos < 60 and 0 <= segundos < 60):
            raise ValueError("O horário deve ser real e no formato hh:mm:ss")

    def _validar_cor(self, cor: str) -> None:
        if cor not in self.cores_validas:
            raise ValueError("Cor invalida")

    def _obter_codigo_cor(self, cor: str) -> str:
        return self.cores_validas[cor]

    def _validar_local(self, local: str) -> None:
        if not 1 <= len(local) <= 100:
            raise ValueError("O local deve possuir entre 1 e 100 caracteres")