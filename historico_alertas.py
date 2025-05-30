"""
Módulo de Histórico de Alertas

Este módulo gerencia o histórico de alertas do sistema ARCA, incluindo:
- Registro de novos alertas
- Verificação de alertas duplicados
- Visualização do histórico de alertas
"""

# Lista que armazena o histórico de alertas
historico_alertas = []

def registrar_alerta(alerta):
    """
    Registra um novo alerta no histórico, evitando duplicatas.
    
    Args:
        alerta (dict): Dicionário contendo os dados do alerta a ser registrado
            - id: Identificador único do alerta
            - tipo: Tipo do alerta
            - nivel: Nível de severidade
            - descricao: Descrição do alerta
            - data_emissao: Data e hora de emissão
            - bairro: Bairro afetado
            - cidade: Cidade afetada
    
    Returns:
        None: A função apenas adiciona o alerta à lista historico_alertas
    """
    if not alerta_ja_registrado(alerta):
        historico_alertas.append(alerta)

def alerta_ja_registrado(alerta):
    """
    Verifica se um alerta já está registrado no histórico.
    
    Args:
        alerta (dict): Dicionário contendo os dados do alerta a ser verificado
        
    Returns:
        bool: True se o alerta já estiver registrado, False caso contrário
    """
    for alerta_existente in historico_alertas:
        if alerta_existente['id'] == alerta['id']:
            return True
    return False

def menu_historico_alertas():
    """
    Exibe o histórico de alertas registrados no sistema.
    
    Returns:
        None: A função apenas exibe as informações na tela
    """
    print('\n~~~~ Histórico de Alertas ~~~~')
    if not historico_alertas:
        print('Nenhum alerta registrado.')
        return
        
    for alerta in historico_alertas:
        print(f'Emitido em: {alerta["data_emissao"]}')
        print(f'Tipo: {alerta["tipo"]} - Nível: {alerta["nivel"]}')
        print(f'Local: {alerta["bairro"]}, {alerta["cidade"]}')
        print(f'{alerta["descricao"]}\n')
