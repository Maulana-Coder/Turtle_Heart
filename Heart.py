import turtle
import time

turtle.title("Heart - Maulana ID")
turtle.bgcolor("black")
turtle.pensize(2)

def curve():
    for x in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(0)
turtle.color("red", "pink")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

def font():
    turtle.color("pink", "red")
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-125, -50)
    turtle.write("Onii-Chan Daisuki", font=("Consolas", 20, "bold",))
    turtle.penup()
    turtle.hideturtle()
font()

time.sleep(1)

def credits():
    turtle.color("white")
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-100, -250)
    turtle.write("   Created\nBy Maulana ID", font=("Consolas", 20, "bold",))
    turtle.penup()
    turtle.hideturtle()
credits()
