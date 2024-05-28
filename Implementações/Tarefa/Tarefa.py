from Interfaces.Inter_Tarefa import Inter_Tarefa, Inter_Compromisso

#   GUIA DE PRIORIDADES DAS TAREFAS:
#
#       1 - MAIS IMPORTANTE
#         2 - IMPORTANTE
#           3 - MENOS IMPORTANTE

#   GUIA DE ESTADOS DAS TAREFAS:
#
#       FEITO (DELETAR EM SEGUIDA)
#         EM PROGRESSO
#           NAO FEITO (ALERTAR)

class Tarefa(Inter_Tarefa):
    def __init__(self, titulo: str, descricao: str, data: str, prioridade: int, estado: str) -> None:
        self._titulo = titulo
        self._descricao = descricao
        self._data = data
        self._prioridade = prioridade
        self._estado = estado
  
    # @brief Busca pelo titulo da tarefa
    #
    # @return String do titulo
    def getTitulo(self) -> str:
        return self._titulo

    # @brief Busca pela descricao da tarefa
    #
    # @return String da destricao
    def getDescricao(self) -> str:
        return self._descricao

    # @brief Busca pela data da tarefa
    #
    # @return String da data
    def getData(self) -> str:
        return self._data

    # @brief Busca pela prioridade da tarefa
    #
    # @return Unsigned (1, 2 ou 3)
    def getPrioridade(self) -> str:
        return self._prioridade

    # @brief Busca pelo estado da tarefa
    #
    # @return String do estado
    def getEstado(self) -> str:
        return self._estado

    # @brief Muda o titulo de uma tarefa
    #
    # @param novo_Titulo O novo titulo 
    def setTitulo(self, novo_Titulo: str) -> None:
        MAX_CARACTERES = 50

        if novo_Titulo <= MAX_CARACTERES or not novo_Titulo:
            self._titulo = novo_Titulo
        else:
            print("Titulo invalido!")
            print("O titulo deve possuir entre 1 e 50 caracteres")

    # @brief Muda a descricao de uma tarefa
    #
    # @param nova_Descricao A nova descricao
    def setDescricao(self, nova_Descricao: str) -> None:
        MAX_CARACTERES = 120

        if nova_Descricao <= MAX_CARACTERES or not nova_Descricao:
            self._descricao = nova_Descricao
        else:
            print("Descricao invalida!")
            print("A descricao deve possuir entre 1 e 120 caracteres")

    # @brief Muda a data de uma tarefa
    #
    # @param nova_Data a nova data 
    #
    # @attention A data informada deve estar no formato: DD/MM/AAAA
    def setData(self, nova_Data: str) -> None:
        pass

    # @brief Muda a prioridade de uma tarefa
    #
    # @param nova_Prioridade A nova prioridade 
    def setPrioridade(self, nova_Prioridade: int) -> None:
        if nova_Prioridade == 1 or nova_Prioridade == 2 or nova_Prioridade == 3:
            self._prioridade = nova_Prioridade
        else:
            print("Prioridade invalida!")
            print("A prioridade deve ser:")
            print(" - '1' para mais importante")
            print(" - '2' para importante")
            print(" - '2' para menos importante")

    # @brief Muda o estado de uma tarefa
    #
    # @param novo_Estado O novo estado
    def setEstado(self, novo_Estado) -> None:
        estados = {
            "feito",
            "em progresso",
            "não feito"
        }
        if novo_Estado in estados:
            self._estado = novo_Estado
        else:
            print("Estado invalido!")
            print("O estado deve ser:")
            for estado in estados:
                print(f"    - '{estado}'")

class Compromisso(Inter_Compromisso):

    def __init__(self, titulo: str, descricao: str, data: str, prioridade: int, estado: str, cor: str, local: str, horario: str) -> None:
        super().__init__(titulo, descricao, data, prioridade, estado)
        self._cor = cor
        self._local = local
        self._horario = horario
    
    def getTitulo(self) -> str:
        return self._titulo

    # @brief Busca pela descricao da tarefa
    #
    # @return String da destricao
    def getDescricao(self) -> str:
        return self._descricao

    # @brief Busca pela data da tarefa
    #
    # @return String da data
    def getData(self) -> str:
        return self._data

    # @brief Busca pela prioridade da tarefa
    #
    # @return Unsigned (1, 2 ou 3)
    def getPrioridade(self) -> str:
        return self._prioridade

    # @brief Busca pelo estado da tarefa
    #
    # @return String do estado
    def getEstado(self) -> str:
        return self._estado

    # @brief Muda o titulo de uma tarefa
    #
    # @param novo_Titulo O novo titulo 
    def setTitulo(self, novo_Titulo: str) -> None:
        MAX_CARACTERES = 50

        if novo_Titulo <= MAX_CARACTERES or not novo_Titulo:
            self._titulo = novo_Titulo
        else:
            print("Titulo invalido!")
            print("O titulo deve possuir entre 1 e 50 caracteres")

    # @brief Muda a descricao de uma tarefa
    #
    # @param nova_Descricao A nova descricao
    def setDescricao(self, nova_Descricao: str) -> None:
        MAX_CARACTERES = 120

        if nova_Descricao <= MAX_CARACTERES or not nova_Descricao:
            self._descricao = nova_Descricao
        else:
            print("Descricao invalida!")
            print("A descricao deve possuir entre 1 e 120 caracteres")

    # @brief Muda a data de uma tarefa
    #
    # @param nova_Data a nova data 
    #
    # @attention A data informada deve estar no formato: DD/MM/AAAA
    def setData(self, nova_Data: str) -> None:
        pass

    # @brief Muda a prioridade de uma tarefa
    #
    # @param nova_Prioridade A nova prioridade 
    def setPrioridade(self, nova_Prioridade: int) -> None:
        if nova_Prioridade == 1 or nova_Prioridade == 2 or nova_Prioridade == 3:
            self._prioridade = nova_Prioridade
        else:
            print("Prioridade invalida!")
            print("A prioridade deve ser:")
            print(" - '1' para mais importante")
            print(" - '2' para importante")
            print(" - '2' para menos importante")

    # @brief Muda o estado de uma tarefa
    #
    # @param novo_Estado O novo estado
    def setEstado(self, novo_Estado) -> None:
        estados = {
            "feito",
            "em progresso",
            "não feito"
        }
        if novo_Estado in estados:
            self._estado = novo_Estado
        else:
            print("Estado invalido!")
            print("O estado deve ser:")
            for estado in estados:
                print(f"    - '{estado}'")

    # @brief Busca pela cor do compromisso
    #
    # @return String com o codigo ANSI da cor
    def getCor(self) -> str:
        return self._cor

    # @brief Busca pelo local do compromisso
    #
    # @return String do local 
    def getLocal(self) -> str:
        return self._local

    # @brief Busca pelo horario do compromisso
    #
    # @return String do horario
    def getHorario(self) -> str:
        return self._horario

    # @brief Muda a cor de um compromisso
    #
    # @attencion Cores aceitas: 'laranja', 'azul', 'roxo', 'rosa'
    #
    # @param nova_Cor A nova cor 
    def setCor(self, nova_Cor: str) -> None:
        cores = {
            "laranja": "\033[38;2;247;99;25m",
            "azul": "\033[38;2;25;84;247m",
            "roxo": "\033[38;2;140;25;247m",
            "rosa": "\033[38;2;247;25;180m"
        }

        if nova_Cor in cores:
            self._cor = cores[nova_Cor]
        else: 
            print("Cor invalida!")
            print("Cores aceitas:")
            for cor in cores:
                print(f"    - '{cor}'")

    # @brief Muda o local de um compromisso
    #
    # @param novo_Local O novo local 
    def setLocal(self, novo_Local: str) -> None:
        MAX_CARACTERES = 100

        if novo_Local <= MAX_CARACTERES or not novo_Local:
            self._local = novo_Local
        else:
            print("Local invalido!")
            print("O local deve possuir entre 1 e 100 caracteres")

    # @brief Muda o horario de um compromisso
    #
    # @param novo_Horario O novo horario
    #
    # @attention O horario informado deve estar no formato: HH:MM:SS
    def setHorario(self, novo_Horario: str) -> None:
        pass