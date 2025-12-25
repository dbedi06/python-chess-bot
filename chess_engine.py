from piece import Pawn, Knight, Bishop, Rook, Queen, King
from move import Move
import copy

class ChessGame:

  def __init__(self):
    self.board = self._create_board()
    self.current_turn = 'white'
    self.move_history = []
    self.white_king_pos = (7, 4)
    self.black_king_pos = (0, 4)

  def _create_board(self):
    """Initialize the chess board with pieces"""
    board = [[None for i in range(8)] for i in range(8)]

    # Black pieces (on the top of the board)
    board[0][0] = Rook('black', (0,0))
    board[0][1] = Knight('black', (0, 1))
    board[0][2] = Bishop('black', (0, 2))
    board[0][3] = Queen('black', (0, 3))
    board[0][4] = King('black', (0, 4))
    board[0][5] = Bishop('black', (0, 5))
    board[0][6] = Knight('black', (0, 6))
    board[0][7] = Rook('black', (0, 7))

    for col in range(8):
      board[1][col] = Pawn('black', (1, col))

    # White pieces (on the bottom of the board)
    for col in range(8):
      board[6][col] = Pawn('white', (6, col))

    board[7][0] = Rook('white', (7, 0))
    board[7][1] = Knight('white', (7, 1))
    board[7][2] = Bishop('white', (7, 2))
    board[7][3] = Queen('white', (7, 3))
    board[7][4] = King('white', (7, 4))
    board[7][5] = Bishop('white', (7, 5))
    board[7][6] = Knight('white', (7, 6))
    board[7][7] = Rook('white', (7, 7))

    return board

  def display_board(self):
    """Displays the current state of the board"""
    print("\n  a b c d e f g h")
    for row in range(8):
      print(f"{8-row}|", end="")
      for col in range(8):
        piece = self.board[row][col]
        if piece is None:
          print(". ", end="")
        else:
          print(f"{piece.symbol} ", end="")
      print(f"|{8-row}")
    print("  ---------------")
    print("  a b c d e f g h\n")

  def get_legal_moves(self, color):
    """Get all legal moves for a given color"""
    moves = []
    for row in range(8):
      for col in range(8):
        piece = self.board[row][col]
        if piece and piece.color == color:
          piece_moves = self._get_piece_moves(piece)
          moves.extend(piece_moves)
    return moves

  def _get_piece_moves(self, piece):
    """Get all legal moves for a specific piece"""
    moves = []
    start_pos = piece.position

    for row in range(8):
      for col in range(8):
        end_pos = (row, col)
        if start_pos != end_pos and piece.is_valid_move(self.board, end_pos):
          # Check if move doesn't leave king in check
          if not self._move_causes_check(start_pos, end_pos, piece.color):
            captured = self.board[row][col]
            moves.append(Move(start_pos, end_pos, piece, captured))

    return moves

  def _move_causes_check(self, start_pos, end_pos, color):
    """Check if a move would leave the king in check"""
    # Make a temporary move
    temp_board = copy.deepcopy(self.board)
    temp_piece = temp_board[start_pos[0]][start_pos[1]]
    temp_board[end_pos[0]][end_pos[1]] = temp_piece
    temp_board[start_pos[0]][start_pos[1]] = None
    temp_piece.position = end_pos

    # Find king position
    king_pos = None
    for row in range(8):
      for col in range(8):
        piece = temp_board[row][col]
        if piece and isinstance(piece, King) and piece.color == color:
          king_pos = (row, col)
          break
      if king_pos:
        break

    # Check if any opponent piece can attack the king
    opponent_color = 'black' if color == 'white' else 'white'
    for row in range(8):
      for col in range(8):
        piece = temp_board[row][col]
        if piece and piece.color == opponent_color:
          if piece.is_valid_move(temp_board, king_pos):
            return True

    return False

  def make_move(self, move):
    """Execute a move on the board"""
    start_row, start_col = move.start_pos
    end_row, end_col = move.end_pos

    piece = self.board[start_row][start_col]

    # Move the piece
    self.board[end_row][end_col]
    self.board[start_row][start_col] = None
    piece.position = move.end_pos
    piece.has_moved = True

    # Update king position
    if isinstance(piece, King):
      if piece.color == 'white':
        self.white_king_pos = move.end_pos
      else:
        self.black_king_pos = move.end_pos

    self.move_history.append(move)
    self.current_turn = 'black' if self.current_turn == 'white' else 'white'

  def is_checkmate(self, color):
    """Check if the given color is in checkmate"""
    return len(self.get_legal_moves(color)) == 0 and self.is_in_check(color)

  def is_stalemate(self, color):
    """Check if the given color is in stalemate"""
    return len(self.get_legal_moves(color)) == 0 and not self.is_in_check(color)

  def is_in_check(self, color):
    """Check if the given color's king is in check"""
    king_pos = self.white_king_pos if color == 'white' else self.black_king_pos
    opponent_color = 'black' if color == 'white' else 'white'

    for row in range(8):
      for col in range(8):
        piece = self.board[row][col]
        if piece and piece.color == opponent_color:
          if piece.is_valid_move(self.board, king_pos):
            return True

    return False

  def is_game_over(self):
    """Check if the game is over"""
    return (self.is_checkmate('white') or self.is_checkmate('black') or
            self.is_stalemate('white') or self.is_stalemate('black'))