# @@@@@@@@@@@@
# CS1400 - MW 1
# Assignment 12

def main():
    valList = []
    userInput = True
    while userInput:
        userNum = input("Enter a Value: ")
        
        if userNum == "":
            break
        else:
            userNum = userNum.strip
            
            valList.append(userNum)
            
    print(valList)
    print("Number of Values Entered: " + str(len(valList)))
    
    maxVal(valList)
    print(valList)
    print("Max Value Entered: " + valList[len(valList) - 1])
  
# bubble sort 
def maxVal(valList):
    
   maxVal = valList[0]
   for num in valList:
       if maxVal < num:
           maxVal = num
   return maxVal
 
   
   
   

   
    
main()

