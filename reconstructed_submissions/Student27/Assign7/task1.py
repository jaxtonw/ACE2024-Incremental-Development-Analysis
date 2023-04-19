# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

def makeNumberPyramid():
    # Get input
    numRows = eval(input("Enter the number of rows: "))
    
    #string variable
    msg = ""
    
    #loop 
    msg += "\n"
    for i in range(1,numRows +1):
        numSpace = numRows - i 
        msg +=format("","^" +str(numSpace) )
        
        for j in range(1,i +1):
            numDigits = 3
            msg +=(format(i,"^" + str(numDigits)))
        msg += "\n"
       
    print(msg)

#Call function
makeNumberPyramid()


