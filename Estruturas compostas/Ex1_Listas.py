numeros =[10, 20, 30, 40]

print(numeros)

for x in numeros:
    print(x)

numeros.append(50)
numeros.append(70)

print(numeros)

numeros.insert(0,0)
print(numeros)

numeros.insert(3,25)
print(numeros)

numeros.remove(25)
print(numeros)


numeros.insert(1, 80)
numeros.insert(3,200)

print(numeros)

numeros.sort()

print(numeros)

numeros.sort(reverse=True)

print(numeros)
