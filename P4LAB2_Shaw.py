#This activity is to create intitials "LS"
#using the turtle program.

#Open turtle program and change background color
import turtle
wn = turtle.Screen()
wn.bgcolor("purple")

#Name turtle and define its color, pen size, shape, and speed
tortie = turtle.Turtle()
tortie.color("yellow")
tortie.pensize(3)
tortie.shape("arrow")
tortie.speed(2)

#Turtle creates the letter "L"
tortie.left(-90)
tortie.forward(100)
tortie.left(90)
tortie.forward (50)

#Turtle moves to another area and creates a triangle
tortie.penup()
tortie.forward(80)
tortie.left(90)
tortie.forward (100)
tortie.pendown()

#Turtle creates the letter "S"
tortie.left(90)
tortie.forward(30)

for i in [0,1,2]:
    tortie.left(45)
    tortie.forward(20)

tortie.left(45)
tortie.forward(30)

for i in [0,1,2]:
    tortie.right(45)
    tortie.forward(20)

tortie.right(45)
tortie.forward(30)

wn.mainloop()
