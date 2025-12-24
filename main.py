from chess_engine import ChessGame
from ai_player import AIPlayer
from move import Move

def main():
  print("----- AI Chess Bot -----")

  print("\nSelect game mode:")
  print("1. Human (White) vs AI (Black)")
  print("2. AI (White) vs Human (Black)")
  print("3. AI vs AI (watch)")

  mode = input("\nEnter choice (1-3): ").strip()

  print("Select difficulty:")
  print("1. Easy") # depth 2
  print("2. Medium") # depth 3
  print("3. Hard") # depth 4

  difficulty = input("\nEnter choice (1-3): ").strip()
  depth_map = {'1': 2, '2': 3, '3': 4}
  ai_depth = depth_map.get(difficulty, 3) # depth 3 by default

  game = ChessGame()
  ai = AIPlayer(depth=ai_depth)

  print(f"\nStarting the game with AI depth: {ai_depth}")
  print("Enter moves in format: e2e4 (from-square to-square, no spaces)")
  print("Type 'quit' to exit\n")

  human_color = None
  if mode == '1':
    human_color = 'white'
  elif mode == '2':
    human_color = 'black'
  # For the third mode, the color stays none since it is AI vs AI

  move_count = 0

  while not game.is_game_over():
    game.display_board()
    print(f"Move {move_count + 1} - {game.current_turn.upper()}'s turn")

    if game.is_in_check(game.current_turn):
      print("CHECK!!!")

    if human_color is None or game.current_turn != human_color:
      best_move = ai.get_best_move(game)

      if best_move:
        print(f"AI plays: {best_move}")
        game.make_move(best_move)
        move_count += 1
      else:
        print("AI has no legal moves!")
        break

      if mode == '3':
        input("\nPress Enter for next move...")

    else: # If it is the human's turn
      legal_moves = game.get_legal_moves(game.current_turn)

      if len(legal_moves) == 0:
        print("No legal moves available!")
        break

      while True:
        user_input = input(f"Your move ({game.current_turn}): ").strip().lower()

        if user_input == 'quit':
          print("Your Mama raised a quitter! Walk away in shame!") # Motivating my users to never quit again lol
          return

        if user_input == 'help':
          print("\nAvailable moves:")
          for move in legal_moves[:10]: #Shows them the first 10 legal moves
            print(f"  {move}")
          if len(legal_moves) > 10:
            print(f"  ...and {len(legal_moves) - 10} more")
          continue

        if len(user_input) == 4:
          try:
            start_notation = user_input[:2] # Parsing the moves, for example: (e2e4) turns into e2 and e4
            end_notation = user_input[2:]

            start_pos = Move.chess_notation_to_pos(start_notation)
            end_pos = Move.chess_notation_to_pos(end_notation)

            selected_move = None
            for move in legal_moves:
              if move.start_pos == start_pos and move.end_pos == end_pos:
                selected_move = move
                break

            if selected_move:
              game.make_move(selected_move)
              move_count += 1
              break
            else:
              print("Illegal move! Try again or type 'help'.")
          except:
            print("Invalid format! Use format like 'e2e4'.")
        else:
          print("Invalid format! Use format like 'e2e4' or type 'help'.")

  game.display_board()
  print("\n" + "=" * 50)
  print("  GAME OVER")
  print("=" * 50)

  if game.is_checkmate('white'):
    print("BLACK WINS by checkmate!")
  elif game.is_checkmate('black'):
    print("WHITE WINS by checkmate!")
  elif game.is_stalemate('white') or game.is_stalemate('black'):
    print("DRAW by stalemate!")

  print(f"\nTotal moves: {move_count}")
  print("Thanks for playing!\n")

if __name__ == "__main__":
   main()
