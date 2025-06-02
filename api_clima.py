"""
Módulo de Integração com API de Clima

Este módulo contém funções para obter informações meteorológicas utilizando
a API Open-Meteo, incluindo:
- Temperatura atual
- Probabilidade de chuva
- Precipitação acumulada
- Condições do tempo
"""

import requests

def obter_temperatura(lat, lon):
    """
    Obtém informações meteorológicas para uma localização específica.
    
    Args:
        lat (float): Latitude da localização
        lon (float): Longitude da localização
        
    Returns:
        tuple: Tupla contendo (temperatura, chuva_prob, chuva_acumulada, condicao)
            - temperatura (float): Temperatura atual em graus Celsius
            - chuva_prob (int): Probabilidade de chuva em porcentagem
            - chuva_acumulada (float): Precipitação acumulada em mm
            - condicao (str): Descrição das condições do tempo
            
        Em caso de erro, retorna valores padrão:
            (28.0, 0, 0, "Desconhecido")
    
    Raises:
        requests.RequestException: Se houver erro na requisição HTTP
    """
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current_weather=true"
        f"&hourly=precipitation_probability"
        f"&daily=precipitation_sum"
        f"&timezone=America%2FSao_Paulo"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta exceção para códigos de erro HTTP
        
        dados = response.json()

        temperatura = dados["current_weather"]["temperature"]
        weathercode = dados["current_weather"]["weathercode"]
        chuva_prob = dados["hourly"]["precipitation_probability"][0]
        chuva_acumulada = dados["daily"]["precipitation_sum"][0]
        condicao = interpretar_condicao_tempo(weathercode)

        return temperatura, chuva_prob, chuva_acumulada, condicao
        
    except requests.RequestException as e:
        print(f"⚠️ Erro na API Open-Meteo: {str(e)}")
        return 28.0, 0, 0, "Desconhecido"
    except Exception as e:
        print(f"⚠️ Erro ao conectar com API de clima: {str(e)}")
        return 28.0, 0, 0, "Desconhecido"

def interpretar_condicao_tempo(codigo):
    """
    Converte o código numérico da condição do tempo em uma descrição textual.
    
    Args:
        codigo (int): Código numérico da condição do tempo conforme API Open-Meteo
        
    Returns:
        str: Descrição textual da condição do tempo
            - Se o código não for reconhecido, retorna "Desconhecido"
    """
    mapa = {
        0: "Céu limpo",
        1: "Principalmente limpo",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Névoa",
        48: "Névoa com gelo",
        51: "Garoa leve",
        61: "Chuva leve",
        63: "Chuva moderada",
        65: "Chuva forte",
        80: "Chuva com pancadas",
        95: "Tempestade"
    }
    return mapa.get(codigo, "Desconhecido")