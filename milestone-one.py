print("Hello World")

board = {
    "row1" : [" ","|"," ","|"," "],
    "border" : ["-","-","-","-","-"],
    "row2": [" ","|"," ","|"," "],
    "row3" : [" ","|"," ","|"," "]
}

def printBoard():
    for spot in board["row1"]:
        print(spot, end="")
    print(" ")
    for spot in board["border"]:
        print(spot, end="")
    print(" ")
    for spot in board["row2"]:
        print(spot, end="")
    print(" ")
    for spot in board["border"]:
        print(spot, end="")
    print(" ")
    for spot in board["row3"]:
        print(spot, end="")
    print("\n")

printBoard()
    