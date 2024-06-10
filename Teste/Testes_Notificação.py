from Implementações.Notificações import Notificação
from Implementações.Tarefa.Tarefa import Compromisso
from Implementações.Lembrete import Lembrete

def main():
    # Criação de uma instância de Notificação
    notificacao = Notificação()

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
    compromisso = Compromisso("Reunião de trabalho", "Reunião sobre o projeto X", "15/06/2024", 2, "não feito")
    compromisso.setCor("laranja")
    compromisso.setLocal("Escritório")
    compromisso.setHorario("09:00:00")


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
    lembrete = Lembrete()
    lembrete.setData("17/06/2024")
    lembrete.setHorario("16:00:00")
    lembrete.setMensagem("Fazer nada")

    # Teste com a hora e minuto atuais
    notificacao.setHorasAntes(0)
    notificacao.setMinAntes(0)
    notificacao.notificar(lembrete)

    print("Todos os testes foram concluídos com sucesso.")

if __name__ == "__main__":
    main()