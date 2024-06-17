from abc import ABC, abstractmethod
import pandas as pd
from typing import Optional, Dict, Union

class Inter_Usuario(ABC):
    
    @abstractmethod
    # @brief Busca pelo nome do usuario 
    #
    # @return String do nome completo
    def getNomeCompleto(self) -> str:
        pass

    @abstractmethod
    # @brief Busca pelo nome do usuario 
    #
    # @return String do nome
    def getNome(self) -> str:
        pass

    @abstractmethod
    # @brief Busca pelo sobrenome do usuario 
    #
    # @return String do sobrenome
    def getSobrenome(self) -> str:
        pass
   
    @abstractmethod
    # @brief Busca pelo email do usuario 
    #
    # @return String do email
    def getEmail(self) -> str:
        pass
    
    @abstractmethod
    # @brief Busca pela senha do usuario 
    #
    # @return String da senha
    def getSenha(self) -> str:
        pass

    @abstractmethod
    # @brief Muda o nome e sobrenome de um usuario
    #
    # @param nome O nome do usuario 
    #
    # @param sobrenome O sobrenome do usuario 
    def setNome(self, novo_nome: str, novo_sobrenome: str) -> None:
        pass

    @abstractmethod
    # @brief Muda a senha de um usuario
    #
    # @param nova_senha A senha a ser alterada
    def setSenha(self, nova_senha: str) -> None:
        pass
    
    @abstractmethod
    # @brief Muda o email de um usuario
    #
    # @param novo_email O email a ser alterado
    def setEmail(self, novo_email: str) -> None:
        pass
    
class Inter_ListadeUsuario(ABC):
    @abstractmethod
    # @brief Carrega a planilha do arquivo Excel dos usuários salvos
    #
    # @return A planilha caso exista, cria uma nova caso nao exista
    def _carregar_planilha(self) -> pd.DataFrame:
        pass

    @abstractmethod
    # @brief Adiciona um Usuario a lista de Usuarios
    #
    # @param usuario O Usuario a ser adicionado
    def adicionarUsuario(self, usuario: Inter_Usuario) -> None:
        pass
        
    @abstractmethod
    # @brief Remove um usuário do banco de dados
    #
    # @param usuario O usuário a ser removido
    #
    # @return Retorna True se o usuário foi removido com sucesso
    def removerUsuario(self, usuario: Inter_Usuario) -> bool:
        pass
    
    @abstractmethod
    # @brief Verifica se um usuário existe no banco de dados com o email fornecido
    #
    # @optional Fazer verificação checkando se o email bate com o nome fornecido
    #
    # @param email O email do usuário
    #
    # @param nome (Optional) o nome do usuário
    #
    # @return True se o usuário existe, False caso contrário
    def checkUsuario(self, email: str, nome: Optional[str] = None) -> bool:
        pass
    
    @abstractmethod
    # @brief Verifica se o email e senha fornecidos batem no banco de dados
    #
    # @param email O email fornecido
    #
    # @param senha_inserida A senha fornecida
    #
    # @return True se o email e senha verificam, False caso contrário
    def checkLogin(self, email: str, senha_inserida: str) -> bool:
        pass

    @abstractmethod
    # @brief Retorna um dicionário com todos os dados do usuário baseado no email
    #
    # @param email O email do usuário
    #
    # @return Um dicionário com 'Nome', 'Sobrenome', 'Email' e 'Senha' se o usuário existir, None caso contrário
    def obterUsuario(self, email: str) -> Optional[Dict[str, Union[str, int]]]:
        pass