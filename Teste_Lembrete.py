from src.Implementações.Lembrete.Lembrete import Lembrete
from src.Implementações.Lembrete.ListaLembrete import ListaLembrete
from src.Implementações.Lembrete.ImprimirLembrete import ImprimirLembrete

def main():
    # Cria instâncias de Lembrete
    lembrete1 = Lembrete("25/12/2024", "12:00:00", "Almoço de Natal")

    lembrete2 = Lembrete("31/12/2024", "23:59:59", "Reveillon")

    # Cria uma instância de ListaLembrete e adiciona os lembretes
    lista_lembretes = ListaLembrete()
    lista_lembretes.adicionarLembrete(lembrete1, "user1@example.com")
    lista_lembretes.adicionarLembrete(lembrete2, "user2@example.com")

    # Cria uma instância de ImprimirLembrete
    imprimir_lembretes = ImprimirLembrete(lista_lembretes)

    # Imprime os lembretes
    print("Lembretes do user1:")
    imprimir_lembretes.verLembretes("user1@example.com")
    
    print("Lembretes do user2:")
    imprimir_lembretes.verLembretes("user2@example.com")

    # Testa o método buscarLembrete
    encontrado = lista_lembretes.buscarLembrete("Almoço de Natal")
    if encontrado:
        print("Lembrete encontrado: ", encontrado['Mensagem'][0])
    else:
        print("Lembrete não encontrado")

    # Testa a remoção de um lembrete
    lista_lembretes.removerLembrete(lembrete1, "user1@example.com")
    print("Lembretes do user1 após remoção:")
    imprimir_lembretes.verLembretes("user1@example.com")

if __name__ == "__main__":
    main()