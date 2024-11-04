import turtle

turtle.title("Exemplo 2 - Desenhar Polígono")
turtle.setup(1920,1080)
a = turtle.Turtle()
a.shape("turtle")
a.pensize(3)
a.color("green","green")
a.penup()
a.setpos(0,0)
a.pendown()

lados = int(input("Quantos lado tem o polígono?"))
tam = int(input("Qual o tamanho dos lados do poligono?"))
angulo = 360/lados


for i in range(lados):
    a.forward(tam)
    a.left(angulo)

turtle.done()