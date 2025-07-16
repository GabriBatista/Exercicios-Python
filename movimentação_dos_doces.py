#region Movimentação dos doces
casos = int(input('Dígite quantos casos devem ser resolvidos\n'))
for i in range(casos):
    docesApp = []
    subApp = []
    pacotes = int(input(f'Quantos pacotes de doce no {i + 1}º Caso?\n'))
    for j in range(pacotes):
        doces = int(input(f'Quantos doces existem no {j + 1}º Pacote?\n'))
        docesApp.append(doces)
    media = sum(docesApp) / pacotes
    if sum(docesApp) % pacotes != 0:
        print('Não é possível redistribuir a quantidade de doces igualmente sem quebra-los')
    else:
        for n in docesApp:
            if n > media:
                sub = int(n - media)
                subApp.append(sub)
            else:
                continue
        print(f'A quantidade de movimentos necessários é: {sum(subApp)}')
#endregion