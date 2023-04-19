from random import randint

from random import randint

runAgain = "true"

while runAgain:

    samePen = 0
    notSamePen = 0
    zookeeperSawAtLeastOne = 0
    zookeeperSawBoth = 0
    for nightNumber in range(1, 100001):
        elephant1 = randint(1, 6)
        elephant2 = randint(1, 6)
        zookeeperCheck = randint(1, 6)
    # print("Nightnumber" + str(nightNumber))
    # print("elephant1 pen # " + str(elephant1))
    # print("elephant2 pen # " + str(elephant2))
    # print("Zookeeper Check # " + str(zookeeperCheck))

        if zookeeperCheck == elephant1:
            zookeeperSawAtLeastOne += 1
            if zookeeperCheck == elephant2:
                zookeeperSawBoth += 1

        elif zookeeperCheck == elephant2:
            zookeeperSawAtLeastOne += 1

# print("saw both " + str(zookeeperSawBoth))
# print("saw at least one " + str(zookeeperSawAtLeastOne))

    percentSawAtLeastOne = (zookeeperSawAtLeastOne / 100000)
    percentSawBoth = (zookeeperSawBoth / zookeeperSawAtLeastOne)
    print("Percentage the Zookeper saw at least one elephant when he checks: " + str(
        (round((percentSawAtLeastOne * 100), 2))))
    if (percentSawAtLeastOne * 100) < 31.33:
        print("Zookeeper's guess was not accurate.")
    print("percentage the zookeeper saw both of the elephants when he saw at least one : " + str(
        (round((percentSawBoth * 100), 2))))

    runit = str(input("Do you wanna run it again? (Yes or No):"))
    
    if runit.upper() != "YES":
        break
        
        
    
        

    


