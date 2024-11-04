n1 = int(input("Insira a quantidade de números que pretende digitar"))
total = 0

while n1 > 0:
    n2 = int(input("Insira um número inteiro: "))
    total = total + n2
    n1 = n1 - 1
print("Digitados {} números com o valor total {}.".format(n1, total))
