# region * Lista até 42 *
# guardarNums = []
# numLista = int(input())
# print("Digite os números")
# for i in range(numLista):
#     i + 1
#     nums = int(input())
#     guardarNums.append(nums)
# for nums in guardarNums:
#     if nums == 42:
#         print(nums)
#         break
#     print(nums)
# endregion

# region * Soma de números invertidos *
# quantSomas = int(input("Digite quantas somas você quer resolver\n"))
# guardarResul = []
# guardarResuls = []
# print("Escreva somente os números que serão somados, sem sinal")
# for i in range(quantSomas):
#     i - 1
#     numeros = input().split()
#     a, b = map(lambda x: int(x[::-1]), numeros)    
#     guardarResul = a + b
#     guardarResuls.append(int(str(guardarResul)[::-1]))
# print(guardarResuls)

# endregion

#region * 
primos = []
casos = int(input('Quantos casos você quer que sejam resolvidos?\n'))
for i in range(casos):
    x, y = map(int, input(f'caso {i + 1}\n').split())
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
# endregion 