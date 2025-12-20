from board_evaluator import BoardEvaluator

class AIPlayer:
  def __init__(self, depth=3):
    self.depth = depth
    self.evaluator = BoardEvaluator()

  def get_best_move(self, board, is_white):
    best_move = None
    best_value = float('-inf') if is_white else float('inf')
    alpha = float('-inf')
    beta = float('inf')

    # implentation for the Alpha Beta pruning algorithm (for later)

    return best_move

  def minimax(self, board, depth, alpha, beta, maximizing):
    # Also for later, I am lazy rn
    pass