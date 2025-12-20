from chess_engine import ChessGame
from ai_player import AIPlayer

def main():
  print("----- AI Chess Bot -----")
  print("Select difficulty:")
  print("1. Easy") # depth 2
  print("2. Medium") # depth 3
  print("3. Hard") # depth 4

  difficulty = int(input("Enter choice: ")) # add input validation later
  depth_map = {1: 2, 2: 3, 3: 4}

  game = ChessGame()
  ai = AIPlayer(depth=depth_map.get(difficulty, 3))

  # Game loop will go here, when I actually get to that part

  if __name__ == "__main__":
    main()
