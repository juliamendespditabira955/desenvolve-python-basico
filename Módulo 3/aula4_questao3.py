input("--------- BEM - VINDO ----------")
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Este ano é BISSEXTO!")
else:
    print("Esse ano NÃO É BISSEXTO!")
    