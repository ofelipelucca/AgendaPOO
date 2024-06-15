from src.Interfaces.Inter_Tarefa import Inter_Tarefa, Inter_Compromisso
from datetime import datetime
import re

# GUIA DE PRIORIDADES DAS TAREFAS:
# 1 - MAIS IMPORTANTE
# 2 - IMPORTANTE
# 3 - MENOS IMPORTANTE

# GUIA DE ESTADOS DAS TAREFAS:
# FEITO (DELETAR EM SEGUIDA)
# EM PROGRESSO
# NAO FEITO (ALERTAR)

class Tarefa(Inter_Tarefa):
    def __init__(self, titulo, descricao, data, prioridade, estado) -> None:
        self.setTitulo(titulo)
        self.setDescricao(descricao)
        self.setData(data)
        self.setPrioridade(prioridade)
        self.setEstado(estado)
  
    def getTitulo(self) -> str:
        return self._titulo

    def getDescricao(self) -> str:
        return self._descricao

    def getData(self) -> str:
        return self._data

    def getPrioridade(self) -> int:
        return self._prioridade

    def getEstado(self) -> str:
        return self._estado

    def setTitulo(self, novo_titulo: str) -> None:
        self._validar_titulo(novo_titulo)
        self._titulo = novo_titulo

    def setDescricao(self, nova_descricao: str) -> None:
        self._validar_descricao(nova_descricao)
        self._descricao = nova_descricao

    def setData(self, nova_data: str) -> None:
        self._validar_data(nova_data)
        self._data = nova_data

    def setPrioridade(self, nova_prioridade: int) -> None:
        self._validar_prioridade(nova_prioridade)
        self._prioridade = nova_prioridade

    def setEstado(self, novo_estado: str) -> None:
        self._validar_estado(novo_estado)
        self._estado = novo_estado

    def _validar_titulo(self, titulo: str) -> None:
        if not 1 <= len(titulo) <= 60:
            raise ValueError("O titulo deve possuir entre 1 e 60 caracteres")

    def _validar_descricao(self, descricao: str) -> None:
        if not 1 <= len(descricao) <= 120:
            raise ValueError("A descricao deve possuir entre 1 e 120 caracteres")

    def _validar_data(self, data: str) -> None:
        try:
            datetime.strptime(data, '%d/%m/%Y')
        except ValueError:
            raise ValueError("O dia deve estar no formato dd/mm/aaaa")

    def _validar_prioridade(self, prioridade: int) -> None:
        if prioridade not in {1, 2, 3}:
            raise ValueError("Prioridade invalida. (1, 2, 3)")

    def _validar_estado(self, estado: str) -> None:
        if estado not in {"feito", "em progresso", "não feito"}:
            raise ValueError("Estado invalido. (feito, em progresso, não feito)")


class Compromisso(Inter_Compromisso, Tarefa):
    def __init__(self, titulo, descricao, data, prioridade, estado, cor, local, horario) -> None:
        super().__init__(titulo, descricao, data, prioridade, estado)
        self.setCor(cor)
        self.setLocal(local)
        self.setHorario(horario)

    def getCor(self) -> str:
        return self._cor

    def getLocal(self) -> str:
        return self._local

    def getHorario(self) -> str:
        return self._horario

    def setCor(self, nova_cor: str) -> None:
        self._validar_cor(nova_cor)
        self._cor = self._obter_codigo_cor(nova_cor)

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
        if cor not in {"laranja", "azul", "roxo", "rosa"}:
            raise ValueError("Cor invalida")

    def _obter_codigo_cor(self, cor: str) -> str:
        cores = {
            "laranja": "#FF8C00",
            "azul": "#0080FF",
            "roxo": "#9933FF",
            "rosa": "#FFCCFF"
        }
        return cores[cor]

    def _validar_local(self, local: str) -> None:
        if not 1 <= len(local) <= 100:
            raise ValueError("O local deve possuir entre 1 e 100 caracteres")