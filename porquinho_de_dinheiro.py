#region Porquinho de dinheiro
def porquinho_dinamico(casos):
    for c in range(casos):
        vazio, cheio = map(int, input(f'\nCaso {c + 1} — Digite peso vazio e cheio: ').split())
        peso_total = cheio - vazio
        n = int(input("Quantos tipos de moedas você tem? "))
        moedas = []
        for i in range(n):
            valor, peso = map(int, input(f"Moeda {i + 1} — valor e peso: ").split())
            moedas.append((valor, peso))
        INF = float('inf')
        dp = [INF] * (peso_total + 1)
        dp[0] = 0 
        for valor, peso in moedas:
            for w in range(peso, peso_total + 1):
                if dp[w - peso] + valor < dp[w]:
                    dp[w] = dp[w - peso] + valor
        if dp[peso_total] == INF:
            print("Isso é impossível.")
        else:
            print(f"O valor mínimo de dinheiro no cofrinho é {dp[peso_total]}.")

casos = int(input("Digite quantos casos devem ser resolvidos: "))
porquinho_dinamico(casos)
#endregion