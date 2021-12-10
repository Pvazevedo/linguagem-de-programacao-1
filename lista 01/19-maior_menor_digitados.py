N = int(input("Digite um número: "))
maior = N
menor = N
while True:
    N = int(input("Digite um número: "))
    if N > maior:
        maior = N
    # Sem negativo no resultado final
    if N < menor and N > 0:
        menor = N
    # Com negativo no resultado final
    # if N < menor:
        # menor = N
    if(N < 0):
        print("Maior: " + str(maior))
        print("Menor: " + str(menor))
        break