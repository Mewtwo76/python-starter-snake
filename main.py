from flask import request
from flask_api import FlaskAPI
from snakelogic import Game

import json

app = FlaskAPI(__name__)

with open('./snake_info.json') as f:
  my_snake_info = json.load(f)

@app.route("/", methods=['GET'])
def snake_info():
  return my_snake_info

@app.route("/start", methods=['POST'])
def snake_start():
  return ('', 204)

@app.route("/move", methods=['POST'])
def snake_move():
  req = request.get_json()
  game = Game(req['board'], req['you'])
  m = game.move()
  return m

@app.route("/end", methods=['POST'])
def snake_end():
  return ('', 204)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)