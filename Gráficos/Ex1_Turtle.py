import turtle

#Titulo da janela
turtle.title("Turtle - APLICAÇÕES INFORMÁTICAS B - Python")

#tamanho da janela (in pixeis - 425 x 425)
#posição da janela (0,0)
turtle.setup(500,300,600,300)


apiTurtle = turtle.Turtle()

apiTurtle.penup() #Caneta levantada, nao desenhamos
apiTurtle.setpos(-100,-50) #Posicionar a turtle
apiTurtle.pendown() #baixa a caneta para escrever

apiTurtle.color("green","yellow") #Dar cor
apiTurtle.shape("turtle") #Dar forma
apiTurtle.pensize(5)

apiTurtle.forward(200) #Andar para a frente
apiTurtle.left(90)
apiTurtle.forward(100)
apiTurtle.left(90)
apiTurtle.forward(200)
apiTurtle.left(90)
apiTurtle.forward(100)

apiTurtle.color("blue", "yellow")
apiTurtle.penup()
apiTurtle.setpos(0,0)
apiTurtle.pendown()
apiTurtle.left(90)
apiTurtle.forward(150)
apiTurtle.left(90)
apiTurtle.forward(150)
apiTurtle.left(90)
apiTurtle.forward(150)
apiTurtle.left(90)
apiTurtle.forward(150)

turtle.done()
