from Implementações.Nitificações import Notificação
from Implementações.Tarefa.Tarefa import Compromisso
from Implementações.Lembrete import Lembrete
def main():
    # Criar instâncias de Compromisso e Lembrete
    compromisso = Compromisso("Reunião de projeto", "14:30")
    lembrete = Lembrete("Comprar presente", "16:00")

    # Criar instância de Notificacao
    notificacao = Notificação(hora_antes=1, min_antes=0)

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