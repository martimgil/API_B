#Calcular IMC

print("---------- CALCULAR IMC ---------")
peso = float(input("\n\t o peso em kg: "))
altura = float(input("\n\tInsira a sua altura em cm: "))
imc=peso/(altura**2)*10000

if imc<18.5:
    print("\n\tO seu IMC é {}. Abaixo do peso!" .format(imc))
elif imc>18.6 and imc<24.9:
    print("\n\tO seu IMC é {}. Saudável!" .format(imc))
elif imc>24.9 and imc<29.9:
    print("\n\tO seu IMC é {}. Peso em excesso!" .format(imc))
else:
    print("\n\tO seu IMC é {}. Obesidade!" .format(imc))
