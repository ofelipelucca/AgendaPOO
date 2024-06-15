from src.Implementações.Calendario.Calendario import Calendario
from datetime import datetime

def main():
    # Criando uma instância do Calendario
    meu_calendario = Calendario()

    # Inserindo algumas atividades
    meu_calendario.inserir("10:00", ["Estudar Python", "Fazer exercícios"])
    meu_calendario.inserir("20:00", ["Fazer trabalho de POO"])
    meu_calendario.inserir("13/06/2024")
    
    meu_calendario.inserir("15:30", ["Reunião", "Almoçar com amigos"])
    meu_calendario.inserir("14/06/2024")
    
    meu_calendario.inserir("16:00", ["Ir ao supermercado"])
    meu_calendario.inserir("16:00", ["Ler um livro"])
    meu_calendario.inserir("15/06/2024")
    
    meu_calendario.inserir("18:00", ["Assistir filme", "Jogar videogame"])
    meu_calendario.inserir("17/06/2024")
    
    meu_calendario.inserir("14:00", ["Limpar a casa", "Fazer compras"])
    meu_calendario.inserir("19/06/2024")

    # Ordenando a agenda
    meu_calendario.ordenarAgenda()

    # Imprimindo o calendário para os próximos 7 dias
    hoje = datetime.now().strftime("%d/%m/%Y")
    meu_calendario._imprimirCalendario(hoje)


if __name__ == "__main__":
    main()
