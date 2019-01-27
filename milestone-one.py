board = [
    ["  ", "1", " ", "2", " ", "3"],
    ["1","  ","|"," ","|"," "],
    ["  ","-","-","-","-","-"],
    ["2","  ","|"," ","|"," "],
    ["  ","-","-","-","-","-"],
    ["3","  ","|"," ","|"," "]
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
    print("Choose your spot by entering the column number then the row number.")
    choiceColumn = input("Column Number: ")
    choiceRow = input("Row Number: ")

    #if it's player one
    if (len(playerOneChoices) == len(playerTwoChoices)):
        playerOneChoices.append([int(choiceColumn), int(choiceRow)])
        #adjusting row number
        if (playerOneChoices[-1][1] == 3):
            playerOneChoices[-1][1] = 5
        elif(playerOneChoices[-1][1] == 2):
            playerOneChoices[-1][1] = 3
        #adjusting column number
        if (playerOneChoices[-1][0] == 3):
            playerOneChoices[-1][0] = 5
        elif(playerOneChoices[-1][0] == 2):
            playerOneChoices[-1][0] = 3
        
        board[playerOneChoices[-1][1]][playerOneChoices[-1][0]] = playerOne
        printBoard()
    else:
        playerTwoChoices.append([int(choiceColumn), int(choiceRow)])

    print(playerOneChoices)


choose()
    
#3 always == 5
#2 always  == 3
#1 always == 1