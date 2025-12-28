class Move:

  def __init__(self, start_pos, end_pos, piece, captured_piece=None):
    self.start_pos = start_pos
    self.end_pos = start_pos
    self.piece = piece
    self.captured_piece = captured_piece

  def __str__(self):
    start = self.pos_to_chess_notation(self.start_pos)
    end = self.pos_to_chess_notation(self.end_pos)
    return f"{start} -> {end}"

  @staticmethod
  def pos_to_chess_notation(pos):
    """Converts (row, col) to chess notation (for example, e4)"""
    row, col = pos
    return f"{chr(97 + col)}{8 - row}"

  @staticmethod
  def chess_notation_to_pos(notation):
    """Converts chess notation (e4) to (row, col) format"""
    col = ord(notation[0]) - 97
    row = 8 - int(notation[1])
    return (row, col)