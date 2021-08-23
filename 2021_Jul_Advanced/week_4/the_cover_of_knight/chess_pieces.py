
from utils import exists

class Knight:
  """
  A Knight chess piece object.
  """
  
  @property
  def board(self):
    return self._board
  @board.setter
  def board(self, new_board):
    # Check that board is correctly shaped (ie. square => row = col)
    if len(new_board) == len(new_board[0]):
      self._board = new_board
    else:
      raise ValueError('The board must be square (ie. num of row = num of col)')
  
  def __init__(self, board, pos):
    """
    :param board: The board.
    :type board: list
    
    :param pos: The position of the knight as a list-like object. Index 0 should
                be the column index, while Index 1 should be the row index.
    :type pos: list-like (eg. tuple, list)
    """
    # Set the board
    self.board = board
    # Set the X position of the knight (horizontal - row)
    self._x_pos = pos[0]
    # Set the Y position of the knight (vertical - col)
    self._y_pos = pos[1]
  
  def get_moves(self):
    """
    Get all possible moves from the current position on the board.
    """
    combinations = self.get_combinations(self._x_pos, self._y_pos)
    
    possible = []
    for combination in combinations:
      if exists(self.board, combination):
        possible.append(combination)
    
    return possible
  
  def get_combinations(self, x, y):
    """
    Get positions of all knight moves from given coordinates.
    
    :param x: X-coordinate.
    :type x: int
    
    :param y: Y-coordinate.
    :type y: int
    
    :return: A tuple of all positions.
    :rtype: tuple
    """
    return (
      (x - 1, y - 2),
      (x + 1, y - 2),
      (x - 1, y + 2),
      (x + 1, y + 2),
      (x - 2, y + 1),
      (x - 2, y - 1),
      (x + 2, y - 1),
      (x + 2, y + 1)
    )