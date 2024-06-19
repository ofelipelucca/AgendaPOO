from src.Interfaces.Inter_Tarefa import Inter_Tarefa

from datetime import datetime

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
        if not 1 <= len(titulo) <= 15:
            raise ValueError("O titulo deve possuir entre 1 e 15 caracteres")

    def _validar_descricao(self, descricao: str) -> None:
        if not 1 <= len(descricao) <= 35:
            raise ValueError("A descricao deve possuir entre 1 e 35 caracteres")

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