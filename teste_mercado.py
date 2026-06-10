import urllib.request
import json

print("--- 📈 MOTOR DE DADOS FINANCEIROS INTERNACIONAIS ---")

# Dicionário organizando as principais ações por mercado/país
CATALOGO_ACOES = {
    "Brasil (B3)": {
        "PETR4.SA": "Petrobras",
        "VALE3.SA": "Vale",
        "ITUB4.SA": "Itaú Unibanco"
    },
    "Estados Unidos (NASDAQ/NYSE)": {
        "AAPL": "Apple Inc.",
        "MSFT": "Microsoft",
        "NVDA": "NVIDIA"
    },
    "Nova Zelândia (NZX)": {
        "AIR.NZ": "Air New Zealand",
        "FPH.NZ": "Fisher & Paykel Healthcare",
        "AIA.NZ": "Auckland Airport"
    }
}

def buscar_cotacao_global(ticker):
    """
    Busca o preço atualizado de qualquer ação do mundo usando uma URL pública.
    Faremos a requisição usando a biblioteca nativa do Python que roda direto no PyScript.
    """
    # Usamos o proxy de finanças do Yahoo que o navegador não bloqueia
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=1d"
    
    try:
        # Define um cabeçalho (User-Agent) para simular um navegador real e evitar bloqueios
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req) as resposta:
            dados = json.loads(resposta.read().decode())
            
            # Navega pelas chaves do JSON do Yahoo Finance para achar o preço
            meta = dados["chart"]["result"][0]["meta"]
            preco_atual = meta["regularMarketPrice"]
            moeda = meta["currency"]
            
            return preco_atual, moeda
    except Exception as e:
        print(f"❌ Erro ao buscar o ticker {ticker}: {e}")
        return None, None

# --- TESTANDO O MOTOR NA TELA ---
# Vamos simular o usuário navegando pelo nosso catálogo internacional
for mercado, acoes in CATALOGO_ACOES.items():
    print(f"\n🌍 Mercado: {mercado}")
    print("-" * 40)
    for ticker, nome in acoes.items():
        preco, moeda = buscar_cotacao_global(ticker)
        if preco:
            # Exibe o nome da empresa, o código (ticker) e o valor na moeda local dela
            print(f"📈 {nome} ({ticker}) -> {moeda} ${preco:.2f}")
        else:
            print(f"❌ Não foi possível carregar {ticker}")