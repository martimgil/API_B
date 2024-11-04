numeros = list(range(0,20))
print("Lista inicial:", numeros)
par = []
impar = []

for i in numeros:
        if (i%2)== 0:
            par.append(i)
        else:
            impar.append(i)

print("\nLista PAR:", par)
print("\nLista ímpar", impar)
