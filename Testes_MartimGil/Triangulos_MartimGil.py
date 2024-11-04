print("\nVERIFICA SE É UM TRIÂNGULO ---> EQUILÁTERO, ISÓSCELES OU ESCALENO")
n1 = float(input("\nInsira um dos lados do triângulo: "))
n2 = float(input("Insira um dos lados do triângulo: "))
n3 = float(input("Insira um dos lados do triângulo: "))

soma = n1+n2

if soma > n3:
    if n1 == n2 and n2 == n3 and n1 == n3:
        print("\nTriângulo EQUILÁTERO: três lados iguais")
    elif n1 != n2 and n2 != n3 and n3 != n1:
        print("\nTriângulo ESCALENO: três lados diferentes")
    else:
        print("\nTriângulo ISÓSCELES: quaisquer dois lados iguais")
else:
    print("\nNÃO É UM TRIÂNGULO")
