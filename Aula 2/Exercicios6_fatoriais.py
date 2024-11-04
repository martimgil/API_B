#Calcular um fatorial

print("\n --- CALCULAR FATORIAL DE UM NÚMERO ---")
n1 = int(input("Insira um número inteiro maior do que 1: "))
a=n1
fat = n1
while n1 > 1:
    n1 = n1-1
    fat = fat*n1
print("\nO valor do", a, "fatorial é:", fat)

#print("\n --- CALCULAR FATORIAL DE UM NÚMERO ---")
# n1 = int(input("Insira um número inteiro maior do que 1: "))
#fat=n1

#for i in range(1,n1,1):
 #   fat=fat*i
#print("O VALOR É", fat)