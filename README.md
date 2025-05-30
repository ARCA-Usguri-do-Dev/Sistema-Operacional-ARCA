# Sistema ARCA - Sistema de Gerenciamento de Alertas e Recursos de Apoio

O Sistema ARCA é uma aplicação Python que gerencia alertas e recursos de apoio baseados em condições climáticas e localização. O sistema oferece funcionalidades para monitoramento de condições meteorológicas, geração de alertas, cálculo de hidratação e gerenciamento de pontos de apoio.

## Funcionalidades Principais

- **Gerenciamento de Usuários**

  - Cadastro e edição de perfis
  - Seleção de usuário ativo
  - Visualização de usuários conectados

- **Sistema de Alertas**

  - Alertas automáticos baseados em condições climáticas
  - Monitoramento de temperatura
  - Previsão de chuvas
  - Alertas de tempestade
  - Risco de enchente

- **Pontos de Apoio**

  - Localização de pontos de apoio próximos
  - Informações sobre recursos disponíveis

- **Histórico de Alertas**

  - Registro de alertas emitidos
  - Visualização do histórico por região

- **Calculadora de Hidratação**
  - Cálculo personalizado baseado no peso
  - Ajuste automático baseado na temperatura
  - Recomendações diárias

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python:
  - requests
  - datetime
  - os

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/sistema-arca.git
cd sistema-arca
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure as chaves de API:
   - Edite o arquivo `config.py` e adicione sua chave de API do OpenCage Geocoder

## Uso

Execute o arquivo principal:

```bash
python main.py
```

## Estrutura do Projeto

- `main.py`: Arquivo principal do sistema
- `usuarios.py`: Gerenciamento de usuários
- `alertas.py`: Sistema de alertas
- `pontos_apoio.py`: Gerenciamento de pontos de apoio
- `historico_alertas.py`: Histórico de alertas
- `hidratar.py`: Calculadora de hidratação
- `geolocalizacao.py`: Integração com API de geolocalização
- `api_clima.py`: Integração com API de clima
- `utils.py`: Funções utilitárias
- `config.py`: Configurações do sistema


## Contato

| Nome                           | GitHub                                         | LinkedIn                                                               |
| ------------------------------ | ------------------------------------------     | ---------------------------------------------------------------------- |
| Alexander Dennis Isidro Mamani | [alex-isidro](https://github.com/alex-isidro)  | [LinkedIn](https://www.linkedin.com/in/alexander-dennis-a3b48824b/)    |
| Kelson Zhang                   | [KelsonZh0](https://github.com/KelsonZh0)      | [LinkedIn](https://www.linkedin.com/in/kelson-zhang-211456323/)        |
| Lucas Rossoni Dieder           | [PxS00](https://github.com/PxS00)              | [LinkedIn](https://www.linkedin.com/in/lucas-rossoni-dieder-32242a353/)|