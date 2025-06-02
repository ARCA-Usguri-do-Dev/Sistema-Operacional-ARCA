"""
Módulo de Gerenciamento de Alertas

Este módulo contém as funções necessárias para gerenciar alertas do sistema ARCA,
incluindo:
- Geração automática de alertas baseados em condições climáticas
- Visualização de alertas por região
- Registro de alertas no histórico
"""

from datetime import datetime
from geolocalizacao import obter_regiao
from api_clima import obter_temperatura
from historico_alertas import registrar_alerta
from utils import data_atual_formatada
import random


def gerar_alertas_automaticos(lat, lon, cidade, estado, bairro, rua):
    """
    Gera alertas automáticos baseados nas condições climáticas da região.
    
    Args:
        lat (float): Latitude da localização
        lon (float): Longitude da localização
        cidade (str): Nome da cidade
        estado (str): Nome do estado
        bairro (str): Nome do bairro
        rua (str): Nome da rua
        
    Returns:
        list: Lista de dicionários contendo os alertas gerados. Cada alerta contém:
            - id: Identificador único do alerta
            - tipo: Tipo do alerta (Calor extremo, Chuvas intensas, etc)
            - nivel: Nível de severidade (Informativo, Atenção, Alerta Máximo)
            - descricao: Descrição detalhada do alerta
            - data_emissao: Data e hora de emissão do alerta
            - bairro: Bairro afetado
            - cidade: Cidade afetada
    """
    temperatura, chuva, chuva_acumulada, condicao, velocidade_vento, rajadas_vento = obter_temperatura(lat, lon)
    dt_atual = data_atual_formatada()

    alertas = []

    # Alerta de calor extremo
    if temperatura >= 32:
        alertas.append({
            'id': 1001,
            'tipo': 'Calor extremo',
            'nivel': 'Informativo' if temperatura < 36 else 'Alerta Máximo',
            'descricao': f'Temperatura de {temperatura} °C detectada na sua região.',
            'data_emissao': dt_atual,
            'bairro': bairro,
            'cidade': cidade
        })

    # Alerta de chuvas intensas
    if chuva >= 70:
        alertas.append({
            'id': 1002,
            'tipo': 'Chuvas intensas',
            'nivel': 'Atenção' if chuva < 90 else 'Alerta Máximo',
            'descricao': f'Previsão de {chuva}% de chance de chuva nas próximas horas.',
            'data_emissao': dt_atual,
            'bairro': bairro,
            'cidade': cidade
        })

    # Alerta de tempestade
    if condicao in ['Tempestade', 'Chuva forte']:
        alertas.append({
            'id': 1003,
            'tipo': 'Tempestade',
            'nivel': 'Alerta Máximo',
            'descricao': f'Condição atual: {condicao}. Risco de raios e ventos fortes.',
            'data_emissao': dt_atual,
            'bairro': bairro,
            'cidade': cidade
        })

    # Alerta de risco de enchente
    if chuva_acumulada >= 30:
        alertas.append({
            'id': 1004,
            'tipo': 'Risco de enchente',
            'nivel': 'Atenção' if chuva_acumulada < 50 else 'Alerta Máximo',
            'descricao': f'Previsão de {chuva_acumulada} mm de chuva acumulada nas próximas 24h.',
            'data_emissao': dt_atual,
            'bairro': bairro,
            'cidade': cidade
        })

    # Alerta de ventos fortes
    if velocidade_vento >= 30:
        alertas.append({
            'id': 1005,
            'tipo': 'Ventos fortes',
            'nivel': 'Atenção' if velocidade_vento < 50 else 'Alerta Máximo',
            'descricao': f'Velocidade do vento de {velocidade_vento} km/h detectada. Mantenha-se em local seguro.',
            'data_emissao': dt_atual,
            'bairro': bairro,
            'cidade': cidade
        })

    # Alerta de rajadas de vento
    if rajadas_vento >= 50:
        alertas.append({
            'id': 1006,
            'tipo': 'Rajadas de vento',
            'nivel': 'Atenção' if rajadas_vento < 70 else 'Alerta Máximo',
            'descricao': f'Rajadas de vento de até {rajadas_vento} km/h. Evite áreas abertas e objetos soltos.',
            'data_emissao': dt_atual,
            'bairro': bairro,
            'cidade': cidade
        })

    return alertas

def gerar_alertas_simulados(lat, lon, cidade, estado, bairro, rua):
    """
    Gera alertas simulados para fins de demonstração.
    
    Args:
        lat (float): Latitude da localização
        lon (float): Longitude da localização
        cidade (str): Nome da cidade
        estado (str): Nome do estado
        bairro (str): Nome do bairro
        rua (str): Nome da rua
        
    Returns:
        list: Lista de dicionários contendo os alertas simulados
    """
    dt_atual = data_atual_formatada()
    
    # Lista de alertas simulados
    alertas_simulados = [
        {
            'id': 1001,
            'tipo': 'Calor extremo',
            'nivel': 'Alerta Máximo',
            'descricao': f'Temperatura de 38°C detectada na sua região. Risco de desidratação e insolação.',
            'data_emissao': dt_atual,
            'bairro': bairro,
            'cidade': cidade
        },
        {
            'id': 1002,
            'tipo': 'Chuvas intensas',
            'nivel': 'Atenção',
            'descricao': f'Previsão de 85% de chance de chuva nas próximas horas. Mantenha-se em local seguro.',
            'data_emissao': dt_atual,
            'bairro': bairro,
            'cidade': cidade
        },
        {
            'id': 1003,
            'tipo': 'Tempestade',
            'nivel': 'Alerta Máximo',
            'descricao': f'Condição atual: Tempestade. Risco de raios e ventos fortes. Evite áreas abertas.',
            'data_emissao': dt_atual,
            'bairro': bairro,
            'cidade': cidade
        },
        {
            'id': 1004,
            'tipo': 'Risco de enchente',
            'nivel': 'Atenção',
            'descricao': f'Previsão de 45mm de chuva acumulada nas próximas 24h. Evite áreas baixas.',
            'data_emissao': dt_atual,
            'bairro': bairro,
            'cidade': cidade
        },
        {
            'id': 1005,
            'tipo': 'Ventos fortes',
            'nivel': 'Alerta Máximo',
            'descricao': f'Velocidade do vento de 45 km/h detectada. Mantenha-se em local seguro.',
            'data_emissao': dt_atual,
            'bairro': bairro,
            'cidade': cidade
        },
        {
            'id': 1006,
            'tipo': 'Rajadas de vento',
            'nivel': 'Alerta Máximo',
            'descricao': f'Rajadas de vento de até 75 km/h. Evite áreas abertas e objetos soltos.',
            'data_emissao': dt_atual,
            'bairro': bairro,
            'cidade': cidade
        }
    ]
    
    return alertas_simulados

def menu_alertas(usuario_logado):
    """
    Exibe e gerencia o menu de alertas do sistema.
    
    Args:
        usuario_logado (dict): Dicionário contendo os dados do usuário atualmente logado,
                             incluindo latitude e longitude
        
    Returns:
        None: A função apenas exibe as informações na tela e registra os alertas
    """
    lat = usuario_logado['lat']
    lon = usuario_logado['lon']
    rua, bairro, cidade, estado, pais = obter_regiao(lat, lon)
    
    print("\nEscolha o tipo de alertas:")
    print("1 - Alertas em tempo real")
    print("2 - Alertas simulados (para demonstração)")
    
    while True:
        try:
            opcao = int(input("\nDigite sua opção (1 ou 2): "))
            if opcao in [1, 2]:
                break
            print("Opção inválida! Digite 1 ou 2.")
        except ValueError:
            print("Por favor, digite um número válido.")
    
    # Escolhe entre alertas reais ou simulados
    if opcao == 1:
        alertas = gerar_alertas_automaticos(lat, lon, cidade, estado, bairro, rua)
        print(f"\nBuscando alertas reais para {bairro}, {cidade}...\n")
    else:
        alertas = gerar_alertas_simulados(lat, lon, cidade, estado, bairro, rua)
        print(f"\nExibindo alertas simulados para {bairro}, {cidade}...\n")

    if not alertas:
        print("Nenhum alerta para sua região.")
        return
    
    alerta_aleatorio = random.choice(alertas)
    if alerta_aleatorio["cidade"].lower() == cidade.lower():
        if alerta_aleatorio["bairro"] == "" or alerta_aleatorio["bairro"].lower() == bairro.lower():
            print(f"Emitido em: {alerta_aleatorio['data_emissao']}")
            print(f"⚠️ {alerta_aleatorio['tipo']} - {alerta_aleatorio['nivel']}")
            print(f"Local: {alerta_aleatorio['bairro']}, {alerta_aleatorio['cidade']}")
            print(f"{alerta_aleatorio['descricao']}\n")
            registrar_alerta(alerta_aleatorio)