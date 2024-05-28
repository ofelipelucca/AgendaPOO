from Implementações.Lembrete import Lembrete, ListaLembrete

def main():
    # Criar instância de ListaLembrete
    lista_lembretes = ListaLembrete()
    
    # Criar instância de Lembrete
    lembrete1 = Lembrete("27/05/2024", "Reunião importante", "15:30:00")
    lembrete2 = Lembrete("28/05/2024", "Consulta médica", "10:00:00")
    
    # Adicionar lembretes à lista
    user_email1 = "usuario1@example.com"
    user_email2 = "usuario2@example.com"
    lista_lembretes.adicionarLembrete(lembrete1, user_email1)
    lista_lembretes.adicionarLembrete(lembrete2, user_email2)
    
    # Verificar se os lembretes foram adicionados
    assert lista_lembretes.tamanho() == 2
    
    # Buscar lembrete por mensagem
    lembrete_encontrado = lista_lembretes.buscarLembrete("Reunião importante")
    assert lembrete_encontrado.getMensagem() == "Reunião importante"
    
    # Testar métodos de Lembrete
    print(lembrete1.getData())  # Deve imprimir "27/05/2024"
    print(lembrete1.getHorario())  # Deve imprimir "15:30:00"
    print(lembrete1.getMensagem())  # Deve imprimir "Reunião importante"
    
    lembrete1.setData("29/05/2024")  # Deve atualizar a data
    print(lembrete1.getData())  # Deve imprimir "29/05/2024"
    
    lembrete1.setHorario("16:00:00")  # Deve atualizar o horário
    print(lembrete1.getHorario())  # Deve imprimir "16:00:00"
    
    lembrete1.setMensagem("Reunião com o cliente")  # Deve atualizar a mensagem
    print(lembrete1.getMensagem())  # Deve imprimir "Reunião com o cliente"
    
    # Remover lembrete da lista
    lista_lembretes.removerLembrete(lembrete1, user_email1)
    assert lista_lembretes.tamanho() == 1
    
    print("Todos os testes foram concluídos com sucesso!")

if __name__ == "__main__":
    main()