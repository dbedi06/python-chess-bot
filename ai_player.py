from board_evaluator import BoardEvaluator
import copy

class AIPlayer:
  def __init__(self, depth=3):
    self.depth = depth
    self.evaluator = BoardEvaluator()
    self.nodes_evaluated = 0

  def get_best_move(self, game):
    """Find the best move using Minimax with Alpha-Beta pruning"""
    self.nodes_evaluated = 0
    best_move = None
    alpha = float('-inf')
    beta = float('inf')

    # Maximizing for white, minimizing for black (not racism)
    is_maximizing = game.current_turn == 'white'
    best_value = float('-inf') if is_maximizing else float('inf')

    legal_moves = game.get_legal_moves(game.current_turn)

    # Order moves: captures first (simple move ordering for better pruning)
    legal_moves.sort(key=lambda m: m.captured_piece is not None, reverse=True)

    for move in legal_moves:
      # Make move on copy
      game_copy = self._copy_game(game)
      game_copy.make_move(move)

      # Evaluate position
      value = self._minimax(game_copy, self.depth - 1, alpha, beta, not is_maximizing)

      # Update best move
      if is_maximizing:
        if value > best_value:
          best_value = value
          best_move = move
        alpha = max(alpha, value)

      else:
        if value < best_value:
          best_value = value
          best_move = move
        beta = min(beta, value)

    print(f"Nodes evaluated: {self.nodes_evaluated}")
    print(f"Best move evaluation: {best_value}")

    return best_move

  def minimax(self, game, depth, alpha, beta, is_maximizing):
    """Minimax algorithm with Alpha-Beta pruning"""
    self.nodes_evaluated += 1

    # Base case: depth 0 or game over
    if depth == 0 or game.is_game_over():
      return self.evaluator.evaluate(game.board)

    legal_moves = game.get_legal_moves(game.current_turn)

    # Checkmate or stalemate
    if len(legal_moves) == 0:
      if game.is_in_check(game.current_turn):
        # Checkmate - return extreme value
        return -100000 if is_maximizing else 100000
      else:
        # Stalemate - return draw value
        return 0

    # Move orderin: captures first
    legal_moves.sort(key=lambda m: m.captured_piece is not None, reverse=True)

    if is_maximizing:
      max_eval = float('-inf')
      for move in legal_moves:
        game_copy = self._copy_game(game)
        game_copy.make_move(move)
        eval_score = self._minimax(game_copy, depth - 1, alpha, beta, False)
        max_eval = max(max_eval, eval_score)
        alpha = max(alpha, eval_score)
        if beta <= alpha:
          break # Beta cutoff
      return max_eval
    else:
      min_eval = float('inf')
      for move in legal_moves:
        game_copy = self._copy_game(game)
        game_copy.make_move(move)
        eval_score = self._minimax(game_copy, depth - 1, alpha, beta, True)
        min_eval = min(min_eval, eval_score)
        beta = min(beta, eval_score)
        if beta <= alpha:
          break # Alpha cutoff
      return min_eval

  def _copy_game(self, game):
    """Creates a deep copy of the game state."""
    return copy.deepcopy(game)