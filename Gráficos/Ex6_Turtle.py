import turtle

def circunferencia(cor, x, y, vel, raio):
    for angulo in range(0,360,15):
        turtle.setpos(x, y)
        turtle.color(cor)
        turtle.speed(100)
        turtle.circle(raio)
turtle.setpos(0,0)

circunferencia("red",0,0,1000,100)
circunferencia("red",0,0,1000,40)
circunferencia("black",-100, 0, 100,40)
circunferencia("green", 0, -100,1000, 40)
circunferencia("gray", 100, 0, 1000, 40)
circunferencia("blue", 0, 100, 1000, 40)
turtle.setpos(-100,0)

turtle.done()