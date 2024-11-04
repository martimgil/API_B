print("\nVERIFICA SE É UM TRIÂNGULO ---> EQUILÁTERO, ISÓSCELES OU ESCALENO")
l1 = float(input("\nInsira um dos lados do triângulo: "))
l2 = float(input("\nInsira um dos lados do triângulo: "))
l3 = float(input("\nInsira um dos lados do triângulo: "))

if (l1 + l2 < l3) or (l2 + l3 < l1) or (l1 + l3 < l2):
    print("\nNÃO É UM TRIÂNGULO")
elif l1 == l2 == l3:
    print("\nTriângulo EQUILÁTERO: três lados iguais")
elif l1 != l2 != l3:
    print("\nTriângulo ESCALENO: três lados diferentes")
else:
    print("\nTriângulo ISÓSCELES: quisquer dois lados iguais")
