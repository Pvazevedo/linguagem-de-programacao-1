comp = 0
alt = 0
larg = 0

while comp <= 0:
    comp = float(input("Digite o comprimento da sua cozinha:"))
while larg <= 0:
    larg = float(input("Digite o largura da sua cozinha:"))
while alt <= 0:
    alt = float(input("Digite o altura da sua cozinha:"))

area1 = 2 * (comp * alt)
area2 = 2 * (larg * alt)
azul = (area1 + area2) / 1.5 

print("Serão necessárias "+str(azul)+" caixas de azulejos para suas paredes")