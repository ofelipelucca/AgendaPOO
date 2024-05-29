from Implementações.Calendario import Calendario
from datetime import datetime

def main():
    # Criando uma instância do Calendario
    meu_calendario = Calendario()

    # Inserindo algumas atividades
    meu_calendario.inserir("01/06/2024", ["Estudar Python", "Fazer exercícios"])
    meu_calendario.inserir("02/06/2024", ["Reunião", "Almoçar com amigos"])
    meu_calendario.inserir("03/06/2024", ["Ir ao supermercado", "Ler um livro"])
    meu_calendario.inserir("04/06/2024", ["Assistir filme", "Jogar videogame"])
    meu_calendario.inserir("05/06/2024", ["Limpar a casa", "Fazer compras"])

    # Ordenando a agenda
    meu_calendario.ordenarAgenda()

    # Imprimindo o calendário para os próximos 7 dias
    hoje = datetime.now().strftime("%d/%m/%Y")
    meu_calendario.imprimirCalendario(hoje)


if __name__ == "__main__":
    main()