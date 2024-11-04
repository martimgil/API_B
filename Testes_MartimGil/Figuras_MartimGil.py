import turtle
print("\n---DESENHA FORMAS GEOMÉTRICAS---")

turtle.title("---DESENHA FORMAS GEOMÉTRICAS---")
turtle.setup(700,500, 600, 200)
f1 = turtle.Turtle()
f1.shape("turtle")
f1.pensize(4)
f1.color("blue", "blue")
forma = str(input("\nQual a forma geométrica que pretende desenhar: "))

if forma == "quadrado" or forma == "QUADRADO" or forma == "Quadrado":
    tamanho = int(input("Insira o tamanho do lado: "))
    for i in range(4):
        f1.forward(tamanho)
        f1.left(90)
elif forma == "retângulo" or forma == "RETÂNGULO" or forma == "Retângulo":
    base = int(input("Insira a base: "))
    altura = int(input("Insira a altura: "))
    f1.forward(base)
    f1.left(90)
    f1.forward(altura)
    f1.left(90)
    f1.forward(base)
    f1.left(90)
    f1.forward(altura)
elif forma == "círculo" or forma == "CÍRCULO" or forma == "Círculo":
    raio = int(input("Insira o valor do raio: "))
    f1.circle(raio, 360)
else:
    print("\nATENÇÃO!!! INSERIU FORMA GEOMÉTRICA INVÁLIDA. ")
turtle.done()