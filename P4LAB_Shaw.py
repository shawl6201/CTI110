#This program is intended to command the turtle to
#create a snowflake through a nested loop.
#October 20, 2018
#CTI-110 P4LAB- Snowflakes
#Snowflakes
#Leslie Shaw

def main ():
    #Open turtle program and change background color
    import turtle
    wn = turtle.Screen()
    wn.bgcolor("blue")

    #Name turtle and define its color, pen size, shape, and speed
    tortie = turtle.Turtle()
    tortie.color("white")
    tortie.pensize(3)
    tortie.shape("arrow")
    tortie.speed(2)

    #Create the polygon shape
    for i in range(4):
        tortie.right(45)
        tortie.forward(45)
        tortie.right(45)
    tortie.left(90)
    tortie.forward(50)

    #create the branches for the snowflakes and
    #have it move around the polygon
    def branch():
        for i in range(3):
            for i in range(3):
                tortie.forward(30)
                tortie.backward(30)
                tortie.left(45)
        tortie.left(135)
        tortie.forward(50)
        tortie.left(45)
        tortie.forward(45)
        tortie.left(45)
        tortie.forward(50)
    for i in range(4):
        branch()
        
main()
