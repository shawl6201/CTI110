#This program is to open the turtle program and
#provide instructions to create shapes

#Open turtle program and change background color
import turtle
wn = turtle.Screen()
wn.bgcolor("hotpink")

#Name turtle and define its color, pen size, and shape
tortie = turtle.Turtle()
tortie.color("white")
tortie.pensize(5)
tortie.shape("turtle")

#Turtle creates a square
for i in [0,1,2,3]:
    tortie.forward(100)
    tortie.left(90)

#Turtle moves to another area and creates a triangle
tortie.penup()
tortie.forward(-100)
tortie.pendown()

for i in [0,1,2]:
    tortie.left(-120)
    tortie.forward(100)

wn.mainloop()
