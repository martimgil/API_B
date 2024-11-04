numeros = []

for i in range(5):
    n = int(input("Insira um número para a lista: "))
    numeros.append(n)
print("\n", numeros)
numeros.sort()
print("\n", numeros)

print("\nMenor nº=", numeros[0])

print("\nMaior nº=", numeros[4])
