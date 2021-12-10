qntd = 0
while qntd <= 0:
    qntd = float(input("Quantas maçãs deseja comprar?\n"))
if qntd >= 12:
    custo = qntd * 0.36
else:
    custo = qntd*0.45
print(str(round(qntd))+" maçãs custarão R$ "+ str(round(custo, 2))+ " reais.")
