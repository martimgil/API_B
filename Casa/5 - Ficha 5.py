nome = str(input("Insira o nome de uma pessoa: "))
idade = int(input("Insira a idade de uma pessoa: "))

if idade<0 or idade>120:
    print("Idade Inválida! ")
elif idade>=0 and idade<=11:
    print(nome,"está na infância.")
elif idade >= 12 and idade <= 20:
    print(nome,"está na adolescência.")
elif idade >= 21 and idade<75:
    print(nome,"está na fase adulta")
else:
    print(nome,"está na velhice")
