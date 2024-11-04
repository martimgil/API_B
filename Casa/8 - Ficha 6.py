soma = 0
n2 = 0
while True:
    n1 = int(input("Digite um número real: "))
    if n1 == 0:
        break
    else:
        soma = soma + n1
        n2 = n2 + 1
print("Soma: ", soma)
media=soma/n2
print("Media: ", media)