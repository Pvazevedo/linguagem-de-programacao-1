N = int(input("Digite um número: "))
i = 0
while True:
    N = int(input("Digite um número: "))
    # Número negativo fora do resultado final
    if N > 0:
        i = i + N
    # Número negativo no resultado final
    #i = i + N
    if(N < 0):
        print("Soma: " + str(i))
        break
