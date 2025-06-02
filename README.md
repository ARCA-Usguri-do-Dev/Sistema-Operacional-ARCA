# Sistema ARCA - Sistema de Gerenciamento de Alertas e Recursos de Apoio

O Sistema ARCA é uma aplicação Python que gerencia alertas e recursos de apoio baseados em condições climáticas e localização. O sistema oferece funcionalidades para monitoramento de condições meteorológicas, geração de alertas, gerenciamento de pontos de apoio e cálculo de hidratação.

## Funcionalidades

### 1. Gerenciamento de Usuários

- Cadastro e autenticação de usuários
- Diferentes níveis de acesso (Administrador e Usuário)
- Perfis personalizados com localização geográfica
- Edição de dados do usuário

### 2. Sistema de Alertas

- **Alertas em Tempo Real**

  - Monitoramento contínuo das condições climáticas
  - Alertas baseados em dados reais do INMET
  - Múltiplos tipos de alertas:
    - Calor extremo (≥32°C)
    - Chuvas intensas (≥70% de probabilidade)
    - Tempestades
    - Risco de enchente (≥30mm de chuva acumulada)
    - Ventos fortes (≥30km/h)
    - Rajadas de vento (≥50km/h)
  - Níveis de severidade: Informativo, Atenção e Alerta Máximo

- **Alertas Simulados**
  - Modo de demonstração para testes
  - Simulação de condições climáticas extremas
  - Útil para treinamento e validação do sistema

### 3. Pontos de Apoio

- Cadastro de locais seguros
- Geolocalização precisa
- Status de disponibilidade
- Capacidade de atendimento
- Restrição de acesso por perfil de usuário

### 4. Histórico de Alertas

- Registro completo de todos os alertas
- Filtragem por região
- Diferentes níveis de acesso ao histórico
- Data e hora de emissão
- Detalhes completos das condições

### 5. Calculadora de Hidratação

- Cálculo personalizado baseado em:
  - Peso corporal do usuário
  - Temperatura atual da região
- Ajustes automáticos por temperatura:
  - +1.0 litro se temperatura ≥ 32°C
  - +0.5 litro se temperatura ≥ 28°C
- Base de cálculo: 35ml por kg de peso

## Requisitos

- Python 3.8+
- Conexão com internet para dados climáticos
- Acesso à API de geolocalização

## Instalação

1. Clone o repositório
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

Execute o arquivo principal:

```bash
python main.py
```

## Estrutura do Projeto

- `main.py`: Arquivo principal do sistema
- `usuarios.py`: Gerenciamento de usuários
- `alertas.py`: Sistema de alertas
- `api_clima.py`: Integração com API de clima
- `pontos_apoio.py`: Gerenciamento de pontos de apoio
- `historico_alertas.py`: Histórico de alertas
- `geolocalizacao.py`: Integração com API de geolocalização
- `hidratar.py`: Calculadora de hidratação
- `utils.py`: Funções utilitárias

## Contato

| Nome                           | GitHub                                        | LinkedIn                                                                |
| ------------------------------ | --------------------------------------------- | ----------------------------------------------------------------------- |
| Alexander Dennis Isidro Mamani | [alex-isidro](https://github.com/alex-isidro) | [LinkedIn](https://www.linkedin.com/in/alexander-dennis-a3b48824b/)     |
| Kelson Zhang                   | [KelsonZh0](https://github.com/KelsonZh0)     | [LinkedIn](https://www.linkedin.com/in/kelson-zhang-211456323/)         |
| Lucas Rossoni Dieder           | [PxS00](https://github.com/PxS00)             | [LinkedIn](https://www.linkedin.com/in/lucas-rossoni-dieder-32242a353/) |
