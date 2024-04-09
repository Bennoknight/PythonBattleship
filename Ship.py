class Ship:
    def __init__(self, size):
        self.size = size
        self.sunk = False
        self.axis = 0
        self.LiveCoords = []

    def PlaceShip(self,coord):
        self.LiveCoords = coord

    def GetSize(self):
        return self.size