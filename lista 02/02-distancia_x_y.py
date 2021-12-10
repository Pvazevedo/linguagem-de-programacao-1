x = 0
y = 0

while x <= 0:
    x = int(input("Digite um número: "))
while y <= 0:
    y = int(input("Digite outro número: "))

if x < y:
    x, y = y, x

distancia = x - y
print("Distância: " + str(distancia))
