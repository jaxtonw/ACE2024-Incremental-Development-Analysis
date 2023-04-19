from random import randint
running = True
while running:
    case1 = 0
    case2 = 0
    case3 = 0
    
    for i in range(1, 100001):
        elephant1 = randint(1, 6)
        elephant2 = randint(1, 6)
        zooKeeper = randint(1, 6)
        if elephant1 == zooKeeper or elephant2 == zooKeeper:
            case1 += 1
        if elephant2 == zooKeeper and elephant1 == zooKeeper:
            case2 += 1
        else:
            case3 += 1
    report1 = case1 / 100000
    report2 = case2 / case1
    percent1 = report1 * 100
    percent2 = report2 * 100
    print("The zookeeper found an elephant in a stall %.2f" % percent1, "% of the time.)"
    print("The Zookeeper found both elephants in a stall %.2f" % percent2, "% of the time.")
    if .31 <= case1 <= .35 and .14 <= case2 <= .18:
        print("The Zookeeper was correct. Silly Custodian.")
    else:
        print("The Custodian was correct. Silly Zookeeper.")
    userInput = input("Want to try again? (Yes / No): ").lower()
    if userInput == "yes":
        continue
    else:
        break
        
