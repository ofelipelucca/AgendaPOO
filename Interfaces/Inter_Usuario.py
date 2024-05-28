from abc import ABC, abstractmethod

class Inter_Usuario(ABC):
    
    @abstractmethod
    # @brief Busca pelo nome do usuario 
    #
    # @return String do nome
    def getNome(self,) -> str:
        pass
   
    @abstractmethod
    # @brief Busca pelo email do usuario 
    #
    # @return String do email
    def getEmail(self,) -> str:
        pass
    
    @abstractmethod
    # @brief Busca pela senha do usuario 
    #
    # @return String da senha
    def getSenha(self,) -> str:
        pass

    @abstractmethod
    # @brief Muda o nome e sobrenome de um usuario
    #
    # @param nome O nome do usuario 
    #
    # @param sobrenome O sobrenome do usuario 
    def setNome(self, novo_nome: str, novo_sobrenome: str):
        pass
    
    @abstractmethod
    # @brief Muda o email de um usuario
    #
    # @param novo_email O email a ser alterado
    def setEmail(self, novo_email: str):
        pass

    @abstractmethod
    # @brief Muda a senha de um usuario
    #
    # @param nova_senha A senha a ser alterada
    def setSenha(self, nova_senha: str):
        pass
    
    @abstractmethod
    # @brief Checa se a senha está correta
    #
    # @param senha_informada senha fornecida pelo usuario
    def checkSenha(self, senha_informada: str) -> bool:
        pass
    
class Inter_ListadeUsuario(ABC):
    @abstractmethod
    # @brief Adiciona um Usuario a lista de Usuarios
    #
    # @param usuario O Usuario a ser adicionado
    def adicionarUsuario(self, usuario: Inter_Usuario):
        pass
        
    @abstractmethod
    # @brief Remove um Usuario da lista de Usuarios
    #
    # @param usuario O Usuario a ser removido
    def removerUsuario(self, usuario: Inter_Usuario):
        pass
    
    @abstractmethod
    # @brief Verifica se o email e o nome fornecidos correpondem na lista
    #
    # @param email O email fornecido
    #
    # @param nome O nome fornecido 
    #
    # @return True se o nome e o email correpondem, false caso contrario
    def checkUsuario(self, email: str, nome: str) -> bool:
        pass