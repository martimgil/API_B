#Fazer a soma de n números
n1=int(input("Insira quantos números deseja somar: "))

soma = 0

for i in range(n1):
    n2 = int(input("Insira um número inteiro: "))
    soma = soma + n2
print ("O resultado da soma é: ", soma)