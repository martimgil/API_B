n1 = float(input("Insira a medida de um dos lados do triângulo: "))
n2 = float(input("Insira a medida de outro dos lados do triângulo: "))
n3 = float(input("Insira a medida de outro dos lados do triângulo: "))

if n1 == n2 and n2 == n3:
    print("O triangulo é equilátero! ")
elif n1 != n2 and  n2!=n3 and n3!=n1:
    print("O triangulo é isosceles!")
else:
    print("O triangulo é escaleno! ")