print ("----------- FLUXOGRAMA PT4 -----------")
numero = float(input("Digite um número:"))
maior = 0
while numero > 0:
    x = float(input("Digite um valor: "))

    if x > maior:
        maior = x

    numero = numero - 1 
print("Maior valor:", maior)

