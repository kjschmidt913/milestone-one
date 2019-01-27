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


printBoard()
    