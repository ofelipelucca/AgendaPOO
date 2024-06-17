from src.Interfaces.Inter_Usuario import Inter_ListadeUsuario
from src.Implementações.Usuario import Usuario

import pandas as pd
from typing import Optional, Dict, Union

class ListaUsuario(Inter_ListadeUsuario):
    def __init__(self) -> None:
        self.__colunas = ['Email', 'Nome', 'Sobrenome', 'Senha']
        self.__nome_do_arquivo = "Planilha_de_usuarios.xlsx"

    # @brief Carrega a planilha do arquivo Excel dos usuários salvos
    #
    # @return A planilha caso exista, cria uma nova caso nao exista
    def _carregar_planilha(self) -> pd.DataFrame:
        try:
            return pd.read_excel(self.__nome_do_arquivo)
        except FileNotFoundError:
            return pd.DataFrame(columns=self.__colunas)

    # @brief Adiciona um novo usuário ao banco de dados
    #
    # @param usuario O usuário a ser adicionado
    def adicionarUsuario(self, usuario: Usuario) -> None:
        planilha = self._carregar_planilha()
            
        if self.checkUsuario(usuario.getEmail()):
            raise ValueError(f"O usuário {usuario.getEmail()} já está cadastrado.")

        novo_usuario = {
            'Email': usuario.getEmail(),
            'Nome': usuario.getNome(),
            'Sobrenome': usuario.getSobrenome(),
            'Senha': usuario.getSenha()
        }

        novo_usuario_df = pd.DataFrame([novo_usuario])

        planilha = pd.concat([planilha, novo_usuario_df], ignore_index=True)
        planilha = planilha.drop_duplicates()
        planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')

    # @brief Remove um usuário do banco de dados
    #
    # @param usuario O usuário a ser removido
    #
    # @return Retorna True se o usuário foi removido com sucesso
    def removerUsuario(self, usuario: Usuario) -> bool:
        planilha = self._carregar_planilha()

        if usuario.getEmail() in planilha['Email'].values:
            planilha = planilha[planilha['Email'] != usuario.getEmail()]
            planilha.to_excel(self.__nome_do_arquivo, index=False, engine='openpyxl')
            return True
        
        raise ValueError(f"Usuário {usuario.getEmail()} não encontrado.")

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
        planilha = self._carregar_planilha()

        if nome is None:
            return email in planilha['Email'].values
        else:
            return any((planilha['Email'] == email) & (planilha['Nome'] == nome))
        
    # @brief Verifica se o email e senha fornecidos batem no banco de dados
    #
    # @param email O email fornecido
    #
    # @param senha_inserida A senha fornecida
    #
    # @return True se o email e senha verificam, False caso contrário
    def checkLogin(self, email: str, senha_inserida: str) -> bool:
        planilha = self._carregar_planilha()

        if email in planilha['Email'].values:
            senha_armazenada = planilha.loc[planilha['Email'] == email, 'Senha'].values[0]
            return senha_inserida == str(senha_armazenada).rstrip('.0')
        return False
    
    # @brief Retorna um dicionário com todos os dados do usuário baseado no email
    #
    # @param email O email do usuário
    #
    # @return Um dicionário com 'Nome', 'Sobrenome', 'Email' e 'Senha' se o usuário existir, None caso contrário
    def obterUsuario(self, email: str) -> Optional[Dict[str, Union[str, int]]]:
        planilha = self._carregar_planilha()

        if email in planilha['Email'].values:
            usuario = planilha[planilha['Email'] == email].iloc[0]
            return {
                'Nome': usuario['Nome'],
                'Sobrenome': usuario['Sobrenome'],
                'Email': usuario['Email'],
                'Senha': usuario['Senha']
            }
        
        return None