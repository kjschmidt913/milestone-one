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
        
    else:
        if player == playerOne:
            playerOneChoices.pop()
        else:
            playerTwoChoices.pop()
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

def checkWinner():
    if len(playerOneChoices) >= 3:
        #very sure I can use a nested for loop to circle through these. hard coding just for now
        top = board[1][1] == board[1][3] and board[1][1] == board[1][5] and board[1][1] != " "
        middle = board[3][1] == board[3][3] and board[3][1] == board[3][5] and board[3][1] != " "
        bottom = board[5][1] == board[5][3] and board[5][1] == board[5][5] and board[5][1] != " "
        diagOne = board[1][5] == board[3][3] and board[1][5] == board[5][1] and board[1][5] != " "
        diagTwo = board[1][1] == board[3][3] and board[1][1] == board[5][5] and board[1][1] != " "
        colOne = board[1][1] == board[3][1] and board[1][1] == board[5][1] and board[1][1] != " "
        colTwo = board[1][3] == board[3][3] and board[1][3] == board[5][3] and board[1][3] != " "
        colThree = board[1][5] == board[3][5] and board[1][5] == board[5][5] and board[1][5] != " "

        if top or middle or bottom or diagOne or diagTwo or colOne or colTwo or colThree:
            print("You have won the game!")

        return top or middle or bottom or diagOne or diagTwo or colOne or colTwo or colThree

    else:
        return False


def choose():

    while not checkWinner():
        if (len(playerOneChoices) == len(playerTwoChoices)):
            print("Player One's Turn!")
        else:
            print("Player Two's Turn!")
            
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
    
    if len(playerOneChoices) == 5 and not checkWinner():
        print("No one wins")

        
choose()