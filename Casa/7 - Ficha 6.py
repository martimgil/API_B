n1 = int(input("Insira um número: "))

n2 = 0

for i in range(10):
    n1 = n1 + 0.5
    print(n1)
    n2 = n2 + n1
print("Soma: ", n2)