from modules.memoryboard import MemoryBoard


def main():
    playerTurn = 0  # Keep track of whose turn it is
    print("Welcome to Memory\n")
    # Get the Board Size
    cols = int(input("Enter the number of columns on the board: "))
    rows = int(input("Enter the number of rows on the board: "))
    # Get the number of players
    playerCount = int(input("Enter the number of players: "))
    scores = [0] * playerCount
    # Create the MemoryBoard object
    memoryBoard = MemoryBoard(rows, cols)
    # Game loop
    winner = False
    while not winner:
        selectedCards = []  # Track the cards the current player selected
        printGameBoard(scores, memoryBoard.getBoard())
        # Each turn is two card flips
        for i in range(2):
            xPos, yPos = eval(input("Player " + str(playerTurn + 1) + " choose a card to flip: "))
            selectedCards.append([xPos, yPos])
            memoryBoard.flipCard(xPos, yPos)
            printGameBoard(scores, memoryBoard.getBoard())
        # Player goes again if they get a match
        if memoryBoard.isMatch(selectedCards[0], selectedCards[1]):
            print("You got a match!")
            scores[playerTurn + 1] += 1
            winner = sum(scores) == cols * rows / 2
            # If the game is over show a different message
            if winner:
                print("All matches have been found!")
            else:
                input("Player " + str(playerTurn + 1) + " hit Enter to go again.")
        else:
            memoryBoard.flipCard(selectedCards[0][0], selectedCards[1][0])
            memoryBoard.flipCard(selectedCards[0][1], selectedCards[1][1])
            print("No Match")
            playerTurn += 1
            if playerTurn == playerCount:
                playerTurn = 0
            input("Hit Enter for Player " + str(playerTurn + 1))
    # Find the winning score value
    highScore = max(scores)
    # Check for a tie/winner
    if scores.count(highScore) > 1:
        print("The following players tied: ", end="")
        for i in range(len(scores)):
            if scores[i] == highScore:
                print(i, end=" ")
    else:
        print("The winner is player " + str(scores.index(highScore) + 1))
# Print the scoreboard and gameboard


def printGameBoard(scores, board):
    for i in range(len(scores)):
        print("Player " + str(i + 1) + ": " + str(scores[i]))
    print()
    print(board)


main()

