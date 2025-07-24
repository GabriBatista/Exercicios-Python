#region Banco
import random
from collections import Counter
def gerar_contas_aleatorias(n):
    contas = []
    for i in range(n):
        if contas and random.random() < 0.35:
            contas.append(random.choice(contas))
            continue
        controle = f"{random.randint(0, 99):02d}"
        codigo = f"{random.randint(0, 99999999):08d}"
        id1 = f"{random.randint(0, 9999):04d}"
        id2 = f"{random.randint(0, 9999):04d}"
        id3 = f"{random.randint(0, 9999):04d}"
        id4 = f"{random.randint(0, 9999):04d}"
        conta = f"{controle} {codigo} {id1} {id2} {id3} {id4}"
        contas.append(conta)
    return contas
def ordenar_contas(contas):
    contagem = Counter(contas)
    unicos = list(contagem.keys())
    unicos.sort()
    for conta in unicos:
        print(f'{conta} {contagem[conta]}')

casos = int(input('Número de casos: '))
for c in range(casos):
    print(f'\n--- Caso {c + 1} ---')
    n = int(input('Número de contas: '))
    contas_geradas = gerar_contas_aleatorias(n)
    ordenar_contas(contas_geradas)
    print()
#endregion