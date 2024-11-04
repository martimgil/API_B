#Calcular a média de n números

n = int(input("\nQuantos números inteiros prentende inserir:"))
soma=0
for i in range(n):
    num=int(input("Insira o número:"))
    soma=soma+num

media=soma/n
print("A média dos números é:", media)
