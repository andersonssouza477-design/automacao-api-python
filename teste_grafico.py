import urllib.request
import json

def analisar_historico_acao(ticker):
    # Alteramos o range para '1mo' (1 mês) e o intervalo para '1d' (1 dia)
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=1mo"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req) as resposta:
            dados = json.loads(resposta.read().decode())
            
            # Pega a lista de fechamentos dos últimos 30 dias
            historico_precos = dados["chart"]["result"][0]["indicators"]["quote"][0]["close"]
            
            # Remove valores nulos (dias que a bolsa fecha, como finais de semana)
            precos_limpos = [preco for preco in historico_precos if preco is not None]
            
            # --- CÁLCULOS QUE VÃO PROS SEUS CARDS ---
            preco_atual = precos_limpos[-1]
            maxima_30_dias = max(precos_limpos)
            minima_30_dias = min(precos_limpos)
            
            # --- PROJEÇÃO SIMPLES (Tendência baseada nos últimos 5 dias) ---
            ultimos_dias = precos_limpos[-5:]
            if ultimos_dias[-1] > ultimos_dias[0]:
                projecao = "TENDÊNCIA DE ALTA 📈"
            elif ultimos_dias[-1] < ultimos_dias[0]:
                projecao = "TENDÊNCIA DE QUEDA 📉"
            else:
                projecao = "ESTÁVEL / LATERALIZADO 📊"
                
            return preco_atual, maxima_30_dias, minima_30_dias, projecao, precos_limpos
            
    except Exception as e:
        print(f"Erro ao analisar {ticker}: {e}")
        return None

# --- TESTANDO O MOTOR COM A APPLE E A PETROBRAS ---
for ticker in ["PETR4.SA", "AAPL"]:
    resultado = analisar_historico_acao(ticker)
    if resultado:
        atual, maxima, minima, proj, lista = resultado
        print(f"\n===== ANÁLISE DE {ticker} =====")
        print(f"💵 Preço Atual: ${atual:.2f}")
        print(f"🔺 Máxima 30 dias: ${maxima:.2f}")
        print(f"🔻 Mínima 30 dias: ${minima:.2f}")
        print(f"🔮 Projeção Futura: {proj}")
        print(f"📊 Quantidade de pontos no gráfico: {len(lista)} dias mapeados")