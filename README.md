# Sistema ARCA - Sistema de Gerenciamento de Alertas e Recursos de Apoio

O Sistema ARCA é uma aplicação Python que gerencia alertas e recursos de apoio baseados em condições climáticas e localização. O sistema oferece funcionalidades para monitoramento de condições meteorológicas, geração de alertas, gerenciamento de pontos de apoio e cálculo de hidratação.

## Objetivo

O Sistema ARCA tem como objetivo principal fornecer informações em tempo real sobre condições climáticas e disponibilizar recursos de apoio para a população em situações de risco. O sistema é especialmente útil para:

- Monitoramento de condições climáticas extremas
- Geração de alertas preventivos
- Identificação de locais seguros
- Recomendações de hidratação baseadas no clima

## Funcionalidades

### 1. Gerenciamento de Usuários

- **Cadastro e Autenticação**

  - Criação de perfis de usuário
  - Diferentes níveis de acesso (Administrador e Usuário)
  - Edição de dados pessoais
  - Troca de usuário durante a sessão

- **Perfis Personalizados**
  - Localização geográfica precisa
  - Dados pessoais (nome, idade, perfil)
  - Histórico de alertas personalizado

### 2. Sistema de Alertas

- **Alertas em Tempo Real**

  - Monitoramento contínuo das condições climáticas
  - Dados fornecidos pelo INMET (Instituto Nacional de Meteorologia)
  - Tipos de alertas:
    - Calor extremo (≥32°C)
    - Chuvas intensas (≥70% de probabilidade)
    - Tempestades
    - Risco de enchente (≥30mm de chuva acumulada)
    - Ventos fortes (≥30km/h)
    - Rajadas de vento (≥50km/h)
  - Níveis de severidade:
    - Informativo: Condições que merecem atenção
    - Atenção: Situações que requerem cuidados
    - Alerta Máximo: Condições críticas que exigem ação imediata

- **Alertas Simulados**
  - Modo de demonstração para testes
  - Simulação de condições climáticas extremas
  - Útil para treinamento e validação do sistema
  - Geração de alertas aleatórios para demonstração

### 3. Pontos de Apoio

- **Cadastro de Locais Seguros**

  - Nome e endereço completo
  - Capacidade de atendimento
  - Status de disponibilidade
  - Contato telefônico
  - Observações especiais

- **Geolocalização**

  - Coordenadas precisas (latitude/longitude)
  - Cálculo de distância até o usuário
  - Filtragem por região

- **Gerenciamento**
  - Aprovação de novos pontos (Administradores)
  - Atualização de status
  - Visualização de detalhes
  - Restrição de acesso por perfil

### 4. Histórico de Alertas

- **Registro Completo**

  - Data e hora de emissão
  - Tipo e nível do alerta
  - Localização afetada
  - Descrição detalhada

- **Filtragem e Visualização**
  - Por região (usuários comuns)
  - Todos os alertas (administradores)
  - Ordenação por data
  - Detalhes completos das condições

### 5. Calculadora de Hidratação

- **Cálculo Personalizado**
  - Baseado no peso corporal
  - Considera a temperatura atual
  - Ajustes automáticos:
    - +1.0 litro se temperatura ≥ 32°C
    - +0.5 litro se temperatura ≥ 28°C
  - Base: 35ml por kg de peso

## Requisitos

- Python 3.8 ou superior
- Conexão com internet para dados climáticos
- Acesso à API de geolocalização
- Bibliotecas Python (ver requirements.txt)

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/Sistema-Operacional-ARCA.git
cd Sistema-Operacional-ARCA
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

1. Execute o arquivo principal:

```bash
python main.py
```

2. Siga o menu interativo:
   - Selecione um usuário
   - Escolha as funcionalidades desejadas
   - Siga as instruções na tela

## Estrutura do Projeto

- `main.py`: Interface principal do sistema
- `usuarios.py`: Gerenciamento de usuários e perfis
- `alertas.py`: Sistema de alertas e notificações
- `api_clima.py`: Integração com API de clima
- `pontos_apoio.py`: Gerenciamento de pontos de apoio
- `historico_alertas.py`: Registro e consulta de histórico
- `geolocalizacao.py`: Integração com API de geolocalização
- `hidratar.py`: Calculadora de hidratação
- `utils.py`: Funções utilitárias
- `config.py`: Configurações do sistema
- `requirements.txt`: Dependências do projeto

## Contato

| Nome                           | GitHub                                        | LinkedIn                                                                |
| ------------------------------ | --------------------------------------------- | ----------------------------------------------------------------------- |
| Alexander Dennis Isidro Mamani | [alex-isidro](https://github.com/alex-isidro) | [LinkedIn](https://www.linkedin.com/in/alexander-dennis-a3b48824b/)     |
| Kelson Zhang                   | [KelsonZh0](https://github.com/KelsonZh0)     | [LinkedIn](https://www.linkedin.com/in/kelson-zhang-211456323/)         |
| Lucas Rossoni Dieder           | [PxS00](https://github.com/PxS00)             | [LinkedIn](https://www.linkedin.com/in/lucas-rossoni-dieder-32242a353/) |

## 📝 Notas

- O sistema utiliza APIs externas para dados climáticos e geolocalização
- Algumas funcionalidades podem requerer conexão com internet
- Os alertas são baseados em dados oficiais do INMET
- A calculadora de hidratação segue recomendações médicas padrão
