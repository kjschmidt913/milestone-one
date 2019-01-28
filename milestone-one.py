board = [
    ["  ", "1", " ", "2", " ", "3"],
    ["1 "," ","|"," ","|"," "],
    ["  ","-","-","-","-","-"],
    ["2 "," ","|"," ","|"," "],
    ["  ","-","-","-","-","-"],
    ["3 "," ","|"," ","|"," "]
]
playerOne = " "
playerOneChoices = []
playerTwoChoices = []

def printBoard():
    print("\n")
    for row in board:
        for spot in row:
            print(spot, end="") 
        print(" ")
    print("\n")

def adjustToList(colRow):
    #adjusting row number
        #3 always == 5, 2 always  == 3, 1 always == 1
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

def checkWinner():
    if len(playerOneChoices) >= 3:
        
        #checks for top middle bottom row wins
        for row in board[1::2]:
            if row[3] == " ":
                continue
            elif row[3] == row[1] and row[3] == row[5]:
                print("You have won the game!")
                return True
        
        #checks for column wins
        for i in range(1, 6, 2):
            if board[3][i] == " ":
                continue
            elif board[3][i] == board[3-2][i] and board[3][i] == board[3+2][i]:
                print("You have won the game!")
                return True
        
        diagOne = board[1][5] == board[3][3] and board[1][5] == board[5][1] and board[1][5] != " "
        diagTwo = board[1][1] == board[3][3] and board[1][1] == board[5][5] and board[1][1] != " "
        
        if diagOne or diagTwo:
            print("You have won the game!")
            return True
        else:
            return False

    else:
        return False

def choose():
    while not checkWinner():
        if len(playerOneChoices) == 5:
            print("No one wins")
            break

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
    
    


#Game playing starts here
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
choose()

