# @@@@@@@@@@@@@@@
# CS 1400- 14 week
# Assignment 9

class Blobber:
    def __init__(myBlobber,name,color, radius,height):
        myBlobber.__radius = radius
        myBlobber.__height = height
        myBlobber.__color = color
        myBlobber.__name = name
        
    def displayName(myBlobber):
        return str(myBlobber.__name.capitalize())
       
    def changeName(myBlobber, name):
        myBlobber.__name = name
        
    def displayColor(myBlobber,):
        return str(myBlobber.__color.capitalize())
        
    def changeColor(myBlobber, color):
        myBlobber.__color = color
        
    def feedBlobber(myBlobber):
        
    def blobberSpeak(myBlobber):
        print("My name is, " + myBlobber.__name + "and I am " + myBlobber.__color)
        print()
        
    def vitalsOk(myBlobber,radius,height):
        
