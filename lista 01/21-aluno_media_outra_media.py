nome = input("Digite seu nome: ")
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
nota4 = float(input("Digite a 4ª nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6.0:
    print("Aluno: "+ nome)
    print("Nota: " + str(media) + "\nAprovado.")
else:
    print("Aluno: "+ nome)
    print("Nota: " + str(media) + "\nReprovado.")
while True:
    again = input("1Deseja calcular outra média?(S/N)\n")
    while again != "S" or again != "N":
        again = input("2Deseja calcular outra média?(S/N)\n")
        if again == "S":
            nome = input("Digite seu nome: ")
            nota1 = float(input("Digite a 1ª nota: "))
            nota2 = float(input("Digite a 2ª nota: "))
            nota3 = float(input("Digite a 3ª nota: "))
            nota4 = float(input("Digite a 4ª nota: "))

            media = (nota1 + nota2 + nota3 + nota4) / 4

            if media >= 6.0:
                print("Aluno: "+ nome)
                print("Nota: " + str(media) + "\nAprovado.")
            else:
                print("Aluno: "+ nome)
                print("Nota: " + str(media) + "\nReprovado.")
        if again == "N":
            break
    if again == "N":
        break