# Calculadora básica
print("\n\t-----Calculadora básica-----")
n1 = int(input("\nInsira o primeiro número: "))
n2 = int(input("\nInsira o segundo número: "))
op = input("\nQual a operação que pretende efetuar: ")

if op == "+":
    soma = n1+n2
    print("\nO valor da soma do {} com o {} é {}" .format(n1,n2,soma))
elif op == "-":
    subtracao = n1-n2
    print("\nO valor da subtração do {} com o {} é {}" .format(n1,n2,subtracao))
elif op == "*":
    multiplicacao = n1*n2
    print("\nO valor da multiplicação do {} com o {} é {}" .format(n1,n2,multiplicacao))
elif op == "/":
    if n1 == 0 or n2 == 0:
        print("\nNão  é possível dividir por 0!")
    else:
        divisao = n1/n2
        print("\nO valor da divisão do {} com o {} é {}" .format(n1,n2,divisao))
else:
    print("\n\tATENÇÃO!!! Carater inválido!!.")
