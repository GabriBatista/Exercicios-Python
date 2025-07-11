# region * Soma de números invertidos *
quantSomas = int(input("Digite quantas somas você quer resolver\n"))
guardarResul = []
guardarResuls = []
print("Escreva somente os números que serão somados, sem sinal")
for i in range(quantSomas):
    i - 1
    numeros = input().split()
    a, b = map(lambda x: int(x[::-1]), numeros)    
    guardarResul = a + b
    guardarResuls.append(int(str(guardarResul)[::-1]))
print(guardarResuls)
# endregion