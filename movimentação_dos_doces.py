#region
import time
casos = int(input('Dígite quantos casos devem ser resolvidos\n'))
for i in range(casos):
    print(f'{i + 1}º Caso\n')
    pacotes = int(input('Quantos pacotes de doce?'))
    for j in range(pacotes):
        doces = int(input('Quantos doces existem em cada pacote?'))
        print(f'{j + 1}º Pacote\n')
        
#endregion