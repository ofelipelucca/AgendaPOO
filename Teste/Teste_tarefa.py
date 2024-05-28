from Implementações.Tarefa.Tarefa import Tarefa
from Implementações.Tarefa.ListaTarefa import ListaTarefa

# Criando instância de ListaTarefa
lista_tarefas = ListaTarefa()

# Criando algumas tarefas de exemplo
tarefa1 = Tarefa("Fazer compras", "Comprar pão e leite", "24/05/2024", 1, "em progresso")
tarefa2 = Tarefa("Estudar", "Estudar para o exame de matemática", "26/05/2024", 1, "em progresso")

# Adicionando tarefas
lista_tarefas.adicionarTarefa(tarefa1, "lipe@example.com")
lista_tarefas.adicionarTarefa(tarefa2, "lipe@example.com")

# Testando adicionar tarefa repetida
lista_tarefas.adicionarTarefa(tarefa1, "lipe@example.com")

for usuario in lista_tarefas._listadetarefa:
    for tarefa in lista_tarefas._listadetarefa[usuario]:
        print(tarefa._titulo, usuario)

# Removendo tarefa
lista_tarefas.removerTarefa(tarefa1, "lipe@example.com")

# Tentando remover tarefa que não existe
lista_tarefas.removerTarefa(tarefa1, "lipe@example.com")

# Tentando remover tarefa de usuário que não possui tarefas
lista_tarefas.removerTarefa(tarefa2, "lip@example.com")

lista_tarefas.adicionarTarefa(tarefa1, "lipe@example.com")

# Buscando tarefa pelo título
tarefa_encontrada = lista_tarefas.buscarTarefa("Fazer compras")
if tarefa_encontrada:
    print("Tarefa encontrada:", tarefa_encontrada.getDescricao())
else:
    print("Tarefa não encontrada.")
