import yfinance as yf

# =====================================================================
# 1. A NOSSA FUNÇÃO INTELIGENTE E AUTÔNOMA
# =====================================================================
def analisar_risco_automatico(ticker):
    print(f"Buscando histórico de {ticker} na Bolsa...")
    
    # O robô vai na internet sozinho e pega o histórico do último mês
    acao = yf.Ticker(ticker)
    historico = acao.history(period="1mo")
    
    # O robô descobre sozinho o maior e o menor preço do mês
    preco_maximo = historico['High'].max()
    preco_minimo = historico['Low'].min()
    
    # Calcula a oscilação (a variação máxima no mês)
    oscilacao = preco_maximo - preco_minimo
    
    # REGRA DE NEGÓCIO AUTÔNOMA: 
    # Se a ação oscilou mais de R$ 4.00 no mês, o ROBÔ decide que é alto risco.
    if oscilacao > 4.00:
        perfil = "🚀 ALTO RISCO (Alta oscilação de preço)"
    else:
        perfil = "🛡️ BAIXO RISCO (Preço mais estável)"
        
    # A função devolve o relatório prontinho
    return f"Ação: {ticker} | Oscilação Mensal: R$ {oscilacao:.2f} | Perfil: {perfil}"


# =====================================================================
# 2. CÓDIGO PRINCIPAL (Totalmente limpo e automatizado!)
# =====================================================================
print("--- 🤖 ROBÔ DE ANÁLISE DE RISCO AUTÔNOMO --- \n")

# Agora você SÓ passa o ticker. O robô faz TODA a investigação sozinho!
relatorio_vale = analisar_risco_automatico("VALE3.SA")
print(relatorio_vale)
print("-" * 60)

relatorio_itau = analisar_risco_automatico("ITUB4.SA")
print(relatorio_itau)
print("-" * 60)