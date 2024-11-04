n1 = int(input("Insira a quantidade de números que pretende digitar: "))
valor=0

for i in range(n1):
    n2 = int(input("Insira um número inteiro: "))
    valor=valor+n2
print("Digitados {} números com o valor total de {}. ".format(n1,valor))
