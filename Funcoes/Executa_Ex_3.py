import Ex_3

while True:
    opcao = input("\nQual a função que pretende executar? (c)comparar número e (p) para verificar se par ou ímpar: ")

    if opcao == "C" or opcao == "c":
        n1 = int(input("\nInsira o 1º número: "))
        n2 = int(input("Insira o 2º número: "))
        Ex_3.compara(n1, n2)

    elif opcao == "P" or opcao == "p":
        n = int(input("Insira o 1º número: "))
        Ex_3.par_impar(n)

    else:
        print("Opção Inválida!")
