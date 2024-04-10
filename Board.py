class Board:
    def __init__(self,team):
        self.team = team
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

#Key
# Blank: _
# Ship: *
# Miss: O
# Hit on ship: X


    def PrintBoard(self):
        if self.team == 0:
            print("Your Board")
        else:
            print("Enemy Board")
        alphanum=["A","B","C","D","E","F","G","H","I","J"]
        print("  1 2 3 4 5 6 7 8 9 10")
        for alpha in self.board:
            strToPrint = ""
            strToPrint+=alphanum[0]+" "
            alphanum.pop(0)
            for num in alpha:
                strToPrint+=num+" "
            print(strToPrint)
        print("")
    
    def SpotChange(self,alpha,num,type):
        self.board[alpha][num]="O"