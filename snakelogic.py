from moveenums import Moves
from gameobjects import Board, Snake
import random

class Game:
  def __init__(self, board, you):
    self.board = Board(board)
    self.me = Snake(you)
 
  def move(self):
    m, s = self.logic()
    return {"move": m.value, "shout":s}

  def logic(self):
    # Add your snake logic here
    # return direction and shout
    print(self.me.head)
    choices = list(Moves)
    new_direction = random.choice(choices)
    print(f"new direction is {new_direction.name}")
    return (new_direction, "")
