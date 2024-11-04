import random
quantidade_erros = 0

numero_correto = random.randint(0,100)

while True:
    palpite = int(input("\nInsira o seu palpite: "))

    if numero_correto == palpite:
        print("\nParabéns acertou com {} tentativas. O número correto é {}!" .format(quantidade_erros, numero_correto))
        break
    else:
        quantidade_erros = quantidade_erros + 1
        print("\nErrou, tente novamente! Tem {} erro(s)" .format(quantidade_erros))
        if palpite > numero_correto:
            print("\nO valor é inferior ao {} ".format(palpite))
        else:
            print("\nO valor é superior ao {}" .format(palpite))

#quantidade_erros=0
#palpite=0
#numero_correto = random.randit(0,100)
#while palpite is not numero_correto:
    #palpite = int(input("Insira o seu palpite: ")
    #if palpite > numero_correto
        #print("O valor é menor que o {}".format(palpite)
        #quantidade_erros = quantidade_erros + 1

    #else:
        #print("O valor é maior que o {}" .format(palpite)
        #quantidade_erros = quantidade_erros + 1
#print("Parabens! O número é {} com {} tentativas" .format(numero_correto, quantidade_erros)
