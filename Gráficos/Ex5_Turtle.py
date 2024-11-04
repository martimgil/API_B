import turtle

def circunferencia (cor, x, y, veloc, raio):
    for angle in range (0,360,15):
        turtle.goto(x,y)
        turtle.color(cor)
        turtle.left(angle)
        turtle.speed(veloc)
        turtle.circle(raio)
turtle.reset()

circunferencia("red", 0, 0, 100, 100)
circunferencia("black", -100, 0, 100, 40)
circunferencia("green", 0, -100, 100,40)
circunferencia("grey", 100, 0, 100,40)
circunferencia("blue", 0, 100, 100,40)
turtle.done()