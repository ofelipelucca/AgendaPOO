from Implementações.Nitificações import Notificação
from Implementações.Tarefa.Tarefa import Compromisso
from Implementações.Lembrete import Lembrete
def main():
    # Criar instâncias de Compromisso e Lembrete
    compromisso = Compromisso("Reunião de projeto", "Discussão sobre o projeto", "25/12/2024", 1, "em progresso", "azul", "Sala de Reunião", "14:30:00")
    lembrete = Lembrete("25/12/2024", "Comprar presente", "16:00:00")

    # Criar instância de Notificacao
    notificacao = Notificação(minutos=30, horas=1)

    # Ativar notificação
    notificacao.ativarNotificacao()

    # Verificar estado da notificação
    estado = notificacao.checkEstado()
    print("Estado da notificação:", "Ativada" if estado else "Desativada")

    # Tentar notificar compromisso e lembrete
    notificacao.notificar(compromisso)
    notificacao.notificar(lembrete)

    # Desativar notificação
    notificacao.desativarNotificacao()

if __name__ == "__main__":
    main()