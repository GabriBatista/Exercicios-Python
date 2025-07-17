#region Porquinho de dinheiro
casos = int(input('Dígite quantos casos devem ser realizados\n'))
for i in range(casos):
    x, y = map(int, input(f'Escreva o peso do porquinho vazio, e cheio de moedas, nessa ordem (Caso {i + 1}º)\n').split())
    diferenca = abs(x - y)
    moedas = int(input('Quantos tipos de moedas você tem?\n'))
    for j in range(moedas):
        valorMoeda, pesoMoeda = map(int, input(f'Tipo {j + 1}\n').split())
#endregion