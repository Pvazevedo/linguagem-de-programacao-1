km1 = 0
km2 = 0
gasolina = 0
bruto = 0

while km1 <= 0:
    km1 = float(input("Km inicial: "))
while km2 <= 0:
    km2 = float(input("Km final: "))
while gasolina <= 0:
    gasolina = float(input("Quantos litros de gasolina foram gastos hoje? "))   
while bruto <= 0:
    bruto = float(input("Valor bruto recebido hoje? "))

media = (km2-km1) / gasolina
abastecer = gasolina * 2.75
liquido = bruto - abastecer
print("Sua média de consumo foi de "+str(media)+" Km/L.")
print("O gasto para abstecer o veículo foi de R$ "+str(abastecer)+ " reais.")
print("Seu lucro líquido do dia foi de R$ "+str(liquido)+" reais.")

