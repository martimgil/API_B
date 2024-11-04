import math
import turtle
import random
print("Bem-vindo ao faz tudo!")
print("Seleciona a função que desejas!")
print("1- Calculadora Básica")
print("2 - Comparar números")
print("3 - Calcular IMC")
print("4 - Verificar o tipo de triângulo")
print("5 - Determinar o perimetro, area e o volume da esfera com o raio")
print("6 - Fazer lista com os pares e os impares")
print("7 - Tabuada")
print("8 - Fazer lista e verificar o maior e menor número inserido")
print("9 - Ler piadas")
print("10 - Desenhos")
print("11 - Jogo de acertar o número")
print("12 - Calcular a raiz de um número")
print("13 - Calcular a média de vários números")
print("14 - Calcular o fatorial de um número")
print("15 - Ver se um número é par ou impar")
print("16 - Calcular a proporção entre duas quantidades")
print("17 - Verificar se um número é positivo ou negativo")
print("18 - Verificar em que fase da vida uma pessoa vai")
print("19 - Acumular números até 100")
print("20 - Exponenciação numero a numero")
menu1 = int(input("Insere aqui a opção: "))
if menu1 == 1:
    n1 = int(input("Insira um número: "))
    n2 = int(input("Insira um número: "))
    operacao = input("Insere a operação: ")
    if operacao == "+":
        soma = n1 + n2
        print("O valor da soma é: ", soma)
    elif operacao == "-":
        subtracao = n1 - n2
        print("O valor da subtração é: ", subtracao)
    elif operacao == "*":
        multiplicacao = n1 * n2
        print("O valor da multiplicacao: ", multiplicacao)
    elif operacao == "/":
        divisao = n1 / n2
        print("O valor da divisão é: ", divisao)
    else:
        print("Operação Inválida!")
elif menu1==2:
    n1 = float(input("Insira um número:"))
    n2 = float(input("Insira um número"))
    if n1>n2:
        print("O {} é maior que o {}". format(n1, n2))
    elif n1<n2:
        print("O {} é memor que o {}".format(n1, n2))
    else:
        print("O {} é igual ao {}".format(n1,n2))
elif menu1 == 3:
    peso = float(input("Insira o seu peso"))
    altura = float(input("Insira a sua altura"))
    imc = peso / (altura ** 2) * 10000
    if imc<18.5:
        print("O seu IMC é {}. Abaixo do peso!" .format (imc))
    elif imc>19.6 and imc < 24.9:
        print("O seu IMC é {}. Saudável!".format(imc))
    elif imc>24.9 and imc <29.9:
        print("O seu IMC é {}. Peso em excesso!" .format (imc))
    else:
        print("O seu IMC é {}. Obesidade!" .format (imc))
elif menu1==4:
    n1 = int(input("Insira o valor do lado do triângulo: "))
    n2 = int(input("Insira o valor do lado do triângulo: "))
    n3 = int(input("Insira o valor do lado do triângulo: "))
    if (n1+n2)<n3:
        if n1 == n2 == n3:
            print ("Triangulo equilatero")
        elif n1 != n2 != n3:
            print("Triangulo escaleno")
        else:
            print("Triangulo isosceles")
    else:
        print("NÃO É TRIANGULO!!!")
elif menu1 == 5:
    r = input("Insira o valor do raio: ")
    p = 2*math.pi*r
    a = math.pi*r**2
    v = (4*math.pi*r**3)/3
    print("O valor do perimetro é {2f:.}" .format(p))
    print("O valor da área é {2f:.}".format(a))
    print("O valor do volume é {2f:.}".format(v))
elif menu1 == 6:
    par = []
    impar=[]
    numeros = list(range(0,10))
    print(numeros)
    for i in numeros:
        if (i%2)==0:
            par.append(i)
        else:
            impar.append(i)
    print("Números Pares:", par)
    print("Números Impares", impar)
elif menu1 == 7:
    n = int(input("Insira o valor da tabuada que pretende:"))
    for i in range(11):
        valor = i * n
        print("{} X {} = {}".format(n,i, valor))

elif menu1 == 8:
    lista = []
    quantidade  = int(input("Insira a quantidade de números que pretende inserir:"))
    for i in range(quantidade):
        n = int(input("Insira um número:"))
        lista.append(n)
    lista.sort()
    print(lista)
    print(min(lista))
    print(max(lista))

elif menu1 == 9:
    f = open("Piadas.txt", "+w")
    f.write("Qual é a diferença entre um peixe e um piano? Não se pode atum um peixe.\n")
    f.write("O que diz um cão quando vê um gato? Au au au, miau miau miau.\n")
    f.write("Porque é que o elefante não usa o computador? Porque tem medo do rato.\n")
    f.write("Como se chama um queijo que é um génio? Um queijus.\n")
    f.write(("O que é que o tomate disse para a alface? Vamos fazer uma salada.\n"))
    f.write("O que é que o café disse para o leite? Estou a precisar de um pouco de ti.\n")
    f.write("Como se chama um pássaro que sabe karaté? Um pássaro kiwi.\n")
    f.seek(0)
    print(f.read())

elif menu1 == 10:
    print("1 - Desnhar retangulo com quadrado no canto")
    print("2 - Logo Microsoft")
    print("3 - Desenhar um poligono personalizado")
    print("4 - Fazer meio circulo")
    print("5 - Fazer simbolo olimpico")
    menu_figuras = int(input("Insere a opção pretendida: "))
    if menu_figuras == 1:
        turtle.setup(500,500)
        turtle.title("RETÂNGULO COM QUADRADO NO CANTO")
        f1 = turtle.Turtle()
        f1.shape("turtle")
        f1.color("green", "green")
        f1.pensize(5)
        f1.penup()
        f1.setpos(0,0)
        f1.pendown()
        f1.forward(90)
        f1.left(90)
        f1.forward(45)
        f1.left(90)
        f1.forward(90)
        f1.left(90)
        f1.forward(45)
        f1.penup()
        f1.setpos(45,22.5)
        f1.pendown()
        f1.color("red","red")
        for i in range(4):
            f1.forward(45)
            f1.left(90)
        turtle.done()
    elif menu_figuras == 2:
        turtle.title("Microsoft")
        turtle.setup(800, 600)
        f2 = turtle.Turtle()
        f2.shape("turtle")
        f2.color("green", "green")
        f2.speed(100)
        f2.setpos(0, 0)
        f2.begin_fill()
        for i in range(4):
            f2.forward(100)
            f2.left(90)
        f2.end_fill()
        f2.penup()
        f2.setpos(-5,0)
        f2.color("red","red")
        f2.pendown()
        f2.begin_fill()
        for a in range(4):
            f2.back(100)
            f2.right(90)
        f2.end_fill()

        f2.penup()
        f2.setpos(-5,-5)
        f2.color("blue","blue")
        f2.pendown()
        f2.begin_fill()

        for b in range(4):
            f2.back(100)
            f2.left(90)
        f2.end_fill()

        f2.penup()
        f2.setpos(0,-5)
        f2.color("yellow","yellow")
        f2.pendown()
        f2.begin_fill()

        for c in range(4):
            f2.forward(100)
            f2.right(90)

        f2.end_fill()
        turtle.done()
    elif menu_figuras==3:
        turtle.title("Polígono personalizado")
        turtle.setup(800, 900)
        f3 = turtle.Turtle()
        f3.shape("turtle")
        f3.color("green", "green")
        f3.speed(1000)
        f3.penup()
        f3.setpos(0,0)
        f3.pendown()
        lados = int(input("Insira o número de lados que pretende inserir: "))
        angulos = 360/lados
        f3.begin_fill()
        for d in range(lados):
            f3.forward(100)
            f3.left(angulos)
        f3.end_fill()
        turtle.done()
    elif menu_figuras == 4:
        turtle.title("Meia Circunferencia")
        turtle.setup(800,900)
        f4 = turtle.Turtle()
        f4.color("green", "green")
        f4.shape("turtle")
        f4.penup()
        f4.setpos(0,0)
        f4.pendown()
        f4.circle(40,180)
        turtle.done()
    elif menu_figuras == 5:
        turtle.title("Anéis Olímpicos")
        turtle.setup(900,900)
        f5 = turtle.Turtle()
        f5.penup()
        f5.setpos(0,0)
        f5.pendown()
        f5.pensize(20)
        f5.shape("turtle")
        f5.color("black", "black")
        f5.circle(80, 360)
        f5.penup()
        f5.setpos(200,0)
        f5.pendown()
        f5.color("red", "red")
        f5.circle(80,360)
        f5.penup()
        f5.setpos(100,-80)
        f5.color("green","green")
        f5.pendown()
        f5.circle(80,360)


        turtle.done()
    else:
        print("Opção Inválida")
elif menu1 == 11:
    numero = random.randint(0,100)
    erros = 0
    palpite = 0
    while palpite is not numero:
        palpite = int(input("Insere o teu palpite: "))
        erros = erros + 1
        if palpite > numero:
            print("O seu palpite é maior que o número correto! ")
        else:
            print("O seu palpite é memor que o número correto!")
    print("Parabéns! Acertou no número com {} erros. O número correto é o {}".format(erros, numero))
elif menu1 == 12:
    n = float(input("Insira o número: "))
    valor = math.sqrt(n)
    print("O valor da raiz de {} é {2f:.}".format(n, valor))

elif menu1 == 13:
    n1 = int("Insira a quantidade de números que pretende inserir: ")
    soma = 0
    for i in range(n1):
        n2 = int(input("Insira um número: "))
        soma = soma + n2
    media = soma/n1
    print("O valor da média é:", media)
elif menu1 == 14:
    n = int(input("Insira o número que pretende calcular: "))
    a = n
    fat = n
    while n>1:
        n = n-1
        fat = n*fat

    print("{}! = {} " .format(a, fat))
elif menu1 == 15:
    n1 = int(input("Insira um número: "))
    def par_impar(n1):
        if (n1%2) == 0:
            return print("O número {} é par! " .format(n1))
        else:
            return print("O número {} é impar! " .format(n1))
    par_impar(n1)
elif menu1 == 16:
    n1 = int(input("Insere a primeira quantidade"))
    n2 = int(input("Insere a segunda quantidade"))
    total = n1 + n2
    valor1 = (n1/total)*100
    valor2 = (n2/total)*100
    print("A proporção do valor {} corresponde a {}% e do valor {} corresponde a {}%. Total de casos: {}".format(n1, valor1, n2, valor2,))
    if valor1 > valor2:
        print("A primeira percentagem é maior!")
    else:
        print("A segunda percentagem é menor!")
    media = (n1 + n2)/2
    print("A média é", media)
elif menu1 == 17:
    n1 = float(input("Insira um número: "))
    if n1 > 0:
        print("O {} é positivo!" .format(n1))
    elif n1 < 0:
        print("O {} é negativo!" .format(n1))
    else:
        print("O número é um zero!")
elif menu1 == 18:
    nome = str(input(("Insira o nome: ")))
    idade = int(input("Insira a idade: "))
    if idade<0 or idade>120:
        print("Idade Inválida!")
    elif idade>=0 and idade<=11:
        print("{}, está na infancia!".format(nome))
    elif idade>=12 and idade<=20:
        print("{}, está na adolescencia!".format(nome))
    elif idade>=21 and idade<75:
        print("{}, está na fase adulta!".format(nome))
    else:
        print("{}, está na velhice" .format(nome))
elif menu1 == 19:
    acum = 0
    while acum<100:
        n = int(input("Insira um número: "))
        acum = acum + n
    print("O valor acumulado foi {}" .format(acum))
elif menu1 == 20:
    def exp1 (n1, n2):
        v1 = n1**n2
        v2 = n2**n1
        return print(v1,v2)
    n1 = int(input("Insira um número: "))
    n2 = int(input("Insira um número: "))
    exp1(n1,n2)

else:
    print("Opção Inválida!")
