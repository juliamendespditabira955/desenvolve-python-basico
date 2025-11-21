input("--------- BEM - VINDO ---------")
distancia = int(input("Qual é a distância da entrega em km ? "))
peso =  int(input("Qual é o peso da encomenda em kg ? "))
cemkm = distancia <=100 
maisqcemkm = distancia >=101<=300
maisqt = distancia >=300 
adicional = peso > 10
if cemkm and peso>10:
    print("O valor do frete é de:")
    print(distancia*1*peso+10 )
else:
    print("O valor do frete é de: ")
    print(distancia*1*peso)
if maisqcemkm and peso>10:
    print("O valor do frete é de:")
    print(distancia*1.50*peso+10)
else: 
    print("O valor do frete é de:")
    prinnt(distancia*1.50*peso)
if maisqt and peso>10:
    print("O valor do frete é de:")
    print(distancia*2*peso)
else:
    print("O valor do frete é de: ")
    print(distancia*2*peso)
