"""
Sistema ARCA - Sistema de Gerenciamento de Alertas e Recursos de Apoio

Este módulo contém a interface principal do sistema ARCA, que gerencia usuários,
alertas, pontos de apoio, histórico de alertas e calculadora de hidratação.

Módulos importados:
- usuarios: Gerenciamento de usuários e perfis
- alertas: Sistema de alertas e notificações
- pontos_apoio: Gerenciamento de pontos de apoio
- historico_alertas: Registro e consulta de histórico de alertas
- hidratar: Calculadora de hidratação
- utils: Funções utilitárias
"""

from usuarios import menu_usuarios, selecionar_usuario
from alertas import menu_alertas
from pontos_apoio import menu_pontos_apoio
from historico_alertas import menu_historico_alertas
from hidratar import menu_calculadora_hidratacao
from utils import limpar_console
import random
from usuarios import usuarios

# Inicializa com um usuário aleatório
usuario_logado = random.choice(usuarios)

def trocar_usuario():
    """
    Permite trocar o usuário atualmente logado no sistema.
    
    Returns:
        None: A função modifica a variável global usuario_logado
    """
    global usuario_logado
    usuario_logado = selecionar_usuario()

def menu_main():
    """
    Exibe e gerencia o menu principal do sistema ARCA.
    
    O menu oferece as seguintes opções:
    1. Gerenciamento de Usuários
    2. Sistema de Alertas
    3. Pontos de Apoio
    4. Histórico de Alertas
    5. Calculadora de Hidratação
    0. Sair do Sistema
    
    Returns:
        None
    """
    global usuario_logado
    while True:
        if usuario_logado:
            print(f"\n👤 Usuário logado: {usuario_logado['nome']} ({usuario_logado['perfil']})")
        else:
            print("\n⚠️ Nenhum usuário logado.")

        print("\n~~~~ Sistema ARCA - Menu Principal ~~~~")
        print('1 - Usuário')
        print('2 - Alertas')
        print('3 - Pontos de Apoio')
        print('4 - Histórico de Alertas')
        print('5 - Calculadora de Hidratação')
        print('0 - Sair')

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            novo_usuario = menu_usuarios(usuario_logado)
            if novo_usuario:
                usuario_logado = novo_usuario
        elif opcao == '2':
            if usuario_logado:
                menu_alertas(usuario_logado)
            else:
                print("⚠️  Você precisa selecionar um usuário primeiro.")
        elif opcao == '3':
            if usuario_logado:
                menu_pontos_apoio(usuario_logado)
            else:
                print("⚠️  Você precisa selecionar um usuário primeiro.")
        elif opcao == '4':
            if usuario_logado:
                menu_historico_alertas(usuario_logado)
            else:
                print("⚠️  Você precisa selecionar um usuário primeiro.")
        elif opcao == '5':
            if usuario_logado:
                menu_calculadora_hidratacao(usuario_logado)
            else:
                print("⚠️  Você precisa selecionar um usuário primeiro.")
        elif opcao == '0':
            print("\nSaindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

    print("\nSistema finalizado com sucesso.\n")

if __name__ == "__main__":
    limpar_console()
    menu_main()
