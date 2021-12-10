altura = 1
while altura <= 1 or altura >= 2.3:
    altura = float(input("Digite a sua altura em metros: "))
sexo = str(input("Digite seu sexo (sendo 'F' para Feminino e 'M' para Masculino: "))
while sexo != 'F' and sexo != 'M':
    sexo = input("Digite seu sexo (sendo 'F' para Feminino e 'M' para Masculino: ")
else:
    if sexo == 'M':
        peso = (72.7 * altura) - 58.7
    else:
        peso = (62.1 * altura) - 44.7
    print("Seu peso ideal é "+ str(round(peso, 2)) + " quilos.")
