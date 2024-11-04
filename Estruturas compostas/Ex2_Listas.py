nomes = ["Martim", "Afonso", "Diana", "Leonel", "Theo"]

nomes.insert(2, "Beatriz")

nomes.insert(6,"Guilherme")

print("\n", nomes)

for i in nomes:
    if i == "Leonel":
        nomes.remove("Leonel")
        print("\nNome encontrado na lista e vai ser removido")
        print("\n", nomes)

nomes.sort()
print("\n", nomes)