from src.Implementações.Usuario.Usuario import Usuario, ListaUsuario

def main():
    # Cria instâncias de Usuario
    user1 = Usuario("Felipe", "Silva", "exemploF@gmail.com", "123456")

    user2 = Usuario("Maria", "Ferreira", "mariaF@yahoo.com","654321")

    # Cria uma instância de ListaUsuario e adiciona os usuários
    lista_usuarios = ListaUsuario()
    lista_usuarios.adicionarUsuario(user1)
    lista_usuarios.adicionarUsuario(user2)

    # Testa os métodos getNome, getEmail e getSenha
    print(f"Nome do user1: {user1.getNomeCompleto()}")
    print(f"Email do user1: {user1.getEmail()}")
    print(f"Senha do user1: {user1.getSenha()}")

    # Testa o método checkLogin
    print(f"Check senha user1 (123456): {lista_usuarios.checkLogin("exemploF@gmail.com", '123456')}")
    print(f"Check senha user1 (000000): {lista_usuarios.checkLogin("exemploF@gmail.co", '000000')}")

    # Testa o método checkUsuario na lista de usuários
    print(f"Check usuario (exemploF@gmail.com, Felipe Silva): {lista_usuarios.checkUsuario('exemploF@gmail.com', 'Felipe Silva')}")
    print(f"Check usuario (mariaF@yahoo.com, Maria Ferreira): {lista_usuarios.checkUsuario('mariaF@yahoo.com', 'Maria Ferreira')}")

    # Testa a mudança de nome, email e senha
    user1.setNome("Carlos", "Souza")
    print(f"Nome atualizado do user1: {user1.getNomeCompleto()}")

    user1.setEmail("carlos@outlook.com")
    print(f"Email atualizado do user1: {user1.getEmail()}")

    user1.setSenha("111222")
    print(f"Senha atualizada do user1: {user1.getSenha()}")
    
if __name__ == "__main__":
    main()