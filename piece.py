class Piece:

  def __init__(self, color, position):
    self.color = color
    self.position = position
    self.has_moved = False

  def __str__(self):
    return self.symbol

  def is_valid_move(self, board, end_pos):
    """Check if move is valid for this piece type"""
    raise NotImplementedError

class Pawn(Piece):

  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = '♙' if color == 'white' else '♟'

  def is_valid_move(self, board, end_pos):
    start_row, start_col = self.position
    end_row, end_col = end_pos
    direction = -1 if self.color == 'white' else 1

    # Forward move
    if start_col == end_col:
      if end_row == start_row + direction and board[end_row][end_col] is None:
        return True

      # Double move from starting position
      if not self.has_moved and end_row == start_row + 2 * direction:
        if board[start_row + direction][start_col] is None and board[end_row][end_col] is None:
          return True

    # Capture other pieces diagonally
    if abs(end_col - start_col) == 1 and end_row == start_row + direction:
      if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
        return True

    return False

class Knight(Piece):

  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = '♘' if color == 'white' else '♞'

  def is_valid_move(self, board, end_pos):
    start_row, start_col = self.position
    end_row, end_col = end_pos

    row_diff = abs(end_row - start_row)
    col_diff = abs(end_col - start_col)

    if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
      target = board[end_row][end_col]
      return target is None or target.color != self.color
    return False

class Bishop(Piece):

  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = '♗' if color == 'white' else '♝'

  def is_valid_move(self, board, end_pos):
    start_row, start_col = self.position
    end_row, end_col = end_pos

    if abs(end_row - start_row) != abs(end_col - start_col):
      return False

    # Check if the path is clear
    row_step = 1 if end_row > start_row else -1
    col_step = 1 if end_col > start_col else -1

    current_row, current_col = start_row + row_step, start_col + col_step
    while (current_row, current_col) != (end_row, end_col):
      if board[current_row][current_col] is not None:
        return False
      current_row += row_step
      current_col += col_step

    target = board[end_row][end_col]
    return target is None or target.color != self.color

class Rook(Piece):

  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = '♖' if color == 'white' else '♜'

  def is_valid_move(self, board, end_pos):
    start_row, start_col = self.position
    end_row, end_col = end_pos

    if start_row != end_row and start_col != end_col:
      return False

    # Check if the paht is clear
    if start_row == end_row:
      step = 1 if end_col > start_col else -1
      for col in range(start_col + step, end_col, step):
        if board[start_row][col] is not None:
          return False
    else:
      step = 1 if end_row > start_row else -1
      for row in range(start_row + step, end_row, step):
        if board[row][start_col] is not None:
          return False

    target = board[end_row][end_col]
    return target is None or target.color != self.color

class Queen(Piece):

  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = '♕' if color == 'white' else '♛'

  def is_valid_move(self, board, end_pos):
    start_row, start_col = self.position
    end_row, end_col = end_pos

    # Check if it's a rook-like move
    if start_row == end_row or start_col == end_col:
      temp_rook = Rook(self.color, self.position)
      return temp_rook.is_valid_move(board, end_pos)

    # Check if it's a bishop-like move
    if abs(end_row - start_row) == abs(end_col - start_col):
      temp_bishop = Bishop(self.color, self.position)
      return temp_bishop.is_valid_move(board, end_pos)

    return False

class King(Piece):

  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = '♔' if color == 'white' else '♚'

  def is_valid_move(self, board, end_pos):
    start_row, start_col = self.position
    end_row, end_col = end_pos

    row_diff = abs(end_row - start_row)
    col_diff = abs(end_col - start_col)

    if row_diff <= 1 and col_diff <= 1 and (row_diff + col_diff) > 0:
      target = board[end_row][end_col]
      return target is None or target.color != self.color
    return False