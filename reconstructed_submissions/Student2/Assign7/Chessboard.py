import turtle

#setup
def setup():
    #speed up
    turtle.speed(0)
    #setup window size 1000 x 800
    turtle.setup(1000,800)
#ersase the scree
def reset():
    turtle.reset()
    turtle.speed(0)
    turtle.color("blue")
    

def drawChessboard(startX,startY, width=200, height=200):
    turtle.penup()
    turtle.color("blue")
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)

def drawAllRectangles():
    turtle.color("black")
    turtle.filcolor("black")
    
def drawRectangle():
    
        
    turtle.done()
