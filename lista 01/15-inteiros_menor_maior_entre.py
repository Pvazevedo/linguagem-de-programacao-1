x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))
if x > y:
    x, y = y, x
while x < y-1:
    x += 1
    print(x)
    