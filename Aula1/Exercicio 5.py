#Programa que verifica se os numeros são iguais, maior ou menor que o outro

print("\nVerificar qual número é maior")
n1 = int(input("\nInsira o primeiro número: "))
n2 = int(input("\nInsira o segundo número: "))

if n1==n2:
    print("\nOs números são iguais! ")
elif n1>n2:
    print("\nO primeiro número {} é maior que o segundo número {}.".format(n1,n2))
else:
    print("\nO segundo número {} é maior que o primeiro número {}.".format(n2, n1))
