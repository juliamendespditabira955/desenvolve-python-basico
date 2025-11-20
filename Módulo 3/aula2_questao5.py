input("--------- BEM - VINDO ----------")
genero = (input("Qual o seu gênero? Digite M (Masculino) o F (Feminino) "))
idade = int(input("Qual a sua idade?"))
anosserv = int(input("Quantos anos de serviço você tem ?"))
F = idade >=60 or anosserv >=25
M = idade >=65 or anosserv >=25
faposentar = F
maposentar =  M 
print("Está apto para aposentar ?")
print(faposentar)
print(maposentar)