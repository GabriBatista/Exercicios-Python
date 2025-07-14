#region * Lista até 42 *
import time
guardarNums = []
numLista = int(input("Quantos números deseja digitar?\n"))
print("Digite os números:")
for _ in range(numLista):
    nums = int(input())
    guardarNums.append(nums)
inicio = time.time()
for nums in guardarNums:
    if nums == 42:
        print(nums)
        break
    print(nums)
fim = time.time()
print(f"\nTempo de execução (processamento): {fim - inicio:.4f} segundos")
#endregion