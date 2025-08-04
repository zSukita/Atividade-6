# ===============================================
# 1. GERADOR DE SENHA ALEATÓRIA
# ===============================================

import random
import string
import requests
import json
from datetime import datetime

def gerar_senha_aleatoria():
    """
    Programa 1: Gera uma senha aleatória com caracteres especiais
    """
    print("=== GERADOR DE SENHA ALEATÓRIA ===")
    
    try:
        tamanho = int(input("Digite o número de caracteres para a senha: "))
        
        if tamanho <= 0:
            print("O tamanho deve ser um número positivo!")
            return
        
        # Definindo os caracteres disponíveis
        letras_minusculas = string.ascii_lowercase
        letras_maiusculas = string.ascii_uppercase
        numeros = string.digits
        caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Combinando todos os caracteres
        todos_caracteres = letras_minusculas + letras_maiusculas + numeros + caracteres_especiais
        
        # Gerando a senha
        senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))
        
        print(f"\nSenha gerada: {senha}")
        print(f"Tamanho: {len(senha)} caracteres")
        
    except ValueError:
        print("Por favor, digite um número válido!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# ===============================================
# 2. GERADOR DE PERFIL DE USUÁRIO ALEATÓRIO
# ===============================================

def gerar_perfil_usuario():
    """
    Programa 2: Gera um perfil de usuário aleatório usando a API Random User Generator
    """
    print("\n=== GERADOR DE PERFIL DE USUÁRIO ALEATÓRIO ===")
    
    try:
        # URL da API Random User Generator
        url = "https://randomuser.me/api/"
        
        print("Consultando API...")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            usuario = dados['results'][0]
            
            # Extraindo informações
            nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']
            cidade = usuario['location']['city']
            telefone = usuario['phone']
            
            print("\n--- PERFIL GERADO ---")
            print(f"Nome: {nome_completo}")
            print(f"Email: {email}")
            print(f"País: {pais}")
            print(f"Cidade: {cidade}")
            print(f"Telefone: {telefone}")
            
        else:
            print(f"Erro na consulta: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
    except KeyError as e:
        print(f"Erro ao processar dados da API: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# ===============================================
# 3. CONSULTA DE CEP
# ===============================================

def consultar_cep():
    """
    Programa 3: Consulta informações de endereço a partir de um CEP usando a API ViaCEP
    """
    print("\n=== CONSULTA DE CEP ===")
    
    try:
        cep = input("Digite o CEP (formato: 12345-678 ou 12345678): ").strip()
        
        # Removendo caracteres não numéricos
        cep_limpo = ''.join(filter(str.isdigit, cep))
        
        if len(cep_limpo) != 8:
            print("CEP deve conter exatamente 8 dígitos!")
            return
        
        # URL da API ViaCEP
        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
        
        print("Consultando CEP...")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            
            if 'erro' in dados:
                print("CEP não encontrado!")
                return
            
            print("\n--- INFORMAÇÕES DO CEP ---")
            print(f"CEP: {dados.get('cep', 'N/A')}")
            print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f"Bairro: {dados.get('bairro', 'N/A')}")
            print(f"Cidade: {dados.get('localidade', 'N/A')}")
            print(f"Estado: {dados.get('uf', 'N/A')}")
            print(f"Região: {dados.get('regiao', 'N/A')}")
            
        else:
            print(f"Erro na consulta: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# ===============================================
# 4. CONSULTA DE COTAÇÃO DE MOEDAS
# ===============================================

def consultar_cotacao():
    """
    Programa 4: Consulta cotação de moedas usando a API AwesomeAPI
    """
    print("\n=== CONSULTA DE COTAÇÃO DE MOEDAS ===")
    
    try:
        print("Moedas disponíveis: USD, EUR, GBP, ARS, BTC, etc.")
        codigo_moeda = input("Digite o código da moeda (ex: USD): ").strip().upper()
        
        if not codigo_moeda:
            print("Código da moeda não pode estar vazio!")
            return
        
        # URL da API AwesomeAPI
        url = f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL"
        
        print(f"Consultando cotação de {codigo_moeda}...")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            
            # A chave do JSON é no formato "USDBRL", "EURBRL", etc.
            chave_moeda = f"{codigo_moeda}BRL"
            
            if chave_moeda in dados:
                cotacao = dados[chave_moeda]
                
                # Convertendo timestamp para data legível
                timestamp = int(cotacao['timestamp'])
                data_atualizacao = datetime.fromtimestamp(timestamp)
                
                print(f"\n--- COTAÇÃO {codigo_moeda}/BRL ---")
                print(f"Moeda: {cotacao['name']}")
                print(f"Valor Atual: R$ {float(cotacao['bid']):.4f}")
                print(f"Valor Máximo: R$ {float(cotacao['high']):.4f}")
                print(f"Valor Mínimo: R$ {float(cotacao['low']):.4f}")
                print(f"Variação: {float(cotacao['pctChange']):.2f}%")
                print(f"Última Atualização: {data_atualizacao.strftime('%d/%m/%Y %H:%M:%S')}")
                
            else:
                print(f"Moeda {codigo_moeda} não encontrada ou não disponível!")
                
        else:
            print(f"Erro na consulta: {response.status_code}")
            if response.status_code == 404:
                print("Moeda não encontrada. Verifique o código digitado.")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
    except ValueError as e:
        print(f"Erro ao processar dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# ===============================================
# MENU PRINCIPAL
# ===============================================

def main():
    """
    Menu principal para executar os programas
    """
    while True:
        print("\n" + "="*50)
        print("ESCOLHA UM PROGRAMA PARA EXECUTAR:")
        print("="*50)
        print("1 - Gerador de Senha Aleatória")
        print("2 - Gerador de Perfil de Usuário")
        print("3 - Consulta de CEP")
        print("4 - Consulta de Cotação de Moedas")
        print("0 - Sair")
        print("="*50)
        
        try:
            opcao = input("Digite sua opção: ").strip()
            
            if opcao == "1":
                gerar_senha_aleatoria()
            elif opcao == "2":
                gerar_perfil_usuario()
            elif opcao == "3":
                consultar_cep()
            elif opcao == "4":
                consultar_cotacao()
            elif opcao == "0":
                print("Programa encerrado. Até logo!")
                break
            else:
                print("Opção inválida! Digite um número de 0 a 4.")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")

# ===============================================
# EXECUÇÃO DO PROGRAMA
# ===============================================

if __name__ == "__main__":
    main()