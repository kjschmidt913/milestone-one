board = [
    ["  ", "1", " ", "2", " ", "3"],
    ["1 "," ","|"," ","|"," "],
    ["  ","-","-","-","-","-"],
    ["2 "," ","|"," ","|"," "],
    ["  ","-","-","-","-","-"],
    ["3 "," ","|"," ","|"," "]
]

def printBoard():
    print("\n")
    for row in board:
        for spot in row:
            print(spot, end="") 
        print(" ")
    print("\n")

def adjustToList(colRow):
    #adjusting row number
        #3 always == 5
        #2 always  == 3
        #1 always == 1
    if (colRow[1] == 3):
        colRow[1] = 5
    elif(colRow[1] == 2):
        colRow[1] = 3
    #adjusting column number
    if (colRow[0] == 3):
        colRow[0] = 5
    elif(colRow[0] == 2):
        colRow[0] = 3
    return colRow

def placeOnBoard(position, player):
    if (board[position[1]][position[0]] == " "):
        board[position[1]][position[0]] = player
        printBoard()
        if player == playerOne:
            print("Player Two's Turn!")
        else:
            print("Player One's Turn!")
    else:
        playerOneChoices.pop()
        print("That spot already has a marker. Please choose again")

def validInput(col, row):
    return int(row) in range(1, 4) and int(col) in range(1, 4)


#Game playing starts here
playerOne = " "

while(playerOne != "X") and (playerOne != "O"):
    playerOne = input("Player One, choose either X or O for your marker: ")
    if playerOne == "X":
        playerTwo = "O"
    elif playerOne == "O":
        playerTwo = "X"
    else:
        print("Not a valid marker. Please choose again.")
        continue
    
    print(f"Player Two, your marker is {playerTwo}")


printBoard()

playerOneChoices = []
playerTwoChoices = []


def choose():
    winner = False
    totalTurns = 0
    while (not winner):
        if totalTurns >= 6:
            checkWinner()

        print("Choose your spot by entering the column number then the row number.")
        choiceColumn = input("Column Number: ")
        choiceRow = input("Row Number: ")

        if not validInput(choiceColumn, choiceRow):
            print("Invalid space. Please enter valid numbers")
            continue

        #if it's player one
        if (len(playerOneChoices) == len(playerTwoChoices)):
            playerOneChoices.append([int(choiceColumn), int(choiceRow)])
            boardposition = adjustToList(playerOneChoices[-1])         
            #placing on board
            placeOnBoard(boardposition, playerOne)
            continue
        
        #if it's player two
        else:
            playerTwoChoices.append([int(choiceColumn), int(choiceRow)])
            boardposition = adjustToList(playerTwoChoices[-1])
            #placing on board
            placeOnBoard(boardposition, playerTwo)
            continue

        
choose()

def checkWinner():
    print("hi")