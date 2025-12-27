from piece import Pawn, Knight, Bishop, Rook, Queen, King

class BoardEvaluator:

  PIECE_VALUES = {
    'Pawn': 100,
    'Knight': 320,
    'Bishop': 330,
    'Rook': 500,
    'Queen': 900,
    'King': 20000
  }

  # Positional bonus tables from white's perspective
  PAWN_TABLE = [
    [0,  0,  0,  0,  0,  0,  0,  0],
    [50, 50, 50, 50, 50, 50, 50, 50],
    [10, 10, 20, 30, 30, 20, 10, 10],
    [5,  5, 10, 25, 25, 10,  5,  5],
    [0,  0,  0, 20, 20,  0,  0,  0],
    [5, -5,-10,  0,  0,-10, -5,  5],
    [5, 10, 10,-20,-20, 10, 10,  5],
    [0,  0,  0,  0,  0,  0,  0,  0]
  ]

  KNIGHT_TABLE = [
    [-50,-40,-30,-30,-30,-30,-40,-50],
    [-40,-20,  0,  0,  0,  0,-20,-40],
    [-30,  0, 10, 15, 15, 10,  0,-30],
    [-30,  5, 15, 20, 20, 15,  5,-30],
    [-30,  0, 15, 20, 20, 15,  0,-30],
    [-30,  5, 10, 15, 15, 10,  5,-30],
    [-40,-20,  0,  5,  5,  0,-20,-40],
    [-50,-40,-30,-30,-30,-30,-40,-50]
  ]

  BISHOP_TABLE = [
    [-20,-10,-10,-10,-10,-10,-10,-20],
    [-10,  0,  0,  0,  0,  0,  0,-10],
    [-10,  0,  5, 10, 10,  5,  0,-10],
    [-10,  5,  5, 10, 10,  5,  5,-10],
    [-10,  0, 10, 10, 10, 10,  0,-10],
    [-10, 10, 10, 10, 10, 10, 10,-10],
    [-10,  5,  0,  0,  0,  0,  5,-10],
    [-20,-10,-10,-10,-10,-10,-10,-20]
  ]

  ROOK_TABLE = [
    [0,  0,  0,  0,  0,  0,  0,  0],
    [5, 10, 10, 10, 10, 10, 10,  5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [-5,  0,  0,  0,  0,  0,  0, -5],
    [0,  0,  0,  5,  5,  0,  0,  0]
  ]

  QUEEN_TABLE = [
    [-20,-10,-10, -5, -5,-10,-10,-20],
    [-10,  0,  0,  0,  0,  0,  0,-10],
    [-10,  0,  5,  5,  5,  5,  0,-10],
    [-5,  0,  5,  5,  5,  5,  0, -5],
    [0,  0,  5,  5,  5,  5,  0, -5],
    [-10,  5,  5,  5,  5,  5,  0,-10],
    [-10,  0,  5,  0,  0,  0,  0,-10],
    [-20,-10,-10, -5, -5,-10,-10,-20]
  ]

  KING_TABLE = [
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-30,-40,-40,-50,-50,-40,-40,-30],
    [-20,-30,-30,-40,-40,-30,-30,-20],
    [-10,-20,-20,-20,-20,-20,-20,-10],
    [20, 20,  0,  0,  0,  0, 20, 20],
    [20, 30, 10,  0,  0, 10, 30, 20]
  ]

  def evaluate(self, board):
    """
    Evaluates the board from white's perspective.
    Positive score means that white is winning,
    negative means black is winning.
    """

    score = 0

    for row in range(8):
      for col in range(8):
        piece = board[row][col]
        if piece is not None:
          piece_value = self._get_piece_value(piece, row, col)
          if piece.color == 'white':
            score += piece_value
          else:
            score -= piece_value

    return score

  def _get_piece_value(self, piece, row, col):
    """Get total value of a piece including the positional bonus"""
    piece_type = type(piece).__name__
    material_value = self.PIECE_VALUES[piece_type]

    position_value = 0
    if piece_type == 'Pawn':
      position_value = self.PAWN_TABLE[row][col] if piece.color == 'white' else self.PAWN_TABLE[7-row][col]
    elif piece_type == 'Knight':
      position_value = self.KNIGHT_TABLE[row][col] if piece.color == 'white' else self.KNIGHT_TABLE[7-row][col]
    elif piece_type == 'Bishop':
        position_value = self.BISHOP_TABLE[row][col] if piece.color == 'white' else self.BISHOP_TABLE[7-row][col]
    elif piece_type == 'Rook':
        position_value = self.ROOK_TABLE[row][col] if piece.color == 'white' else self.ROOK_TABLE[7-row][col]
    elif piece_type == 'Queen':
        position_value = self.QUEEN_TABLE[row][col] if piece.color == 'white' else self.QUEEN_TABLE[7-row][col]
    elif piece_type == 'King':
        position_value = self.KING_TABLE[row][col] if piece.color == 'white' else self.KING_TABLE[7-row][col]

    return material_value + position_value