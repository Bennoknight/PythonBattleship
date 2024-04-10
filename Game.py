import Board
import Ship
import EnemyAI

win = False
PlayerShips=[]
EnemyShips=[]


PlayerBoard = Board.Board(0)
EnemyBoard = Board.Board(1)

PlayerBoard.SpotChange(0,1,"miss")
PlayerBoard.PrintBoard()