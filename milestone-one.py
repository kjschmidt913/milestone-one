board = [
    [" ","|"," ","|"," "],
    ["-","-","-","-","-"],
    [" ","|"," ","|"," "],
    ["-","-","-","-","-"],
    [" ","|"," ","|"," "]
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
    