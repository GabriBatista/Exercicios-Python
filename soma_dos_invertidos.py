#region * Soma de números invertidos *
quantSomas = int(input("Número de somas: "))
guardarResul = []
guardarResuls = []
print("Números a serem somados: ")
for i in range(quantSomas):
    i - 1
    numeros = input().split()
    a, b = map(lambda x: int(x[::-1]), numeros)    
    guardarResul = a + b
    guardarResuls.append(int(str(guardarResul)[::-1]))
print(guardarResuls)
#endregion