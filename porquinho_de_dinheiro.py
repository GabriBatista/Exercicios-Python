#region Porquinho de dinheiro
def porquinho(casos):
    for c in range(casos):
        cheio, vazio = map(int, input('Peso cheio e vazio: ').split())
        capacidade = cheio - vazio
        if capacidade <= 0:
            print('Isso é impossivel')
            continue
        moedas = int(input('Quantidade de moedas: '))
        moedasApp = []
        for i in range(moedas):
            valor, peso = map(int, input(f'Valor e peso da {i + 1}ª moeda: ').split())
            moedasApp.append((valor, peso))
        INF = float('inf')
        dp = [INF] * (capacidade + 1)
        dp[0] = 0
        for valor, peso in moedasApp:
            for i in range(peso, capacidade + 1):
                if dp[i - peso] + valor < dp[i]:
                    print(dp[capacidade])
                    dp[i] = dp[i - peso] + valor
        if dp[capacidade] != INF:
            print(dp[capacidade])
            print(f'O menor valor no porquinho é {dp[capacidade]}')
        else:
            print('Isso é impossível')
casos = int(input(f'Número de casos:'))
porquinho(casos)
#endregion