input("--------- BEM - VINDO!---------")
compr = int(input("Digite o valor do comprimento: "))
larg = int(input("Digite o valor da largura:"))
metro = float(input("Digite o valor do m2: "))
area = compr*larg
total = metro*area
print (f"O terreno possui {area}m2 e custa R$ {total}")