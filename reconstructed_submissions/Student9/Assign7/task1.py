# @@@@@@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 7


num = int(input("How many rows would you like?"))

def main():
    
    def makeNumberPyramid(num):
        r=1
        for i in range(0,num):
            line = 0
            row = ""
            line = len(str(num))
            line1 = (line * num)
            line2 = line1 + (num - 1)
            
            r1 = len(str(i))
            r2 = r1*(i+1)
            r3 = r2+(i)
            if r == 10:
                r3=r3+10
            
            for b in range((line2-r3)//2):
                row += " "
            for l in range(0,i+1):
                if ((i+1)==num):
                    row += str(i+1)
                    if (l==i):
                        row+= ""
                    else:
                        row+= " "


                else:

                    row += " "
                    row += str(i+1)
            r+=1  
            print(row)
    print(makeNumberPyramid(num))
print(main())
