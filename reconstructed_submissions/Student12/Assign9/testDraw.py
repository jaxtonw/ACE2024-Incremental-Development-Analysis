# @@@@@@@@@@@@
# CS1400 - 001
# Assignment 9

import turtle

def drawHead():
    turtle.pu()
    turtle.goto(0, -100)
    turtle.pencolor("black")
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.pd()
    turtle.circle(100)
    turtle.end_fill()
    turtle.pu()


# draws both eyes        
def drawEyes():
        le.goto(-30, 30)
    turtle.pd()
    turtle.circle(            le.p        turtle.goto(30, 30)
    turtle.pd()
        le.circle(10)
    turtle.pu()
     
#    
def drawMouth():
    #turtle.goto(-50, -20)
    turtle.width(10)
    turtle.pencolor("black")
    #turtle.right(90)
    #turtle.pd()
    #turtle.circle(50, 180)
    turtle.pu()
    turtle.goto(50, -50)
    turtle.left(90)
    turtle.pd()
    turtle.circle(50, 180)     
   w_face():
    turtle.clear()
    drawHead()
    drawEyes()
    drawMouth()
    
draw_face()

turtle.exitonclick()
turtle.done()

