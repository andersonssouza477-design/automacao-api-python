import yfinance as yf
from datetime import datetime

print("--- 📊 Monitor de Carteira Avançado (Média Móvel de 5 Dias) ---")

# Lista de ações para monitorizar
minha_carteira = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "ABEV3.SA"]

# Cabeçalho do relatório
data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
conteudo_relatorio = f"--- 📊 RELATÓRIO DE TENDÊNCIAS (MÉDIA MÓVEL) ---\nGerado em: {data_atual}\n\n"

# A esteira do loop começa a trabalhar
for papel in minha_carteira:
    dados_acao = yf.Ticker(papel)
    
    # 🌟 ATENÇÃO: Mudamos para "5d" para trazer o histórico da semana!
    historico = dados_acao.history(period="5d")
    
    if len(historico) < 5:
        print(f"⚠️ Dados insuficientes para calcular a média de 5 dias de {papel}\n")
        continue
        
    # Preço de hoje (o último da tabela)
    preco_hoje = float(historico['Close'].iloc[-1])
    
    # 🧠 MATEMÁTICA: Pegamos a coluna 'Close', tiramos a média (.mean()) e garantimos o FLOAT
    preco_medio_5dias = float(historico['Close'].mean())
    
    # Monta o bloco de texto deste ativo
    bloco_ativo = f"📌 Ativo: {papel}\n"
    bloco_ativo += f"   Preço Atual: R$ {preco_hoje:.2f}\n"
    bloco_ativo += f"   Média dos Últimos 5 Dias: R$ {preco_medio_5dias:.2f}\n"
    
    # Lógica de QA / Insight de Investimento
    if preco_hoje < preco_medio_5dias:
        bloco_ativo += "   Análise: 🟢 O preço atual está ABAIXO da média da semana (Oportunidade?).\n"
    elif preco_hoje > preco_medio_5dias:
        bloco_ativo += "   Análise: 🔴 O preço atual está ACIMA da média da semana.\n"
    else:
        bloco_ativo += "   Análise: ⚪ O preço atual está igual à média da semana.\n"
        
    bloco_ativo += "-" * 45 + "\n"
    
    print(f"Processado com sucesso: {papel}")
    conteudo_relatorio += bloco_ativo

conteudo_relatorio += "--- Monitoramento Concluído com Sucesso ---"

# Salva o novo relatório físico substituindo o antigo[cite: 1]
with open("relatorio_acoes.txt", "w", encoding="utf-8") as ficheiro:
    ficheiro.write(conteudo_relatorio)

print("\n💾 NOVO RELATÓRIO GERADO! Abre o 'relatorio_acoes.txt' para ver os resultados!")