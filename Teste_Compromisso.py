from src.Implementações.Compromisso.Compromisso import Compromisso
from src.Implementações.Compromisso.ListaCompromisso import ListaCompromisso

def main():
    # Criando uma lista de compromissos
    lista_compromissos = ListaCompromisso()

    # Criando um compromisso
    print("Criando um compromisso...")
    compromisso1 = Compromisso("Reunião", "Reunião sobre o projeto X", "15/06/2024", 2, "não feito", "laranja", "Escritório", "09:00:00")

    # Adicionando o compromisso à lista
    print("Adicionando um compromisso no banco de dados...")
    lista_compromissos.adicionarCompromisso(compromisso1, "user1@example.com")

    # Buscando o compromisso pelo título
    print("Buscando pelo compromisso no banco de dados...")
    compromisso_encontrado = lista_compromissos.buscarCompromisso("user1@example.com", "Reunião")
    if compromisso_encontrado:
        print("Compromisso encontrado:")
        print("Título:", compromisso_encontrado['Título'])
        print("Descrição:", compromisso_encontrado['Descrição'])
        print("Data:", compromisso_encontrado['Data'])
        print("Prioridade:", compromisso_encontrado['Prioridade'])
        print("Estado:", compromisso_encontrado['Estado'])
        print("Cor:", compromisso_encontrado['Cor'])
        print("Local:", compromisso_encontrado['Local'])
        print("Horário:", compromisso_encontrado['Horário'])
    else:
        print("Compromisso não encontrado.")

    # Removendo o compromisso
    print("Removendo o compromisso...")
    lista_compromissos.removerCompromisso(compromisso1, "user1@example.com")

    # Buscando o compromisso removido
    compromisso_removido = lista_compromissos.buscarCompromisso("user1@example.com", "Reunião")

    if compromisso_removido:
        print("Compromisso encontrado após remoção:", compromisso_removido.getTitulo())
    else:
        print("Compromisso não encontrado após remoção.")

if __name__ == "__main__":
    main()