#region * Lista até 42 *
guardarNums = []
numLista = int(input("Quantos números deseja digitar?\n"))
print("Digite os números:")
for _ in range(numLista):
    nums = int(input())
    guardarNums.append(nums)
for nums in guardarNums:
    if nums == 42:
        print(nums)
        break
    print(nums)
#endregion