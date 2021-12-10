numero = 0
while numero <= 0:
    numero = int(input("Digite um número: ")) 
    i = numero - 1
    while i > 1:
        numero = numero * i
        i -= 1
print("Fatorial: "+ str(numero))