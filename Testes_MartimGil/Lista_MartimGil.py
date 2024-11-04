print("\n--- PROGRAMA PARA INSERIR NÚMEROS NUMA LISTA VAZIA, MOSTRA LISTA E ORDENA-A --- ")
quantidade = int(input("\nQuantos números pretende inserir: "))
lista = []
for i in range (quantidade):
    n = int(input("Insira um número: "))
    lista.append(n)
print("LISTA INICIAL :",lista)
lista.sort()
print("LISTA ORDENADA: ",lista)
