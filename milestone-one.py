board = [
    [" ","|"," ","|"," "],
    ["-","-","-","-","-"],
    [" ","|"," ","|"," "],
    ["-","-","-","-","-"],
    [" ","|"," ","|"," "]
]

def printBoard():
    for row in board:
        for spot in row:
            print(spot, end="") 
        print(" ")
    print("\n") 

playerOne = input("Player One, choose either X or O for your marker: ")

if playerOne == "X":
    playerTwo = "O"
else:
    playerTwo = "X"
print(f"Player Two, your marker is {playerTwo}")


printBoard()
    