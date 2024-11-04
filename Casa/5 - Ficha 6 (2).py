#Fazer a soma de n números

n1=int(input("Quantos número deseja inserir? "))
soma = 0

while n1>0:
    n1=n1-1
    n2=int(input("Insira um número inteiro: "))
    soma = soma + n2
print("O valor da soma é ", soma)