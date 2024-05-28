from Tarefa import Tarefa

class ListaTarefa():

    def __init__(self) -> None:
        self._listadetarefa = {}

    # @brief Adiciona uma tarefa no sistema
    #
    # @param tarefa A tarefa a ser adicionada
    #
    # @param user_email O email do usuario logado
    def adicionarTarefa(self, tarefa: Tarefa, user_email: str) -> None:
        if user_email not in self._listadetarefa:
            self._listadetarefa[user_email] = [tarefa]
        else:
            print("A tarefa ja existe.")

    # @brief Remove uma tarefa no sistema
    #
    # @param tarefa A tarefa a ser removida
    #
    # @param user_email O email do usuario logado
    def removerTarefa(self, tarefa: Tarefa, user_email: str) -> None:
        if user_email in self._listadetarefa:
            if tarefa in self._listadetarefa[user_email]:
                self._listadetarefa[user_email].remove(tarefa)
                print("Tarefa removida com sucesso.")
            else:
                print("A tarefa não existe para este usuario.")
        else:
            print("O usuario nao possui tarefas associadas.")

    # @brief Busca uma Tarefa pelo seu Título
    #
    # @param titulo o Título da Tarefa a ser procurada
    #
    # @return A tarefa, se existir. Caso nao exista, retorna None
    def buscarTarefa(self, titulo: str) -> Tarefa:
        for usuario in self._listadetarefa.values():
            for tarefa in usuario:
                if tarefa._titulo == titulo: 
                    return tarefa
        return None