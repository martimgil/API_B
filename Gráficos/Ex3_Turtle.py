import turtle

turtle.title("APLICAÇÕES INFORMÁTICAS B - TURTLE")
turtle.setup(400,400)
turtle.Turtle
turtle.shape("turtle")
turtle.pensize(3)
turtle.color("green","green")
turtle.penup()
turtle.setpos(0,0)
turtle.pendown()
turtle.begin_fill()

for a in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.color("red","red")
turtle.setpos(-5,0)
turtle.pendown()
turtle.begin_fill()

for i in range(4):
    turtle.left(90)
    turtle.forward(100)
turtle.end_fill()

turtle.penup()
turtle.color("yellow")
turtle.setpos(0,-5)
turtle.pendown()
turtle.begin_fill()

for b in range (4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.color("blue","blue")
turtle.setpos(-5,-5)
turtle.pendown()
turtle.begin_fill()

for c in range (4):
    turtle.right(90)
    turtle.forward(100)
turtle.end_fill()

turtle.done()