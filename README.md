# 🐍 Programas Python - Gerador de Senhas, Perfis e Consultas APIs

Este repositório contém 4 programas Python úteis para geração de senhas, perfis de usuário e consultas a APIs públicas.

## 📋 Índice

- [Programas Incluídos](#-programas-incluídos)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Detalhes dos Programas](#-detalhes-dos-programas)
- [APIs Utilizadas](#-apis-utilizadas)
- [Tratamento de Erros](#-tratamento-de-erros)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

## 🚀 Programas Incluídos

1. **🔐 Gerador de Senha Aleatória** - Gera senhas seguras com caracteres especiais
2. **👤 Gerador de Perfil de Usuário** - Cria perfis aleatórios usando API externa
3. **📍 Consulta de CEP** - Busca informações de endereço por CEP
4. **💱 Cotação de Moedas** - Consulta cotações em tempo real

## 🛠 Pré-requisitos

- Python 3.6 ou superior
- Conexão com a internet (para programas 2, 3 e 4)
- Biblioteca `requests` para consumo de APIs

## 📦 Instalação

1. **Clone ou baixe o repositório:**
```bash
git clone <url-do-repositorio>
cd programas-python
```

2. **Instale as dependências:**
```bash
pip install requests
```

3. **Execute o programa:**
```bash
python main.py
```

## 🎯 Como Usar

### Menu Principal
Ao executar o programa, você verá um menu interativo:

```
==================================================
ESCOLHA UM PROGRAMA PARA EXECUTAR:
==================================================
1 - Gerador de Senha Aleatória
2 - Gerador de Perfil de Usuário
3 - Consulta de CEP
4 - Consulta de Cotação de Moedas
0 - Sair
==================================================
```

### Exemplos de Uso

#### 1. Gerador de Senha
```
Digite o número de caracteres para a senha: 12
Senha gerada: aB3@mK9$pL2!
```

#### 2. Perfil de Usuário
```
--- PERFIL GERADO ---
Nome: John Smith
Email: john.smith@example.com
País: United States
Cidade: New York
Telefone: (555) 123-4567
```

#### 3. Consulta CEP
```
Digite o CEP: 01310-100
--- INFORMAÇÕES DO CEP ---
CEP: 01310-100
Logradouro: Avenida Paulista
Bairro: Bela Vista
Cidade: São Paulo
Estado: SP
```

#### 4. Cotação de Moedas
```
Digite o código da moeda: USD
--- COTAÇÃO USD/BRL ---
Moeda: Dollar
Valor Atual: R$ 5.1234
Valor Máximo: R$ 5.2000
Valor Mínimo: R$ 5.0500
Variação: +1.25%
```

## 📝 Detalhes dos Programas

### 🔐 Programa 1: Gerador de Senha Aleatória

**Funcionalidades:**
- Gera senhas com comprimento personalizado
- Inclui letras maiúsculas e minúsculas
- Adiciona números e caracteres especiais
- Validação de entrada do usuário

**Caracteres utilizados:**
- Letras: `a-z`, `A-Z`
- Números: `0-9`
- Especiais: `!@#$%^&*()_+-=[]{}|;:,.<>?`

### 👤 Programa 2: Gerador de Perfil de Usuário

**Funcionalidades:**
- Consome API Random User Generator
- Gera perfis completos e realistas
- Exibe informações pessoais e de contato
- Tratamento de falhas de conexão

**Dados gerados:**
- Nome completo
- Email
- País e cidade
- Telefone

### 📍 Programa 3: Consulta de CEP

**Funcionalidades:**
- Consulta API ViaCEP
- Aceita CEP com ou sem formatação
- Validação de formato (8 dígitos)
- Informações completas de endereço

**Informações retornadas:**
- Logradouro
- Bairro
- Cidade
- Estado (UF)
- Região

### 💱 Programa 4: Cotação de Moedas

**Funcionalidades:**
- Consulta API AwesomeAPI
- Cotações em tempo real
- Histórico de variação
- Data/hora da última atualização

**Moedas suportadas:**
- USD (Dólar Americano)
- EUR (Euro)
- GBP (Libra Esterlina)
- BTC (Bitcoin)
- E muitas outras...

## 🌐 APIs Utilizadas

| Programa | API | URL Base | Documentação |
|----------|-----|----------|--------------|
| 2 | Random User Generator | `https://randomuser.me/api/` | [Docs](https://randomuser.me/documentation) |
| 3 | ViaCEP | `https://viacep.com.br/ws/` | [Docs](https://viacep.com.br/) |
| 4 | AwesomeAPI | `https://economia.awesomeapi.com.br/` | [Docs](https://docs.awesomeapi.com.br/) |

## ⚠️ Tratamento de Erros

O programa inclui tratamento robusto de erros para:

- **Conexão de rede**: Timeout e falhas de conectividade
- **Validação de entrada**: Formatos inválidos e dados vazios
- **Respostas de API**: Status codes e dados malformados
- **Interrupções**: Ctrl+C e outros sinais do sistema
- **Tipos de dados**: Conversões e parsing de JSON

## 🧪 Testes

Para testar os programas:

1. **Programa 1**: Teste com diferentes tamanhos de senha
2. **Programa 2**: Execute múltiplas vezes para ver perfis diferentes
3. **Programa 3**: Teste com CEPs válidos e inválidos
4. **Programa 4**: Teste com códigos de moeda válidos e inválidos

### Exemplos de CEPs para teste:
- `01310-100` (São Paulo - SP)
- `20040-020` (Rio de Janeiro - RJ)
- `70040-010` (Brasília - DF)

### Códigos de moeda para teste:
- `USD` (Dólar)
- `EUR` (Euro)
- `GBP` (Libra)
- `BTC` (Bitcoin)

## 🔧 Personalização

Você pode personalizar os programas:

### Gerador de Senha
```python
# Modificar caracteres especiais
caracteres_especiais = "!@#$%^&*"

# Adicionar mais tipos de caracteres
emoji = "😀😁😂🤣😃"
```

### Consulta APIs
```python
# Modificar timeout das requisições
response = requests.get(url, timeout=5)

# Adicionar headers personalizados
headers = {'User-Agent': 'MeuApp/1.0'}
response = requests.get(url, headers=headers)
```

## 📁 Estrutura do Projeto

```
projeto/
├── main.py              # Arquivo principal com todos os programas
├── README.md            # Este arquivo
└── requirements.txt     # Dependências (opcional)
```

## 🚨 Limitações e Considerações

- **Dependência de Internet**: Programas 2, 3 e 4 precisam de conexão
- **Rate Limiting**: APIs podem ter limites de requisições
- **Disponibilidade**: APIs externas podem estar indisponíveis
- **Dados Sensíveis**: Não armazene senhas geradas em arquivos não criptografados

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Ideias para contribuição:
- Adicionar mais tipos de caracteres nas senhas
- Implementar salvamento de dados em arquivos
- Criar interface gráfica
- Adicionar mais APIs de consulta
- Implementar cache para reduzir requisições

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor  Lucas Silva

Desenvolvido com ❤️ em Python

## 📞 Suporte

Se encontrar problemas ou tiver sugestões:

1. Verifique se todas as dependências estão instaladas
2. Confirme sua conexão com a internet
3. Consulte a documentação das APIs utilizadas
4. Abra uma issue no repositório

---

**⭐ Se este projeto foi útil, considere dar uma estrela!**
