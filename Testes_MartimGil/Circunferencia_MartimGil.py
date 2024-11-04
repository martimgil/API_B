import math
pi = math.pi
print("\nPrograma para calcular o PERÍMETRO, a ÁREA da Circunferência e o VOLUME da Esfera")
r = int(input("\nInsira o valor do raio: "))
p = 2*pi*r
a = pi*r**2
v = (4*pi*r**3)/3

# Faz os arredondamentos das variaveis com duas casas decimais
p = round(p, 2)
a = round(a, 2)
v = round(v, 2)

print("\nO Perímetro da circunferência é ", p)
print("A área da Circunferência é ", a)
print("O Volume da Esfera é ", v)
