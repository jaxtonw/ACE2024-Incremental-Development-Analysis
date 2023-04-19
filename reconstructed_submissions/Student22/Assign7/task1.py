# @@@@@@@@@@@  
# CS 1400 - MW1 XL
# Assignment 007

# here is the definition for the pyramid program
def pyramid(rows):
    # this program uses 2 loops
    # j is the column and i is the row
    for j in range(1, rows + 1):
        rowMsg = ""
        for i in range(1, rows + 1):
            # when the msg is smaller than j the program needs to add in another msg
            if len(rowMsg)/2 < j < 10:
                rowMsg += str(j)
                rowMsg += " "
            # since the function works on length, numbers with more than 1 char breaks the logic
            # every time 9 is printed the char count increases by 1 but when 10 is printed char count
            # increases by 2, so the extra conditional accounts for tha
            elif 9 < j > len(rowMsg)/3:
                rowMsg += str(j)
                rowMsg += " "
            else:
                # the idea is the same here as it was for the previous set of logic
                # 10 kind of ruins things so the conditional here accounts for that
                if rows < 10:
                    rowMsg = format(rowMsg, "^" + str(rows * 2))
                else:
                    rowMsg = format(rowMsg, "^" + str(rows * 3))
        print(rowMsg)
        

# here is the main function, really complex this one

def main():
    rows = eval(input("Enter the number of rows"))
    pyramid(rows)
    
    
main()

