from src.Implementações.Tarefa.Tarefa import Tarefa
from src.Implementações.Tarefa.ListaTarefa import ListaTarefa

def main():
    # Criando uma lista de tarefas
    lista_tarefas = ListaTarefa()

    # Criando uma tarefa
    tarefa1 = Tarefa("Fazer compras", "Comprar alimentos", "10/06/2024", 2, "não feito")

    # Adicionando a tarefa à lista
    lista_tarefas.adicionarTarefa(tarefa1, "user1@example.com")

    # Criando outra tarefa
    tarefa2 = Tarefa("Estudar Python", "Estudar programação", "15/06/2024", 1, "em progresso")

    # Adicionando a segunda tarefa à lista
    lista_tarefas.adicionarTarefa(tarefa2, "user1@example.com")

    # Buscando a tarefa pelo título
    tarefa_encontrada = lista_tarefas.buscarTarefa("user1@example.com", "Fazer compras")
    if tarefa_encontrada:
        print("Tarefa encontrada:")
        print("Título:", tarefa_encontrada['Título'])
        print("Descrição:", tarefa_encontrada['Descrição'])
        print("Data:", tarefa_encontrada['Data'])
        print("Prioridade:", tarefa_encontrada['Prioridade'])
        print("Estado:", tarefa_encontrada['Estado'])
    else:
        print("Tarefa não encontrada.")

    # Removendo a primeira tarefa
    print("Removendo a terafa...")
    lista_tarefas.removerTarefa(tarefa1, "user1@example.com")

    # Buscando a tarefa removida
    tarefa_removida = lista_tarefas.buscarTarefa("user1@example.com", "Fazer compras")
    if tarefa_removida:
        print("Tarefa encontrada após remoção:", tarefa_removida.getTitulo())
    else:
        print("Tarefa não encontrada após remoção.")

if __name__ == "__main__":
    main()