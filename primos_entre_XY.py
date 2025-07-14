#region * Primos entre XY
import time
primos = []
casos = int(input('Quantos casos você quer que sejam resolvidos?\n'))
for i in range(casos):
    x, y = map(int, input(f'caso {i + 1}\n').split())
    inicio = time.time()
    X = min(x, y)
    Y = max(x, y)
    while X <= Y:
        X += 1
        for n in range(2, int((X ** 0.5) + 1)):
            primo = True
            if X % n == 0:
                primo = False
                break
        if primo:
             primos.append(X)
    print(f'Os números primos entre {x} e {y} são: \n{primos}')
    primos.clear()
fim = time.time()
print(f"Tempo de execução: {fim - inicio:.4f} segundos")
#endregion 