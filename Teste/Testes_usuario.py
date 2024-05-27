from Implementações import Usuario
def main():
    # Criar instância de ListaUsuario
    lista_usuarios = ListaUsuario()
    
    # Criar instância de Usuario
    usuario1 = Usuario("João", "Silva", "123456", "joao@gmail.com")
    usuario2 = Usuario("Maria", "Santos", "654321", "maria@yahoo.com")
    
    # Adicionar usuários à lista
    lista_usuarios.adicionarUsuario(usuario1)
    lista_usuarios.adicionarUsuario(usuario2)
    
    # Verificar se os usuários foram adicionados
    assert lista_usuarios.checkUsuario("joao@gmail.com", "João Silva") == True
    assert lista_usuarios.checkUsuario("maria@yahoo.com", "Maria Santos") == True
    assert lista_usuarios.checkUsuario("inexistente@gmail.com") == False
    
    # Testar métodos de Usuario
    print(usuario1.getNome())  # Deve imprimir "João Silva"
    print(usuario1.getEmail())  # Deve imprimir "joao@gmail.com"
    usuario1.setNome("Carlos", "Oliveira")
    print(usuario1.getNome())  # Deve imprimir "Carlos Oliveira"
    
    usuario1.setEmail("carlos@outlook.com")  # Deve imprimir "Email atualizado com sucesso"
    print(usuario1.getEmail())  # Deve imprimir "carlos@outlook.com"
    
    usuario1.setSenha("123123")
    assert usuario1.checkSenha("123123") == True  # Deve imprimir "Senha correta"
    assert usuario1.checkSenha("123456") == False  # Deve imprimir "Senha incorreta"
    
    # Remover usuário da lista
    lista_usuarios.removerUsuario(usuario1)
    assert lista_usuarios.checkUsuario("carlos@outlook.com") == False

    print("Todos os testes foram concluídos com sucesso!")

if __name__ == "__main__":
    main()