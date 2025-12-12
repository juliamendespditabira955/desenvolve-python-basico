print (" ------------ MÉDIA DE IDADES -------------")
n = int(input("Digite a quantidaade de correspondentes:"))
soma = 0  # acumulador das idades
for _ in range(n):
    idade = int(input("Digite a idade: "))
    soma += idade
media = soma / n
print("Média das idades:", media)
