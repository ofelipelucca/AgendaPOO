from src.Implementações.Notificações import Notificação
from src.Implementações.Compromisso.Compromisso import Compromisso
from src.Implementações.Lembrete.Lembrete import Lembrete

def main():
    # Criação de uma instância de Notificação
    notificacao = Notificação(17, 58)

    # Testando getMinAntes e setMinAntes
    notificacao.setMinAntes(15)
    assert notificacao.getMinAntes() == 15, "Erro no set/get de MinAntes"

    # Testando getHorasAntes e setHorasAntes
    notificacao.setHorasAntes(2)
    assert notificacao.getHorasAntes() == 2, "Erro no set/get de HorasAntes"

    # Testando ativarNotificacao e checkEstado
    notificacao.ativarNotificacao()
    assert notificacao.checkEstado() == True, "Erro na ativação de notificação"

    # Testando desativarNotificacao e checkEstado
    notificacao.desativarNotificacao()
    assert notificacao.checkEstado() == False, "Erro na desativação de notificação"
    
    # Preparando um compromisso para teste de notificação
    compromisso = Compromisso("Reunião", "Reunião sobre o projeto X", "15/06/2024", 2, "não feito", "laranja", "Escritório", "09:00:00")


    # Testando notificar (considerando o tempo atual para fins de demonstração)
    # Devemos ativar a notificação para testar corretamente
    notificacao.ativarNotificacao()

    # Teste com a hora e minuto atuais
    notificacao.setHorasAntes(0)
    notificacao.setMinAntes(0)
    notificacao.notificar(compromisso)

    # Testando notificar (considerando o tempo atual para fins de demonstração)
    # Devemos ativar a notificação para testar corretamente
    notificacao.ativarNotificacao()


    # Preparando um lembrete para teste de notificação
    lembrete = Lembrete("17/06/2024", "16:00:00", "Fazer nada")

    # Teste com a hora e minuto atuais
    notificacao.setHorasAntes(0)
    notificacao.setMinAntes(0)
    notificacao.notificar(lembrete)

    print("Todos os testes foram concluídos com sucesso.")

if __name__ == "__main__":
    main()