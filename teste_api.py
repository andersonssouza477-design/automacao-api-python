import requests

print("--- 🌍 Iniciando Validação de QA Multi-Moedas ---")

# Na URL, nós separamos as moedas que queremos por vírgula!
url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,CAD-BRL,AUD-BRL,NZD-BRL"
resposta = requests.get(url)

if resposta.status_code == 200:
    print("✅ PASS: API respondeu com sucesso para todas as moedas.\n")
    dados = resposta.json()
    
    # Lista com os códigos das moedas que pedimos para facilitar a nossa leitura
    moedas_para_testar = ['USDBRL', 'EURBRL', 'CADBRL', 'AUDBRL', 'NZDBRL']
    
    # O robô vai passar de moeda em moeda usando um Loop (igual você fez no Projeto 1!)
    for codigo in moedas_para_testar:
        nome = dados[codigo]['name']
        
        # O nosso bom e velho FLOAT garantindo a segurança matemática
        valor = float(dados[codigo]['bid']) 
        variacao = dados[codigo]['pctChange']
        
        print(f"💰 {nome}")
        print(f"   Valor Atual: R$ {valor:.2f}")
        print(f"   Variação: {variacao}%")
        
        # Validação de QA para cada moeda da lista
        if valor > 0:
            print(f"   ✅ Assert: Payload de {codigo} íntegro.")
        else:
            print(f"   ❌ Assert: ERRO! {codigo} veio com valor zerado.")
        print("-" * 40) # Linha para separar as moedas visualmente

else:
    print(f"❌ FAIL: Erro na requisição. Status: {resposta.status_code}")

print("\n--- Fim do Teste Global ---")