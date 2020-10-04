class Pos:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"x: {self.x}, y:{self.y}"

class Food:
  def __init__(self, food):
    self.pos = Pos(food['x'], food['y'])

class Hazard:
  def __init__(self, hazard):
    self.pos = Pos(hazard['x'], hazard['y'])

class Snake:
  def __init__(self, snake):
    self.id = snake['id']
    self.name = snake['name']
    self.health = snake['health']
    self.body = []
    for value in snake['body']:
      self.body.append(Pos(value['x'], value['y']))
    self.latency = snake['latency']
    self.head = Pos(snake['head']['x'], snake['head']['y'])
    self.length = ['length']
    self.shout = ['shout']
    self.squad = ['squad']

class Board:
  def __init__(self, board):
    self.height = board['height']
    self.width = board['width']
    self.food = []
    for value in board['food']:
      self.food.append(Food(value))
    self.snakes = []
    for value in board['snakes']:
      self.snakes.append(Snake(value))
    self.hazards = []
    for value in board['hazards']:
      self.hazards.append(Hazard(value))