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
    while (not winner):
        print("Choose your spot by entering the column number then the row number.")
        choiceColumn = input("Column Number: ")
        choiceRow = input("Row Number: ")

        if (not int(choiceRow) in range(1, 4)) or (not int(choiceColumn) in range(1, 4)):
            print("Invalid space. Please enter valid numbers")
            continue

        #if it's player one
        if (len(playerOneChoices) == len(playerTwoChoices)):
            playerOneChoices.append([int(choiceColumn), int(choiceRow)])
            #adjusting row number
            #3 always == 5
            #2 always  == 3
            #1 always == 1
            if (playerOneChoices[-1][1] == 3):
                playerOneChoices[-1][1] = 5
            elif(playerOneChoices[-1][1] == 2):
                playerOneChoices[-1][1] = 3
            #adjusting column number
            if (playerOneChoices[-1][0] == 3):
                playerOneChoices[-1][0] = 5
            elif(playerOneChoices[-1][0] == 2):
                playerOneChoices[-1][0] = 3
            #placing on board
            if (board[playerOneChoices[-1][1]][playerOneChoices[-1][0]] == " "):
                board[playerOneChoices[-1][1]][playerOneChoices[-1][0]] = playerOne
                printBoard()
                print("Player Two's Turn!")
            else:
                playerOneChoices.pop()
                print("That spot already has a marker. Please choose again")
                continue
        
        #if it's player two
        else:
            playerTwoChoices.append([int(choiceColumn), int(choiceRow)])
            #adjusting row number
            if (playerTwoChoices[-1][1] == 3):
                playerTwoChoices[-1][1] = 5
            elif(playerTwoChoices[-1][1] == 2):
                playerTwoChoices[-1][1] = 3
            #adjusting column number
            if (playerTwoChoices[-1][0] == 3):
                playerTwoChoices[-1][0] = 5
            elif(playerTwoChoices[-1][0] == 2):
                playerTwoChoices[-1][0] = 3
            #placing on board
            if (board[playerTwoChoices[-1][1]][playerTwoChoices[-1][0]] == " "):
                board[playerTwoChoices[-1][1]][playerTwoChoices[-1][0]] = playerTwo
                printBoard()
                print("Player One's Turn!")
            else:
                playerTwoChoices.pop()
                print("That spot already has a marker. Please choose again")
                continue
        
choose()
