# Descritivo
# 1. Início
# 2. Declarar variáveis a, b e c
# 3. Mostrar mensagem "Uma equação de 2º grau é dada pela expressão 'ax^2 + bx + c = 0'"
# 4. Mostrar mensagem "Para obter as raízes, digite respectivamente os valores de a, b e c:"
# 5. Solicitar variável a
# 6. Solicitar variável b
# 7. Solicitar variável c
# 8. Calcular delta
# 9. Calcular x1
# 10. Calcular x2
# 11. Mostrar mensagem concatenando as variáveis a, b e c e substituindo por seus valores.
# 12. Mostrar x1
# 13. Mostrar x2
# 14. Fim

# Estruturado
# 1. INÍCIO
# 2. DECLARE: a, b, c
# 3. ESCREVA: "Uma equação de 2º grau é dada pela expressão 'ax^2 + bx + c = 0'"
# 4. ESCREVA: "Para obter as raízes, digite respectivamente os valores de a, b e c:"
# 5. LEIA: a
# 6. LEIA: b
# 7. LEIA: c
# 8. CALCULE: Delta <- b^2 - 4*a*c
# 9. CALCULE: x1 <- (-b + delta^0.5) / 2*a
# 10. CALCULE: x2 <- (-b - delta^0.5) / 2*a
# 11. ESCREVA: "As raízes da expressão " + a + "x^2 + " + b + "x + " + c + " = 0 são:"
# 12. ESCREVA: x1
# 13. ESCREVA: x2
# 14. FIM

a, b, c = (0,)*3
repeat = 'S'

while repeat == 'S' or repeat == 's':
    print("Uma equação de 2º grau é dada pela expressão 'ax^2 + bx + c = 0'")
    print("Para obter as raízes, digite respectivamente os valores de a, b e c:")

    a = int(input())
    b = int(input())
    c = int(input())

    delta = (b ** 2) - 4 * (a) * (c)
    print(delta)
    if delta > 0:
        x1 = ((b * -1) + (delta ** 0.5)) / 2 * a
        x2 = ((b * -1) - (delta ** 0.5)) / 2 * a
        print("As raízes da expressão " + str(a) + "x^2 + " +
              str(b) + "x + " + str(c) + " = 0 são:")
        print(x1)
        print(x2)
        repeat = str(
            input("Deseja fazer um novo cálculo? \nDigite s ou S para 'SIM': "))
    else:
        print("Não foi possível calcular, delta negativo.")
        repeat = str(
            input("Deseja fazer um novo cálculo? \nDigite s ou S para 'SIM': "))
