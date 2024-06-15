from src.Implementações.Tarefa.Tarefa import Tarefa, Compromisso
from src.Implementações.Tarefa.ListaTarefa import ListaTarefa

def main():
    # Criando uma lista de tarefas
    lista_tarefas = ListaTarefa()

    # Criando uma tarefa
    tarefa1 = Tarefa("Fazer compras", "Ir ao supermercado comprar alimentos", "10/06/2024", 2, "não feito")

    # Adicionando a tarefa à lista
    lista_tarefas.adicionarTarefa(tarefa1, "user1@example.com")

    # Criando outra tarefa
    tarefa2 = Tarefa("Estudar Python", "Estudar programação em Python", "15/06/2024", 1, "em progresso")

    # Adicionando a segunda tarefa à lista
    lista_tarefas.adicionarTarefa(tarefa2, "user1@example.com")

    # Buscando a tarefa pelo título
    tarefa_encontrada = lista_tarefas.buscarTarefa("Fazer compras")
    if tarefa_encontrada:
        print("Tarefa encontrada:")
        print("Título:", tarefa_encontrada.getTitulo())
        print("Descrição:", tarefa_encontrada.getDescricao())
        print("Data:", tarefa_encontrada.getData())
        print("Prioridade:", tarefa_encontrada.getPrioridade())
        print("Estado:", tarefa_encontrada.getEstado())
    else:
        print("Tarefa não encontrada.")

    # Removendo a primeira tarefa
    lista_tarefas.removerTarefa(tarefa1, "user1@example.com")

    # Buscando a tarefa removida
    tarefa_removida = lista_tarefas.buscarTarefa("Fazer compras")
    if tarefa_removida:
        print("Tarefa encontrada após remoção:", tarefa_removida.getTitulo())
    else:
        print("Tarefa não encontrada após remoção.")

    # Criando uma lista de compromissos
    lista_compromissos = ListaTarefa()

    # Criando um compromisso
    compromisso1 = Compromisso("Reunião de trabalho", "Reunião sobre o projeto X", "15/06/2024", 2, "não feito", "laranja", "Escritório", "09:00:00")

    # Adicionando o compromisso à lista
    lista_compromissos.adicionarTarefa(compromisso1, "user1@example.com")

    # Buscando o compromisso pelo título
    compromisso_encontrado = lista_compromissos.buscarTarefa("Reunião de trabalho")
    if compromisso_encontrado:
        print("Compromisso encontrado:")
        print("Título:", compromisso_encontrado.getTitulo())
        print("Descrição:", compromisso_encontrado.getDescricao())
        print("Data:", compromisso_encontrado.getData())
        print("Prioridade:", compromisso_encontrado.getPrioridade())
        print("Estado:", compromisso_encontrado.getEstado())
        print("Cor:", compromisso_encontrado.getCor())
        print("Local:", compromisso_encontrado.getLocal())
        print("Horário:", compromisso_encontrado.getHorario())
    else:
        print("Compromisso não encontrado.")

    # Removendo o compromisso
    lista_compromissos.removerTarefa(compromisso1, "user1@example.com")

if __name__ == "__main__":
    main()
