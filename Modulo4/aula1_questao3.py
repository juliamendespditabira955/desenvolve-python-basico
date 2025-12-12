print("----------- FLUXOGRAMA PT3 -----------")
n1 = float(input("Digite um número:"))
n2 = float(input("Digite um número:"))
n3 = float(input("Digite um número:"))
m = (n1 + n2 + n3)/3
if m>= 60:
    print ("Aprovado!")
elif m>= 40:
    print("Recuperação")
else:
    print("Reprovado")
print ("Fim")