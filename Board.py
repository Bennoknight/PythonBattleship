class Board:
    def __init__(self):
        self.board = [["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"],
                 ["_","_","_","_","_","_","_","_","_","_"]]


    def PrintBoard(self):
        alphanum=["A","B","C","D","E","F","G","H","I","J"]
        print("  1 2 3 4 5 6 7 8 9 10")
        for alpha in self.board:
            strToPrint = ""
            strToPrint+=alphanum[0]+" "
            alphanum.pop(0)
            for num in alpha:
                strToPrint+=num+" "
            print(strToPrint)