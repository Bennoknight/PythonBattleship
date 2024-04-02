default_board = [["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"]]

class Ship:
    def __init__(self, size):
        self.size = size
        self.sunk = False
        self.axis = 0
        self.LiveCoords = []

    def PlaceShip(self,coord):
        self.LiveCoords = coord


def print_board(board):
    alphanum=["A","B","C","D","E","F","G","H","I","J"]
    print("  1 2 3 4 5 6 7 8 9 10")
    for alpha in board:
        strToPrint = ""
        strToPrint+=alphanum[0]+" "
        alphanum.pop(0)
        for num in alpha:
            strToPrint+=num+" "
        print(strToPrint)

#print_board(default_board)