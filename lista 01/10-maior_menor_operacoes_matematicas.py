x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
if x < y:
    x, y = y, x
soma = x + y
subtracao = x - y
multiplicacao = x * y

print("Soma: " + str(soma))
print("Subtração: " + str(subtracao))
print("Multiplicação: " + str(multiplicacao))
if y > 0:
    divisao = x / y
    print("Divisão: " + str(divisao))
else:
    print("Divisão: Não é possível divir por zero.")
