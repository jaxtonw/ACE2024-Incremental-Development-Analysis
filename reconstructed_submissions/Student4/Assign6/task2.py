# @@@-@@@@@@@-Assn6
# CS1400 - 14 week
# task 2

# I chose to use main function to be able to accurately run code again
# I found that using break and continue in the final if statement 
# did not give me accurate results
def main():
    # import module needed
    import random

    # setting up the variables to measure each night
    totalNights = 0
    # one will be used for if one elephant is in the pen
    one = 0
    # both will be used for if both elephants are in the same pen
    both = 0
    # none will be used for if no elephants are in the pen zookeeper checks
    none = 0

    # while loop to use as main loop
    while True:

        # for loop in range of 100,000 nights
        for night in range(0, 100000):
            # giving random values for each elephant's pen and zookeeper.
            # pens of random between 1 and 6
            elephant1 = random.randint(1, 6)
            elephant2 = random.randint(1, 6)
            zookeeper = random.randint(1, 6)

            # if statement for if both elephants are in the same pen
            if zookeeper == elephant1 and zookeeper == elephant2:
                totalNights += 1
                both += 1
            # if-else-if statement for if at least one elephant is in the same pen
            elif zookeeper == elephant1 or zookeeper == elephant2:
                totalNights += 1
                one += 1
            # final else statement for if neither are in the same pen
            elif zookeeper != elephant1 and zookeeper != elephant2:
                totalNights += 1
                none += 1

        # print statement and percentage for at least one elephant
        # one / totalNights gives value * 100 gives percent
        print("Percentage for at least one elephant in pen ", end=" ")
        one /= totalNights
        one *= 100
        print(format(one, ".2f") + "%")
        # print statement and percentage for at least one elephant
        # both / totalNights gives value * 100 gives percent
        print("Percentage for both elephants in pen ", end=" ")
        both /= totalNights
        both *= 100
        print(format(both, ".2f") + "%")

        # if statement to calculate who was right
        # 1/6 of 1/3 = 1/18 == 5.5% - gave 2% margin of error
        # 1/3 == 33.33% - gave 2% margin of error
        if 7.5 > both > 3.5 and 35 > one > 31:
            print("The Zookeeper is correct. ")
        else:
            print("The Custodian is correct. ")

        # gather user input for repeat of simulation
        answer = input("\nWould you like to run program again? (Yes or No) ")
        # gather any form of yes and enter it as yes
        if answer.lower() == "yes":
            main()
        else:
            exit()


# calling main will truly run program again            
main()










)
 
